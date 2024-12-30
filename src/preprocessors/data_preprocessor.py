"""Data preprocessing module."""
from typing import Dict, Any, List
import pandas as pd

class DataPreprocessor:
    def __init__(self):
        self.key_metrics = [
            'marketCap', 'forwardPE', 'priceToBook',
            'returnOnEquity', 'debtToEquity', 'currentRatio'
        ]
        
    def preprocess_stock_data(self, stock_data: Dict[str, Any], 
                            portfolio_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Preprocess stock and portfolio data for analysis.
        
        Args:
            stock_data: Data for the stock being analyzed
            portfolio_data: List of data for portfolio companies
            
        Returns:
            Dict containing preprocessed data ready for analysis
        """
        # Extract key metrics
        stock_metrics = self._extract_metrics(stock_data)
        
        # Process portfolio data
        portfolio_metrics = [self._extract_metrics(data) for data in portfolio_data]
        portfolio_df = pd.DataFrame(portfolio_metrics)
        
        # Calculate portfolio averages
        portfolio_averages = portfolio_df.mean().to_dict()
        
        return {
            'stock_metrics': stock_metrics,
            'portfolio_averages': portfolio_averages,
            'raw_portfolio_data': portfolio_metrics,
            'statements': stock_data.get('simply_wall_st_data', {}).get('statements', [])
        }
    
    def _extract_metrics(self, data: Dict[str, Any]) -> Dict[str, float]:
        """Extract key metrics from raw data.
        
        Args:
            data: Raw stock data
            
        Returns:
            Dict containing key financial metrics
        """
        metrics = {}
        yahoo_data = data.get('yahoo_data', {}).get('info', {})
        simply_wall_st_data = data.get('simply_wall_st_data', {})
        
        # Extract metrics from Yahoo Finance
        metrics['marketCap'] = yahoo_data.get('marketCap')
        metrics['forwardPE'] = yahoo_data.get('forwardPE')
        metrics['priceToBook'] = yahoo_data.get('priceToBook')
        metrics['returnOnEquity'] = yahoo_data.get('returnOnEquity')
        metrics['debtToEquity'] = yahoo_data.get('debtToEquity')
        metrics['currentRatio'] = yahoo_data.get('currentRatio')
        
        # Update with Simply Wall Street data if available
        if simply_wall_st_data:
            # Market cap is in USD
            if simply_wall_st_data.get('marketCap'):
                metrics['marketCap'] = simply_wall_st_data['marketCap']
                
            # Extract metrics from statements
            for statement in simply_wall_st_data.get('statements', []):
                if statement['name'] == 'IsReturnOnEquityAboveThreshold':
                    # Extract ROE from description (e.g., "NVDA's Return on Equity (95.7%) is considered outstanding.")
                    desc = statement['description']
                    try:
                        roe = float(desc.split('(')[1].split('%')[0])
                        metrics['returnOnEquity'] = roe
                    except:
                        pass
                        
                elif statement['name'] == 'IsGoodHealthIntro':
                    # Extract debt to equity from description
                    desc = statement['description']
                    try:
                        debt_equity = float(desc.split('debt-to-equity ratio to ')[1].split('%')[0])
                        metrics['debtToEquity'] = debt_equity
                    except:
                        pass
                        
        return metrics
