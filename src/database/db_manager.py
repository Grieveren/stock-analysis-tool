"""Database management module."""
from sqlalchemy import create_engine, Column, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from typing import Dict, Any

Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'
    
    ticker = Column(String, primary_key=True)
    yahoo_data = Column(JSON)
    simply_wall_st_data = Column(JSON)
    analysis_results = Column(JSON)
    last_updated = Column(DateTime, default=datetime.utcnow)

class DatabaseManager:
    def __init__(self, db_url: str = 'sqlite:///financial_analyzer.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
    def save_stock_data(self, ticker: str, yahoo_data: Dict[str, Any], 
                       simply_wall_st_data: Dict[str, Any], 
                       analysis_results: Dict[str, Any] = None) -> None:
        """Save stock data to database.
        
        Args:
            ticker: Stock ticker symbol
            yahoo_data: Data from Yahoo Finance
            simply_wall_st_data: Data from Simply Wall Street
            analysis_results: Results from the analysis
        """
        session = self.Session()
        try:
            stock_data = StockData(
                ticker=ticker,
                yahoo_data=yahoo_data,
                simply_wall_st_data=simply_wall_st_data,
                analysis_results=analysis_results
            )
            session.merge(stock_data)
            session.commit()
        finally:
            session.close()
            
    def get_stock_data(self, ticker: str) -> Dict[str, Any]:
        """Retrieve stock data from database.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict containing combined stock data
        """
        session = self.Session()
        try:
            stock_data = session.query(StockData).filter_by(ticker=ticker).first()
            if stock_data:
                return {
                    'yahoo_data': stock_data.yahoo_data,
                    'simply_wall_st_data': stock_data.simply_wall_st_data,
                    'analysis_results': stock_data.analysis_results,
                    'last_updated': stock_data.last_updated
                }
            return None
        finally:
            session.close()
            
    def save_analysis_results(self, ticker: str, analysis_results: Dict[str, Any]) -> None:
        """Save analysis results to database.
        
        Args:
            ticker: Stock ticker symbol
            analysis_results: Results from the analysis
        """
        session = self.Session()
        try:
            stock_data = session.query(StockData).filter_by(ticker=ticker).first()
            if stock_data:
                stock_data.analysis_results = analysis_results
                stock_data.last_updated = datetime.utcnow()
                session.commit()
        finally:
            session.close()
            
    def get_analysis_results(self, ticker: str) -> Dict[str, Any]:
        """Retrieve analysis results from database.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict containing analysis results
        """
        session = self.Session()
        try:
            stock_data = session.query(StockData).filter_by(ticker=ticker).first()
            if stock_data and stock_data.analysis_results:
                return {
                    'analysis_results': stock_data.analysis_results,
                    'last_updated': stock_data.last_updated
                }
            return None
        finally:
            session.close()
