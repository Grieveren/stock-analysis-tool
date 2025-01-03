"""Yahoo Finance data collector module."""
import yfinance as yf
from typing import Dict, Any
import json

class YahooFinanceCollector:
    def get_stock_data(self, ticker: str) -> Dict[str, Any]:
        """Fetch stock data from Yahoo Finance.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict containing stock price and financial data
        """
        try:
            stock = yf.Ticker(ticker)
            
            # Convert DataFrames to dict and handle timestamps
            financials = stock.financials.to_dict() if stock.financials is not None else {}
            balance_sheet = stock.balance_sheet.to_dict() if stock.balance_sheet is not None else {}
            cash_flow = stock.cashflow.to_dict() if stock.cashflow is not None else {}
            
            # Get basic info
            info = {}
            try:
                info = stock.info
            except Exception as e:
                print(f"Error fetching info for {ticker}: {str(e)}")
            
            # Convert all timestamps in the dictionaries to strings
            financials = self._convert_timestamps(financials)
            balance_sheet = self._convert_timestamps(balance_sheet)
            cash_flow = self._convert_timestamps(cash_flow)
            
            return {
                'info': info,
                'financials': financials,
                'balance_sheet': balance_sheet,
                'cash_flow': cash_flow
            }
        except Exception as e:
            print(f"Error fetching data for {ticker}: {str(e)}")
            return {}
            
    def _convert_timestamps(self, data: Dict) -> Dict:
        """Convert all timestamps in a dictionary to strings.
        
        Args:
            data: Dictionary potentially containing timestamps
            
        Returns:
            Dictionary with timestamps converted to strings
        """
        converted = {}
        for key, value in data.items():
            if hasattr(key, 'strftime'):  # Check if key is a timestamp
                str_key = key.strftime('%Y-%m-%d')
            else:
                str_key = str(key)
                
            if isinstance(value, dict):
                converted[str_key] = self._convert_timestamps(value)
            else:
                converted[str_key] = value
        return converted
