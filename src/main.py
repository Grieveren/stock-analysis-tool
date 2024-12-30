"""Main application module for Financial Analyzer."""
import os
import json
from dotenv import load_dotenv
from typing import List, Dict, Any

from data_collectors.simply_wall_st import SimplyWallStCollector
from data_collectors.yahoo_finance import YahooFinanceCollector
from database.db_manager import DatabaseManager
from preprocessors.data_preprocessor import DataPreprocessor
from analyzer.openai_analyzer import OpenAIAnalyzer

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
    
    # Example usage
    ticker = "NVDA"
    portfolio = ["AAPL", "MSFT", "GOOGL"]
    
    results = analyzer.analyze_stock(ticker, portfolio)
    print("\nAnalysis Results:")
    print("=" * 50)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
