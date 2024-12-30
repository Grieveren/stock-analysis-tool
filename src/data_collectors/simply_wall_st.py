"""Simply Wall Street data collector module."""
import os
import requests
import json
import sys
from typing import Dict, Any

class SimplyWallStCollector:
    def __init__(self):
        self.api_key = os.getenv('SWS_API_TOKEN')
        self.base_url = 'https://api.simplywall.st/graphql'
        
    def get_company_data(self, ticker: str) -> Dict[str, Any]:
        """Fetch company data from Simply Wall Street.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict containing company financial and fundamental data
        """
        if not self.api_key:
            print("Warning: SWS_API_TOKEN not found in environment variables", file=sys.stderr)
            return {}
            
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        # First, search for the company to get its ID
        search_query = {
            "query": """
                query searchCompanies($query: String!) {
                    searchCompanies(query: $query) {
                        id
                        name
                        exchangeSymbol
                        tickerSymbol
                    }
                }
            """,
            "variables": {
                "query": ticker
            }
        }
        
        try:
            print(f"\nSearching for company with ticker: {ticker}", file=sys.stderr)
            print("Request Headers:", json.dumps(headers, indent=2), file=sys.stderr)
            print("Search Query:", json.dumps(search_query, indent=2), file=sys.stderr)
            
            # Get company ID
            response = requests.post(self.base_url, json=search_query, headers=headers)
            
            print(f"Search Response Status: {response.status_code}", file=sys.stderr)
            print("Search Response Headers:", json.dumps(dict(response.headers), indent=2), file=sys.stderr)
            
            if response.status_code != 200:
                print(f"Error Response: {response.text}", file=sys.stderr)
                return {}
                
            search_data = response.json()
            print("Search Response Data:", json.dumps(search_data, indent=2), file=sys.stderr)
            
            # Find exact match for ticker
            companies = search_data.get('data', {}).get('searchCompanies', [])
            company_id = None
            for company in companies:
                if company.get('tickerSymbol') == ticker:
                    company_id = company.get('id')
                    break
                    
            if not company_id:
                print(f"Could not find company ID for ticker {ticker}", file=sys.stderr)
                return {}
                
            print(f"Found company ID: {company_id}", file=sys.stderr)
            
            # Get detailed company data
            company_query = {
                "query": """
                    query Company($id: ID!) {
                        company(id: $id) {
                            id
                            name
                            marketCapUSD
                            tickerSymbol
                            exchangeSymbol
                            market {
                                name
                            }
                            statements {
                                name
                                title
                                area
                                type
                                value
                                outcome
                                description
                            }
                            closingPrices
                        }
                    }
                """,
                "variables": {
                    "id": company_id
                }
            }
            
            print("\nFetching company details", file=sys.stderr)
            print("Company Query:", json.dumps(company_query, indent=2), file=sys.stderr)
            
            # Get detailed data
            response = requests.post(self.base_url, json=company_query, headers=headers)
            
            print(f"Company Details Response Status: {response.status_code}", file=sys.stderr)
            print("Company Details Response Headers:", json.dumps(dict(response.headers), indent=2), file=sys.stderr)
            
            if response.status_code != 200:
                print(f"Error Response: {response.text}", file=sys.stderr)
                return {}
                
            company_data = response.json()
            print("Company Details Response Data:", json.dumps(company_data, indent=2), file=sys.stderr)
            
            # Extract and format the data
            data = company_data.get('data', {}).get('company', {})
            if not data:
                return {}
                
            # Format the response
            formatted_data = {
                'name': data.get('name'),
                'marketCap': data.get('marketCapUSD'),
                'tickerSymbol': data.get('tickerSymbol'),
                'exchangeSymbol': data.get('exchangeSymbol'),
                'market': data.get('market', {}).get('name'),
                'statements': data.get('statements', []),
                'closingPrices': data.get('closingPrices', {})
            }
            
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            if hasattr(response, 'status_code') and response.status_code == 403:
                print(f"Error: Invalid or expired Simply Wall Street API token", file=sys.stderr)
                print(f"Response: {response.text}", file=sys.stderr)
            else:
                print(f"Error fetching data for {ticker}: {str(e)}", file=sys.stderr)
            return {}
