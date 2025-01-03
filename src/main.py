"""Main application module for Financial Analyzer."""
import os
import json
import pandas as pd
from dotenv import load_dotenv
from typing import List, Dict, Any

from data_collectors.simply_wall_st import SimplyWallStCollector
from data_collectors.yahoo_finance import YahooFinanceCollector
from database.db_manager import DatabaseManager
from preprocessors.data_preprocessor import DataPreprocessor
from analyzer.openai_analyzer import OpenAIAnalyzer

def load_portfolio_data(file_path: str) -> pd.DataFrame:
    """Load and process portfolio data from CSV file.
    
    Args:
        file_path: Path to the portfolio CSV file
        
    Returns:
        DataFrame containing processed portfolio data
    """
    print("\nReading CSV file...")
    df = pd.read_csv(
        file_path,
        sep=";",
        skiprows=10,      # Skip the metadata so the row with "Position;Bezeichnung;WKN;..." is the first row read
        header=0,         # Treat that row as the header
        skipfooter=7,     # Skip disclaimers at the bottom
        engine="python",  # Required when using skipfooter
        decimal=",",      # Interpret commas as decimals
        thousands=".",    # Interpret dots as thousand separators
    )
    
    # Print raw data for debugging
    print("\nRaw data - first few rows:")
    print(df.head())
    
    # Print original column names
    print("\nOriginal column names:")
    print([f"'{col}'" for col in df.columns.tolist()])
    
    # Clean column names by stripping whitespace
    df.columns = df.columns.str.strip()
    
    # Print cleaned column names
    print("\nCleaned column names:")
    print([f"'{col}'" for col in df.columns.tolist()])
    
    # Fix swapped columns - the actual WKN is in the Bezeichnung column
    df = df.rename(columns={
        'Position': 'Bezeichnung_temp',
        'Bezeichnung': 'WKN',
        'WKN': 'ISIN_temp'
    })
    df['Position'] = df.index + 1
    
    # Keep only relevant columns
    relevant_cols = [
        "Position",
        "Bezeichnung_temp",
        "WKN",
        "ISIN_temp",
        "Bestand",
        "Einstandskurs",
        "Einstandswert in EUR",
        "akt. Kurs",
        "Veränderung in %",
    ]
    
    # Print which relevant columns were found
    print("\nChecking for relevant columns:")
    for col in relevant_cols:
        if col in df.columns:
            print(f"Found column: '{col}'")
        else:
            print(f"Missing column: '{col}'")
    
    # Filter out any columns not in relevant_cols (if they exist in df)
    df = df[[col for col in relevant_cols if col in df.columns]]
    
    # Print sample of WKN values
    print("\nSample of WKN values:")
    if 'WKN' in df.columns:
        print(df['WKN'].head())
    else:
        print("WKN column not found!")
    
    # Convert numeric columns to float
    numeric_cols = ["Bestand", "Einstandskurs", "Einstandswert in EUR", "akt. Kurs", "Veränderung in %"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            
    # Drop any rows that don't have a WKN
    df = df.dropna(subset=["WKN"])
    
    return df

def read_portfolio() -> List[str]:
    """Read portfolio tickers from portfolio.csv file.
    
    Returns:
        List of stock tickers from the portfolio
    """
    try:
        # Load portfolio data
        df = load_portfolio_data('portfolio.csv')
        
        # Create a mapping of WKN to tickers
        wkn_to_ticker = {
            '840400': 'ALV.DE',    # Allianz SE
            'A1J4U4': 'ASML.AS',   # ASML Holding
            '863186': 'AMD',       # Advanced Micro Devices
            'A14Y6H': 'GOOG',      # Alphabet Inc. Class C
            'A0YJQ2': 'BRK-B',     # Berkshire Hathaway B
            'A2PK2R': 'CRWD',      # Crowdstrike Holdings
            '870747': 'MSFT',      # Microsoft
            'A2ACQE': 'NTNX',      # Nutanix Inc.
            '918422': 'NVDA',      # NVIDIA Corp
            '909800': 'TSM',       # Taiwan Semiconductor ADR
            'A1CX3T': 'TSLA'       # Tesla Inc.
        }
        
        # Extract tickers from WKN
        tickers = []
        for _, row in df.iterrows():
            wkn = row['WKN'].strip()
            if wkn in wkn_to_ticker:
                tickers.append(wkn_to_ticker[wkn])
            else:
                print(f"Warning: Could not find ticker for WKN {wkn}")
        
        print(f"Found {len(tickers)} stocks in portfolio: {tickers}")
        return tickers
    except Exception as e:
        print(f"Error reading portfolio: {str(e)}")
        return []

class FinancialAnalyzer:
    def __init__(self):
        load_dotenv()
        self.simply_wall_st = SimplyWallStCollector()
        self.yahoo_finance = YahooFinanceCollector()
        self.db_manager = DatabaseManager()
        self.preprocessor = DataPreprocessor()
        self.analyzer = OpenAIAnalyzer()
        
        # Verify required API keys
        if not os.getenv('OPENAI_API_KEY'):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
    def analyze_stock(self, ticker: str, portfolio_tickers: List[str]) -> Dict[str, Any]:
        """Analyze a stock and compare it with portfolio companies.
        
        Args:
            ticker: Stock ticker to analyze
            portfolio_tickers: List of portfolio stock tickers
            
        Returns:
            Dict containing analysis results
        """
        # First check if we have recent analysis
        saved_analysis = self.db_manager.get_analysis_results(ticker)
        if saved_analysis:
            print(f"\nFound saved analysis for {ticker} from {saved_analysis['last_updated']}")
            return saved_analysis['analysis_results']
        
        # Collect data for target stock
        stock_data = self._collect_stock_data(ticker)
        if not stock_data.get('yahoo_data'):
            return {'error': f'Failed to fetch data for {ticker}'}
        
        # Collect data for portfolio companies
        portfolio_data = []
        for pticker in portfolio_tickers:
            data = self._collect_stock_data(pticker)
            if data and data.get('yahoo_data'):
                portfolio_data.append(data)
        
        if not portfolio_data:
            return {'error': 'Failed to fetch data for any portfolio companies'}
        
        # Preprocess data
        processed_data = self.preprocessor.preprocess_stock_data(
            stock_data, portfolio_data
        )
        
        # Analyze data
        analysis_results = self.analyzer.analyze_stock(processed_data)
        
        # Save analysis results
        self.db_manager.save_analysis_results(ticker, analysis_results)
        
        return analysis_results
    
    def _collect_stock_data(self, ticker: str) -> Dict[str, Any]:
        """Collect stock data from all sources.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict containing combined stock data
        """
        # Check if we have recent data in database
        db_data = self.db_manager.get_stock_data(ticker)
        if db_data:
            return db_data
            
        print(f"\nCollecting data for {ticker}:")
        print("=" * 50)
            
        # Collect new data
        yahoo_data = self.yahoo_finance.get_stock_data(ticker)
        simply_wall_st_data = self.simply_wall_st.get_company_data(ticker)
        
        if simply_wall_st_data:
            print(f"\nSimply Wall Street data for {ticker}:")
            print("-" * 50)
            print("Company Info:")
            print(f"Name: {simply_wall_st_data.get('name')}")
            print(f"Market Cap: ${simply_wall_st_data.get('marketCap')/1e9:.2f}B")
            print(f"Exchange: {simply_wall_st_data.get('exchangeSymbol')}")
            print(f"Market: {simply_wall_st_data.get('market')}")
            
            print("\nKey Statements:")
            for statement in simply_wall_st_data.get('statements', []):
                if statement['area'] in ['HEALTH', 'PAST', 'FUTURE', 'VALUE']:
                    print(f"- {statement['description']}")
            print("-" * 50)
        
        if not yahoo_data:
            print(f"Warning: Failed to fetch Yahoo Finance data for {ticker}")
            return {}
        
        # Save to database
        self.db_manager.save_stock_data(
            ticker, yahoo_data, simply_wall_st_data
        )
        
        return {
            'yahoo_data': yahoo_data,
            'simply_wall_st_data': simply_wall_st_data
        }

def main():
    """Main entry point."""
    analyzer = FinancialAnalyzer()
    
    # Get portfolio tickers
    portfolio = read_portfolio()
    if not portfolio:
        print("Error: Could not read portfolio. Using default tickers.")
        portfolio = ["AAPL", "MSFT", "GOOGL"]
    
    print("\nAnalyzing against portfolio stocks:", portfolio)
    
    # Example usage - analyze NVIDIA against portfolio
    ticker = "NVDA"
    results = analyzer.analyze_stock(ticker, portfolio)
    print("\nAnalysis Results:")
    print("=" * 50)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
