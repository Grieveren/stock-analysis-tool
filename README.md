# Financial Analyzer

A comprehensive stock analysis tool that evaluates stocks and provides investment recommendations based on quantitative data. The system integrates data from multiple sources and uses advanced analytics to provide data-driven investment insights.

## Features
- Multi-source data collection (Simply Wall Street, Yahoo Finance)
- Automated stock comparison with portfolio companies
- Portfolio import from German broker CSV files (with WKN mapping)
- Quantitative analysis using OpenAI
- Investment recommendations based on data-driven insights
- Caching system for efficient data retrieval
- Comprehensive error handling and logging

## Architecture

### Data Pipeline
1. **Data Collection Layer**
   - `SimplyWallStCollector`: Fetches company data via GraphQL API
     - Company information (name, market cap, ticker)
     - Market data and statements
     - Closing prices
   - `YahooFinanceCollector`: Retrieves financial metrics
     - Historical price data
     - Key financial ratios
     - Market statistics
   - `Portfolio Import`: Reads German broker CSV files
     - Supports German number format (comma decimal, dot thousands)
     - Maps WKN (German securities identification) to international tickers
     - Extracts portfolio positions and holdings

2. **Data Processing Layer**
   - `DataPreprocessor`: Transforms and combines data
     - Extracts key metrics from statements
     - Calculates financial ratios
     - Normalizes data for analysis

3. **Analysis Layer**
   - `OpenAIAnalyzer`: Processes financial data
     - Evaluates company performance
     - Compares with portfolio averages
     - Generates investment recommendations

4. **Storage Layer**
   - SQLite database for data persistence
   - Caches analysis results for efficiency
   - Tracks data freshness with timestamps

### Key Components

#### Data Pipeline Map
```
Portfolio Data (CSV)                Yahoo Finance                Simply Wall Street
└── Position Data                  └── Financial Data           └── Company Data
    ├── WKN                           ├── Price History            ├── Company Info
    ├── Holdings                      ├── Market Cap               │   ├── Name
    ├── Entry Price                   ├── P/E Ratio               │   ├── Market Cap
    ├── Current Price                 ├── EPS                     │   ├── Exchange
    └── Change %                      ├── Volume                  │   └── Market
                                     └── Dividends                ├── Financial Metrics
                                                                 │   ├── ROE
                                                                 │   ├── D/E Ratio
                                                                 │   ├── Current Ratio
                                                                 │   └── Dividend Yield
                                                                 └── Analysis
                                                                     ├── Price Target
                                                                     └── Statements

                                Data Processing
                                     │
                            ┌────────┴────────┐
                            │                 │
                     Data Combination    Metric Calculation
                            │                 │
                            │            ├── Portfolio Averages
                            │            ├── Performance Metrics
                            │            └── Risk Metrics
                            │
                            └─────────┬─────────┘
                                     │
                              OpenAI Analysis
                                     │
                            ┌────────┴────────┐
                            │                 │
                    Financial Health    Investment Advice
                            │                 │
                     ├── Metrics        ├── Recommendation
                     ├── Comparisons    ├── Risk Assessment
                     └── Trends         └── Action Items

                              Final Output
                                   │
                        ┌─────────┴─────────┐
                        │                   │
                    Analysis           Database Cache
                        │                   │
                ├── Recommendation      └── JSON Storage
                ├── Metrics                 └── Timestamp
                └── Comparisons
```

#### Database Schema
```sql
CREATE TABLE stock_data (
    ticker TEXT PRIMARY KEY,
    yahoo_data JSON,
    simply_wall_st_data JSON,
    analysis_results JSON,
    last_updated DATETIME
);
```

#### API Integration
- Simply Wall Street: GraphQL-based API
  - Authentication via bearer token
  - Rate-limited requests
  - Error handling with retries

- Yahoo Finance: REST API
  - Direct data access
  - Historical data retrieval
  - Market statistics

## Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

## Configuration
Required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `SIMPLY_WALL_ST_API_KEY`: Your Simply Wall Street API key

## Usage

### Portfolio Analysis
1. Place your portfolio CSV file as `portfolio.csv` in the root directory
2. Run the analyzer:
```bash
python src/main.py
```

The program supports German broker CSV files with the following features:
- German number format (comma as decimal, dot as thousands separator)
- WKN to international ticker mapping
- Automatic handling of broker-specific CSV structure

Example portfolio.csv format:
```csv
Position;Bezeichnung;WKN;ISIN;Notierung;...
1;ALLIANZ SE NA O.N.;840400;DE0008404005;STK;...
2;ASML HOLDING    EO -,09;A1J4U4;NL0010273215;STK;...
```

### Custom Analysis
Analyze specific stocks against your portfolio:
```python
from src.main import FinancialAnalyzer

analyzer = FinancialAnalyzer()
# Will use portfolio.csv if available, otherwise falls back to default tickers
results = analyzer.analyze_stock("NVDA", ["AAPL", "MSFT", "GOOGL"])
print(results)
```

### Database Queries
View cached analysis results:
```sql
-- Get latest analysis for a stock
SELECT ticker, last_updated, json_extract(analysis_results, '$.recommendation')
FROM stock_data
WHERE ticker = 'NVDA';
```

## Data Flow
1. User requests stock analysis
2. System checks cache for recent analysis
3. If needed, fetches fresh data from APIs
4. Preprocesses and combines data
5. Generates analysis using OpenAI
6. Caches results in database
7. Returns formatted recommendations

## Error Handling
- API request retries with exponential backoff
- Comprehensive error logging
- Graceful degradation with partial data
- Data validation at each pipeline stage

## Limitations
- API rate limits may affect analysis speed
- Some financial data may be delayed
- Analysis quality depends on data availability

## Future Improvements
1. Rate limiting implementation
2. Unit test coverage
3. Additional financial metrics
4. Data expiration policies
5. Historical analysis features

## Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
This project is licensed under the MIT License.
