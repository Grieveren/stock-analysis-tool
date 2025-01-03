"""OpenAI-powered stock analysis module."""
import os
import openai
from typing import Dict, Any

class OpenAIAnalyzer:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        
    def analyze_stock(self, processed_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze stock data using OpenAI.
        
        Args:
            processed_data: Preprocessed stock and portfolio data
            
        Returns:
            Dict containing analysis results and recommendations
        """
        # Prepare the prompt
        prompt = self._create_analysis_prompt(processed_data)
        
        try:
            # Get analysis from OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a financial analyst expert. Analyze the given stock data and provide a detailed recommendation."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            analysis = response.choices[0].message.content
            
            return {
                'recommendation': analysis,
                'metrics_comparison': self._compare_metrics(processed_data)
            }
        except Exception as e:
            print(f"Error during analysis: {str(e)}")
            return {'error': str(e)}
    
    def _create_analysis_prompt(self, data: Dict[str, Any]) -> str:
        """Create analysis prompt from processed data.
        
        Args:
            data: Processed stock and portfolio data
            
        Returns:
            String containing the analysis prompt
        """
        stock_metrics = data['stock_metrics']
        portfolio_avg = data['portfolio_averages']
        
        prompt = f"""Please analyze this stock based on the following data:

Stock Metrics:
{self._format_metrics(stock_metrics)}

Portfolio Averages:
{self._format_metrics(portfolio_avg)}

Please provide:
1. A comprehensive analysis of the stock's financial health
2. Comparison with portfolio averages
3. Clear buy/hold/sell recommendation
4. Key risks and opportunities
"""
        return prompt
    
    def _format_metrics(self, metrics: Dict[str, float]) -> str:
        """Format metrics for prompt.
        
        Args:
            metrics: Dictionary of financial metrics
            
        Returns:
            Formatted string of metrics
        """
        return '\n'.join([f"- {k}: {v}" for k, v in metrics.items()])
    
    def _compare_metrics(self, data: Dict[str, Any]) -> Dict[str, str]:
        """Compare stock metrics with portfolio averages.
        
        Args:
            data: Processed stock and portfolio data
            
        Returns:
            Dict containing metric comparisons
        """
        comparisons = {}
        stock = data['stock_metrics']
        portfolio = data['portfolio_averages']
        
        for metric in stock:
            if stock[metric] is not None and portfolio[metric] is not None:
                diff = ((stock[metric] - portfolio[metric]) / portfolio[metric]) * 100
                comparisons[metric] = f"{diff:+.2f}% vs portfolio average"
                
        return comparisons
