# YFinance Documentation

*A comprehensive guide to the YFinance library, organized for easy reference.*

## Table of Contents

    - [API Reference#](#api-reference)
    - [Advanced#](#advanced)
    - [Analysis & Holdings#](#analysis-holdings)
    - [Caching#](#caching)
    - [Contribution to the documentation#](#contribution-to-the-documentation)
    - [Contributiong to yfinance#](#contributiong-to-yfinance)
    - [Development#](#development)
    - [EquityQuery#](#equityquery)
    - [Financials#](#financials)
    - [Functions and Utilities#](#functions-and-utilities)
    - [FundsData class#](#fundsdata-class)
    - [FundsData#](#fundsdata)
    - [Industry#](#industry)
    - [Logging#](#logging)
    - [Multi-Level Column Index#](#multi-level-column-index)
    - [PriceHistory class#](#pricehistory-class)
    - [Proxy Server#](#proxy-server)
    - [Reporting a Bug#](#reporting-a-bug)
    - [Screener#](#screener)
    - [Search#](#search)
    - [Sector and Industry#](#sector-and-industry)
    - [Sector#](#sector)
    - [Stock#](#stock)
    - [Ticker and Tickers#](#ticker-and-tickers)
    - [Ticker#](#ticker)
    - [Tickers#](#tickers)
  - [yfinance documentation#](#yfinance-documentation)
    - [yfinance.Ticker.actions#](#yfinancetickeractions)
    - [yfinance.Ticker.analyst_price_targets#](#yfinancetickeranalyst_price_targets)
    - [yfinance.Ticker.balance_sheet#](#yfinancetickerbalance_sheet)
    - [yfinance.Ticker.calendar#](#yfinancetickercalendar)
    - [yfinance.Ticker.capital_gains#](#yfinancetickercapital_gains)
    - [yfinance.Ticker.cashflow#](#yfinancetickercashflow)
    - [yfinance.Ticker.dividends#](#yfinancetickerdividends)
    - [yfinance.Ticker.earnings#](#yfinancetickerearnings)
    - [yfinance.Ticker.earnings_dates#](#yfinancetickerearnings_dates)
    - [yfinance.Ticker.earnings_estimate#](#yfinancetickerearnings_estimate)
    - [yfinance.Ticker.earnings_history#](#yfinancetickerearnings_history)
    - [yfinance.Ticker.eps_revisions#](#yfinancetickereps_revisions)
    - [yfinance.Ticker.eps_trend#](#yfinancetickereps_trend)
    - [yfinance.Ticker.fast_info#](#yfinancetickerfast_info)
    - [yfinance.Ticker.funds_data#](#yfinancetickerfunds_data)
    - [yfinance.Ticker.get_actions#](#yfinancetickerget_actions)
    - [yfinance.Ticker.get_analyst_price_targets#](#yfinancetickerget_analyst_price_targets)
    - [yfinance.Ticker.get_balance_sheet#](#yfinancetickerget_balance_sheet)
    - [yfinance.Ticker.get_capital_gains#](#yfinancetickerget_capital_gains)
    - [yfinance.Ticker.get_cashflow#](#yfinancetickerget_cashflow)
    - [yfinance.Ticker.get_dividends#](#yfinancetickerget_dividends)
    - [yfinance.Ticker.get_earnings#](#yfinancetickerget_earnings)
    - [yfinance.Ticker.get_earnings_dates#](#yfinancetickerget_earnings_dates)
    - [yfinance.Ticker.get_earnings_estimate#](#yfinancetickerget_earnings_estimate)
    - [yfinance.Ticker.get_earnings_history#](#yfinancetickerget_earnings_history)
    - [yfinance.Ticker.get_eps_revisions#](#yfinancetickerget_eps_revisions)
    - [yfinance.Ticker.get_eps_trend#](#yfinancetickerget_eps_trend)
    - [yfinance.Ticker.get_fast_info#](#yfinancetickerget_fast_info)
    - [yfinance.Ticker.get_funds_data#](#yfinancetickerget_funds_data)
    - [yfinance.Ticker.get_growth_estimates#](#yfinancetickerget_growth_estimates)
    - [yfinance.Ticker.get_history_metadata#](#yfinancetickerget_history_metadata)
    - [yfinance.Ticker.get_income_stmt#](#yfinancetickerget_income_stmt)
    - [yfinance.Ticker.get_info#](#yfinancetickerget_info)
    - [yfinance.Ticker.get_insider_purchases#](#yfinancetickerget_insider_purchases)
    - [yfinance.Ticker.get_insider_roster_holders#](#yfinancetickerget_insider_roster_holders)
    - [yfinance.Ticker.get_insider_transactions#](#yfinancetickerget_insider_transactions)
    - [yfinance.Ticker.get_institutional_holders#](#yfinancetickerget_institutional_holders)
    - [yfinance.Ticker.get_isin#](#yfinancetickerget_isin)
    - [yfinance.Ticker.get_major_holders#](#yfinancetickerget_major_holders)
    - [yfinance.Ticker.get_mutualfund_holders#](#yfinancetickerget_mutualfund_holders)
    - [yfinance.Ticker.get_news#](#yfinancetickerget_news)
    - [yfinance.Ticker.get_recommendations#](#yfinancetickerget_recommendations)
    - [yfinance.Ticker.get_recommendations_summary#](#yfinancetickerget_recommendations_summary)
    - [yfinance.Ticker.get_revenue_estimate#](#yfinancetickerget_revenue_estimate)
    - [yfinance.Ticker.get_sec_filings#](#yfinancetickerget_sec_filings)
    - [yfinance.Ticker.get_shares_full#](#yfinancetickerget_shares_full)
    - [yfinance.Ticker.get_splits#](#yfinancetickerget_splits)
    - [yfinance.Ticker.get_sustainability#](#yfinancetickerget_sustainability)
    - [yfinance.Ticker.get_upgrades_downgrades#](#yfinancetickerget_upgrades_downgrades)
    - [yfinance.Ticker.growth_estimates#](#yfinancetickergrowth_estimates)
    - [yfinance.Ticker.history#](#yfinancetickerhistory)
    - [yfinance.Ticker.income_stmt#](#yfinancetickerincome_stmt)
    - [yfinance.Ticker.info#](#yfinancetickerinfo)
    - [yfinance.Ticker.insider_purchases#](#yfinancetickerinsider_purchases)
    - [yfinance.Ticker.insider_roster_holders#](#yfinancetickerinsider_roster_holders)
    - [yfinance.Ticker.insider_transactions#](#yfinancetickerinsider_transactions)
    - [yfinance.Ticker.institutional_holders#](#yfinancetickerinstitutional_holders)
    - [yfinance.Ticker.isin#](#yfinancetickerisin)
    - [yfinance.Ticker.major_holders#](#yfinancetickermajor_holders)
    - [yfinance.Ticker.mutualfund_holders#](#yfinancetickermutualfund_holders)
    - [yfinance.Ticker.news#](#yfinancetickernews)
    - [yfinance.Ticker.recommendations#](#yfinancetickerrecommendations)
    - [yfinance.Ticker.recommendations_summary#](#yfinancetickerrecommendations_summary)
    - [yfinance.Ticker.revenue_estimate#](#yfinancetickerrevenue_estimate)
    - [yfinance.Ticker.sec_filings#](#yfinancetickersec_filings)
    - [yfinance.Ticker.splits#](#yfinancetickersplits)
    - [yfinance.Ticker.sustainability#](#yfinancetickersustainability)
    - [yfinance.Ticker.upgrades_downgrades#](#yfinancetickerupgrades_downgrades)
    - [yfinance.download#](#yfinancedownload)
    - [yfinance.enable_debug_mode#](#yfinanceenable_debug_mode)
    - [yfinance.set_tz_cache_location#](#yfinanceset_tz_cache_location)

---


<h4 id="api-reference">API Reference#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * API Reference 
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * API Reference 
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * API Reference

# API Reference#

## Overview#

The yfinance package provides easy access to Yahoo! Finance’s API to retrieve market data. It includes classes and functions for downloading historical market data, accessing ticker information, managing cache, and more.

### Public API#

The following are the publicly available classes, and functions exposed by the yfinance package:

  * [`Ticker`](api/yfinance.Ticker.html#yfinance.Ticker "yfinance.Ticker"): Class for accessing single ticker data.

  * [`Tickers`](api/yfinance.Tickers.html#yfinance.Tickers "yfinance.Tickers"): Class for handling multiple tickers.

  * [`Search`](api/yfinance.Search.html#yfinance.Search "yfinance.Search"): Class for accessing search results.

  * [`Sector`](api/yfinance.Sector.html#yfinance.Sector "yfinance.Sector"): Domain class for accessing sector information.

  * [`Industry`](api/yfinance.Industry.html#yfinance.Industry "yfinance.Industry"): Domain class for accessing industry information.

  * [`download`](api/yfinance.download.html#yfinance.download "yfinance.download"): Function to download market data for multiple tickers.

  * [`EquityQuery`](api/yfinance.EquityQuery.html#yfinance.EquityQuery "yfinance.EquityQuery"): Class to build equity market query.

  * [`Screener`](api/yfinance.Screener.html#yfinance.Screener "yfinance.Screener"): Class to screen the market using defined query.

  * [`enable_debug_mode`](api/yfinance.enable_debug_mode.html#yfinance.enable_debug_mode "yfinance.enable_debug_mode"): Function to enable debug mode for logging.

  * [`set_tz_cache_location`](api/yfinance.set_tz_cache_location.html#yfinance.set_tz_cache_location "yfinance.set_tz_cache_location"): Function to set the timezone cache location.

[ __ previous Multi-Level Column Index ](../advanced/multi_level_columns.html "previous page") [ next Ticker and Tickers __](yfinance.ticker_tickers.html "next page")

__On this page

  * Overview
    * Public API

[ __Show Source](../_sources/reference/index.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="advanced">Advanced#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * Advanced 
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * Advanced 
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Logging](logging.html)
  * [Proxy Server](proxy.html)
  * [Caching](caching.html)
  * [Multi-Level Column Index](multi_level_columns.html)

  * [ __](../index.html)
  * Advanced

# Advanced#

  * [Logging](logging.html)
  * [Proxy Server](proxy.html)
  * [Caching](caching.html)
    * [Smarter Scraping](caching.html#smarter-scraping)
    * [Persistent Cache](caching.html#persistent-cache)
  * [Multi-Level Column Index](multi_level_columns.html)

[ __ previous yfinance documentation ](../index.html "previous page") [ next Logging __](logging.html "next page")

[ __Show Source](../_sources/advanced/index.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="analysis-holdings">Analysis & Holdings#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * Analysis & Holdings __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * [API Reference](index.html)
  * Analysis...

# Analysis & Holdings#

## Analysis#

[`get_recommendations`](api/yfinance.Ticker.get_recommendations.html#yfinance.Ticker.get_recommendations "yfinance.Ticker.get_recommendations")([proxy, as_dict]) | Returns a DataFrame with the recommendations Columns: period strongBuy buy hold sell strongSell  
---|---  
[`recommendations`](api/yfinance.Ticker.recommendations.html#yfinance.Ticker.recommendations "yfinance.Ticker.recommendations") |   
[`get_recommendations_summary`](api/yfinance.Ticker.get_recommendations_summary.html#yfinance.Ticker.get_recommendations_summary "yfinance.Ticker.get_recommendations_summary")([proxy, as_dict]) |   
[`recommendations_summary`](api/yfinance.Ticker.recommendations_summary.html#yfinance.Ticker.recommendations_summary "yfinance.Ticker.recommendations_summary") |   
[`get_upgrades_downgrades`](api/yfinance.Ticker.get_upgrades_downgrades.html#yfinance.Ticker.get_upgrades_downgrades "yfinance.Ticker.get_upgrades_downgrades")([proxy, as_dict]) | Returns a DataFrame with the recommendations changes (upgrades/downgrades) Index: date of grade Columns: firm toGrade fromGrade action  
[`upgrades_downgrades`](api/yfinance.Ticker.upgrades_downgrades.html#yfinance.Ticker.upgrades_downgrades "yfinance.Ticker.upgrades_downgrades") |   
[`get_sustainability`](api/yfinance.Ticker.get_sustainability.html#yfinance.Ticker.get_sustainability "yfinance.Ticker.get_sustainability")([proxy, as_dict]) |   
[`sustainability`](api/yfinance.Ticker.sustainability.html#yfinance.Ticker.sustainability "yfinance.Ticker.sustainability") |   
[`get_analyst_price_targets`](api/yfinance.Ticker.get_analyst_price_targets.html#yfinance.Ticker.get_analyst_price_targets "yfinance.Ticker.get_analyst_price_targets")([proxy]) | Keys: current low high mean median  
[`analyst_price_targets`](api/yfinance.Ticker.analyst_price_targets.html#yfinance.Ticker.analyst_price_targets "yfinance.Ticker.analyst_price_targets") |   
[`get_earnings_estimate`](api/yfinance.Ticker.get_earnings_estimate.html#yfinance.Ticker.get_earnings_estimate "yfinance.Ticker.get_earnings_estimate")([proxy, as_dict]) | Index: 0q +1q 0y +1y Columns: numberOfAnalysts avg low high yearAgoEps growth  
[`earnings_estimate`](api/yfinance.Ticker.earnings_estimate.html#yfinance.Ticker.earnings_estimate "yfinance.Ticker.earnings_estimate") |   
[`get_revenue_estimate`](api/yfinance.Ticker.get_revenue_estimate.html#yfinance.Ticker.get_revenue_estimate "yfinance.Ticker.get_revenue_estimate")([proxy, as_dict]) | Index: 0q +1q 0y +1y Columns: numberOfAnalysts avg low high yearAgoRevenue growth  
[`revenue_estimate`](api/yfinance.Ticker.revenue_estimate.html#yfinance.Ticker.revenue_estimate "yfinance.Ticker.revenue_estimate") |   
[`get_earnings_history`](api/yfinance.Ticker.get_earnings_history.html#yfinance.Ticker.get_earnings_history "yfinance.Ticker.get_earnings_history")([proxy, as_dict]) | Index: pd.DatetimeIndex Columns: epsEstimate epsActual epsDifference surprisePercent  
[`earnings_history`](api/yfinance.Ticker.earnings_history.html#yfinance.Ticker.earnings_history "yfinance.Ticker.earnings_history") |   
[`get_eps_trend`](api/yfinance.Ticker.get_eps_trend.html#yfinance.Ticker.get_eps_trend "yfinance.Ticker.get_eps_trend")([proxy, as_dict]) | Index: 0q +1q 0y +1y Columns: current 7daysAgo 30daysAgo 60daysAgo 90daysAgo  
[`eps_trend`](api/yfinance.Ticker.eps_trend.html#yfinance.Ticker.eps_trend "yfinance.Ticker.eps_trend") |   
[`get_eps_revisions`](api/yfinance.Ticker.get_eps_revisions.html#yfinance.Ticker.get_eps_revisions "yfinance.Ticker.get_eps_revisions")([proxy, as_dict]) | Index: 0q +1q 0y +1y Columns: upLast7days upLast30days downLast7days downLast30days  
[`eps_revisions`](api/yfinance.Ticker.eps_revisions.html#yfinance.Ticker.eps_revisions "yfinance.Ticker.eps_revisions") |   
[`get_growth_estimates`](api/yfinance.Ticker.get_growth_estimates.html#yfinance.Ticker.get_growth_estimates "yfinance.Ticker.get_growth_estimates")([proxy, as_dict]) | Index: 0q +1q 0y +1y +5y -5y Columns: stock industry sector index  
[`growth_estimates`](api/yfinance.Ticker.growth_estimates.html#yfinance.Ticker.growth_estimates "yfinance.Ticker.growth_estimates") |   
  
## Holdings#

[`get_funds_data`](api/yfinance.Ticker.get_funds_data.html#yfinance.Ticker.get_funds_data "yfinance.Ticker.get_funds_data")([proxy]) |   
---|---  
[`funds_data`](api/yfinance.Ticker.funds_data.html#yfinance.Ticker.funds_data "yfinance.Ticker.funds_data") |   
  
See also

[`yfinance.scrapers.funds.FundsData()`](api/yfinance.scrapers.funds.FundsData.html#yfinance.scrapers.funds.FundsData "yfinance.scrapers.funds.FundsData")

[`get_insider_purchases`](api/yfinance.Ticker.get_insider_purchases.html#yfinance.Ticker.get_insider_purchases "yfinance.Ticker.get_insider_purchases")([proxy, as_dict]) |   
---|---  
[`insider_purchases`](api/yfinance.Ticker.insider_purchases.html#yfinance.Ticker.insider_purchases "yfinance.Ticker.insider_purchases") |   
[`get_insider_transactions`](api/yfinance.Ticker.get_insider_transactions.html#yfinance.Ticker.get_insider_transactions "yfinance.Ticker.get_insider_transactions")([proxy, as_dict]) |   
[`insider_transactions`](api/yfinance.Ticker.insider_transactions.html#yfinance.Ticker.insider_transactions "yfinance.Ticker.insider_transactions") |   
[`get_insider_roster_holders`](api/yfinance.Ticker.get_insider_roster_holders.html#yfinance.Ticker.get_insider_roster_holders "yfinance.Ticker.get_insider_roster_holders")([proxy, as_dict]) |   
[`insider_roster_holders`](api/yfinance.Ticker.insider_roster_holders.html#yfinance.Ticker.insider_roster_holders "yfinance.Ticker.insider_roster_holders") |   
[`get_major_holders`](api/yfinance.Ticker.get_major_holders.html#yfinance.Ticker.get_major_holders "yfinance.Ticker.get_major_holders")([proxy, as_dict]) |   
[`major_holders`](api/yfinance.Ticker.major_holders.html#yfinance.Ticker.major_holders "yfinance.Ticker.major_holders") |   
[`get_institutional_holders`](api/yfinance.Ticker.get_institutional_holders.html#yfinance.Ticker.get_institutional_holders "yfinance.Ticker.get_institutional_holders")([proxy, as_dict]) |   
[`institutional_holders`](api/yfinance.Ticker.institutional_holders.html#yfinance.Ticker.institutional_holders "yfinance.Ticker.institutional_holders") |   
[`get_mutualfund_holders`](api/yfinance.Ticker.get_mutualfund_holders.html#yfinance.Ticker.get_mutualfund_holders "yfinance.Ticker.get_mutualfund_holders")([proxy, as_dict]) |   
[`mutualfund_holders`](api/yfinance.Ticker.mutualfund_holders.html#yfinance.Ticker.mutualfund_holders "yfinance.Ticker.mutualfund_holders") |   
  
[ __ previous yfinance.Ticker.sec_filings ](api/yfinance.Ticker.sec_filings.html "previous page") [ next yfinance.Ticker.get_recommendations __](api/yfinance.Ticker.get_recommendations.html "next page")

__On this page

  * Analysis
  * Holdings

[ __Show Source](../_sources/reference/yfinance.analysis.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="caching">Caching#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Logging](logging.html)
  * [Proxy Server](proxy.html)
  * Caching
  * [Multi-Level Column Index](multi_level_columns.html)

  * [ __](../index.html)
  * [Advanced](index.html)
  * Caching

# Caching#

## Smarter Scraping#

Install the nospam package to cache API calls and reduce spam to Yahoo:

    pip install yfinance[nospam]

To use a custom requests session, pass a session= argument to the Ticker constructor. This allows for caching calls to the API as well as a custom way to modify requests via the User-agent header.

    import requests_cache
    session = requests_cache.CachedSession('yfinance.cache')
    session.headers['User-agent'] = 'my-program/1.0'
    ticker = yf.Ticker('MSFT', session=session)
    
    # The scraped response will be stored in the cache
    ticker.actions

Combine requests_cache with rate-limiting to avoid triggering Yahoo’s rate-limiter/blocker that can corrupt data.

    from requests import Session
    from requests_cache import CacheMixin, SQLiteCache
    from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
    from pyrate_limiter import Duration, RequestRate, Limiter
    class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
       pass
    
    session = CachedLimiterSession(
       limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
       bucket_class=MemoryQueueBucket,
       backend=SQLiteCache("yfinance.cache"),
    )

## Persistent Cache#

To reduce Yahoo, yfinance store some data locally: timezones to localize dates, and cookie. Cache location is:

  * Windows = C:/Users/<USER>/AppData/Local/py-yfinance

  * Linux = /home/<USER>/.cache/py-yfinance

  * MacOS = /Users/<USER>/Library/Caches/py-yfinance

You can direct cache to use a different location with [`set_tz_cache_location`](../reference/api/yfinance.set_tz_cache_location.html#yfinance.set_tz_cache_location "yfinance.set_tz_cache_location"):

    import yfinance as yf
    yf.set_tz_cache_location("custom/cache/location")

[ __ previous Proxy Server ](proxy.html "previous page") [ next Multi-Level Column Index __](multi_level_columns.html "next page")

__On this page

  * Smarter Scraping
  * Persistent Cache

[ __Show Source](../_sources/advanced/caching.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="contribution-to-the-documentation">Contribution to the documentation#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Contributiong to yfinance](contributing.html)
  * Contribution to the documentation
  * [Reporting a Bug](reporting_bug.html)

  * [ __](../index.html)
  * [Development](index.html)
  * Contribution...

# Contribution to the documentation#

Documentation:

  * About documentation

  * Building documentation locally

  * Building documentation on main

## About documentation#

  * yfinance documentation is written in reStructuredText (rst) and built using Sphinx.

  * The documentation file is in doc/source/...

  * Most of the notes under API References read from class and methods docstrings. These documentations, found in doc/source/reference/api is autogenerated by Sphinx and not included in git.

## Building documentation locally#

To build the documentation locally, follow these steps:

  1. **Install Required Dependencies** :

     * Make sure Sphinx and any other dependencies are installed. If a requirements.txt file is available, you can install dependencies by running:
    
        pip install -r requirements.txt

  2. **Build with Sphinx** :

     * After dependencies are installed, use the sphinx-build command to generate HTML documentation.

     * Go to doc/ directory Run:
    
        make clean && make html

  3. **View Documentation Locally** :

     * Open doc/build/html/index.html in the browser to view the generated documentation.

## Building documentation on main#

The documentation updates are built on merge to main branch. This is done via GitHub Actions workflow based on /yfinance/.github/workflows/deploy_doc.yml.

  1. Reivew the changes locally and push to dev.

  2. When dev gets merged to main, GitHub Actions workflow is automated to build documentation.

[ __ previous Contributiong to yfinance ](contributing.html "previous page") [ next Reporting a Bug __](reporting_bug.html "next page")

__On this page

  * About documentation
  * Building documentation locally
  * Building documentation on main

[ __Show Source](../_sources/development/documentation.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="contributiong-to-yfinance">Contributiong to yfinance#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * Contributiong to yfinance
  * [Contribution to the documentation](documentation.html)
  * [Reporting a Bug](reporting_bug.html)

  * [ __](../index.html)
  * [Development](index.html)
  * Contribution...

# Contributiong to yfinance#

yfinance relies on the community to investigate bugs and contribute code. Here’s how you can help:

## Contributing#

  1. Fork the repository on GitHub.

  2. Clone your forked repository:
    
        git clone https://github.com/your-username/yfinance.git

  3. Create a new branch for your feature or bug fix:
    
        git checkout -b feature-branch-name

  4. Make your changes, commit them, and push your branch to GitHub. To keep the commit history and [network graph](https://github.com/ranaroussi/yfinance/network) compact:

Use short summaries for commits
    
        git commit -m "short summary" -m "full commit message"

**Squash** tiny or negligible commits with meaningful ones.
    
        git rebase -i HEAD~2
    git push --force-with-lease origin <branch-name>

  5. Open a pull request on the yfinance GitHub page.

For more information, see the [Developer Guide](https://github.com/ranaroussi/yfinance/discussions/1084).

## Branches#

To support rapid development without breaking stable versions, this project uses a two-layer branch model:

![Branching Model](../_images/branches.png)

[Inspiration](https://miro.medium.com/max/700/1*2YagIpX6LuauC3ASpwHekg.png)

  * **dev** : New features and some bug fixes are merged here. This branch allows collective testing, conflict resolution, and further stabilization before merging into the stable branch.

  * **main** : Stable branch where PIP releases are created.

By default, branches target **main** , but most contributions should target **dev**.

**Exceptions** : Direct merges to **main** are allowed if:

  * yfinance is massively broken

  * Part of yfinance is broken, and the fix is simple and isolated

## Unit Tests#

Tests are written using Python’s unittest module. Here are some ways to run tests:

  * **Run all price tests** :
    
        python -m unittest tests.test_prices

  * **Run a subset of price tests** :
    
        python -m unittest tests.test_prices.TestPriceRepair

  * **Run a specific test** :
    
        python -m unittest tests.test_prices.TestPriceRepair.test_ticker_missing

  * **Run all tests** :
    
        python -m unittest discover -s tests

## Rebasing#

If asked to move your branch from **main** to **dev** :

  1. Ensure all relevant branches are pulled.

  2. Run:
    
        git checkout <your-branch>
    git rebase --onto dev main <branch-name>
    git push --force-with-lease origin <branch-name>

## Running the GitHub Version of yfinance#

To download and run a GitHub version of yfinance, refer to [GitHub discussion](https://github.com/ranaroussi/yfinance/discussions/1080)

[ __ previous Development ](index.html "previous page") [ next Contribution to the documentation __](documentation.html "next page")

__On this page

  * Contributing
  * Branches
  * Unit Tests
  * Rebasing
  * Running the GitHub Version of yfinance

[ __Show Source](../_sources/development/contributing.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="development">Development#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * Development 

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * Development 

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Contributiong to yfinance](contributing.html)
  * [Contribution to the documentation](documentation.html)
  * [Reporting a Bug](reporting_bug.html)

  * [ __](../index.html)
  * Development

# Development#

  * [Contributiong to yfinance](contributing.html)
  * [Contribution to the documentation](documentation.html)
  * [Reporting a Bug](reporting_bug.html)

[ __ previous PriceHistory class ](../reference/yfinance.price_history.html "previous page") [ next Contributiong to yfinance __](contributing.html "next page")

[ __Show Source](../_sources/development/index.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="equityquery">EquityQuery#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * EquityQuery
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Functions and Utilities](../yfinance.functions.html)
  * EquityQuery

# EquityQuery#

_class _yfinance.EquityQuery(_operator : str_, _operand : Real | str | List[EquityQuery]_)#

The EquityQuery class constructs filters for stocks based on specific criteria such as region, sector, exchange, and peer group.

The queries support operators: GT (greater than), LT (less than), BTWN (between), EQ (equals), and logical operators AND and OR for combining multiple conditions.

Example

Screen for stocks where the end-of-day price is greater than 3.

    gt = yf.EquityQuery('gt', ['eodprice', 3])

Screen for stocks where the average daily volume over the last 3 months is less than a very large number.

    lt = yf.EquityQuery('lt', ['avgdailyvol3m', 99999999999])

Screen for stocks where the intraday market cap is between 0 and 100 million.

    btwn = yf.EquityQuery('btwn', ['intradaymarketcap', 0, 100000000])

Screen for stocks in the Technology sector.

    eq = yf.EquityQuery('eq', ['sector', 'Technology'])

Combine queries using AND/OR.

    qt = yf.EquityQuery('and', [gt, lt])
    qf = yf.EquityQuery('or', [qt, btwn, eq])

See also

`EquityQuery.valid_operand_fields`

supported operand values for query

`EquityQuery.valid_eq_operand_map`

supported EQ query operand parameters

Attributes

valid_eq_operand_map

Valid Operand Map for Operator “EQ”

Permitted Keys/Values# Key | Values  
---|---  
region | 

  * ar
  * at
  * au
  * be
  * br
  * ca
  * ch
  * cl
  * cn
  * cz
  * de
  * dk
  * ee
  * eg
  * es
  * fi
  * fr
  * gb
  * gr
  * hk
  * hu
  * id
  * ie
  * il
  * in
  * is
  * it
  * jp
  * kr
  * kw
  * lk
  * lt
  * lv
  * mx
  * my
  * nl
  * no
  * nz
  * pe
  * ph
  * pk
  * pl
  * pt
  * qa
  * ro
  * ru
  * sa
  * se
  * sg
  * sr
  * th
  * tr
  * tw
  * us
  * ve
  * vn
  * za

sector | 

  * Basic Materials
  * Communication Services
  * Consumer Cyclical
  * Consumer Defensive
  * Energy
  * Financial Services
  * Healthcare
  * Industrials
  * Real Estate
  * Technology
  * Utilities

exchanges | 

  * BSE
  * NAS
  * NCM
  * NGM
  * NMS
  * NYQ
  * YHD

peer_group | 

  * Aerospace & Defense
  * Auto Components
  * Automobiles
  * Banks
  * Building Products
  * Chemicals
  * China Fund Aggressive Allocation Fund
  * China Fund Equity Funds
  * China Fund QDII Greater China Equity
  * China Fund QDII Sector Equity
  * China Fund Sector Equity Financial and Real Estate
  * Commercial Services
  * Construction & Engineering
  * Construction Materials
  * Consumer Durables
  * Consumer Services
  * Containers & Packaging
  * Diversified Financials
  * Diversified Metals
  * EAA CE Global Large-Cap Blend Equity
  * EAA CE Other
  * EAA CE Sector Equity Biotechnology
  * EAA CE UK Large-Cap Equity
  * EAA CE UK Small-Cap Equity
  * EAA Fund Asia ex-Japan Equity
  * EAA Fund China Equity
  * EAA Fund China Equity - A Shares
  * EAA Fund Denmark Equity
  * EAA Fund EUR Aggressive Allocation - Global
  * EAA Fund EUR Corporate Bond
  * EAA Fund EUR Moderate Allocation - Global
  * EAA Fund Emerging Europe ex-Russia Equity
  * EAA Fund Europe Large-Cap Blend Equity
  * EAA Fund Eurozone Large-Cap Equity
  * EAA Fund Germany Equity
  * EAA Fund Global Emerging Markets Equity
  * EAA Fund Global Equity Income
  * EAA Fund Global Flex-Cap Equity
  * EAA Fund Global Large-Cap Blend Equity
  * EAA Fund Global Large-Cap Growth Equity
  * EAA Fund Hong Kong Equity
  * EAA Fund Japan Large-Cap Equity
  * EAA Fund Other Bond
  * EAA Fund Other Equity
  * EAA Fund RMB Bond - Onshore
  * EAA Fund Sector Equity Consumer Goods & Services
  * EAA Fund Sector Equity Financial Services
  * EAA Fund Sector Equity Industrial Materials
  * EAA Fund Sector Equity Technology
  * EAA Fund South Africa & Namibia Equity
  * EAA Fund Switzerland Equity
  * EAA Fund US Large-Cap Blend Equity
  * EAA Fund USD Corporate Bond
  * Electrical Equipment
  * Energy Services
  * Food Products
  * Food Retailers
  * Healthcare
  * Homebuilders
  * Household Products
  * India CE Multi-Cap
  * India Fund Large-Cap
  * India Fund Sector - Financial Services
  * Industrial Conglomerates
  * Insurance
  * Machinery
  * Media
  * Mexico Fund Mexico Equity
  * Oil & Gas Producers
  * Paper & Forestry
  * Pharmaceuticals
  * Precious Metals
  * Real Estate
  * Refiners & Pipelines
  * Retailing
  * Semiconductors
  * Software & Services
  * Steel
  * Technology Hardware
  * Telecommunication Services
  * Textiles & Apparel
  * Traders & Distributors
  * Transportation
  * Transportation Infrastructure
  * US CE Convertibles
  * US CE Options-based
  * US CE Preferred Stock
  * US Fund China Region
  * US Fund Consumer Cyclical
  * US Fund Diversified Emerging Mkts
  * US Fund Equity Energy
  * US Fund Equity Precious Metals
  * US Fund Financial
  * US Fund Foreign Large Blend
  * US Fund Health
  * US Fund Large Blend
  * US Fund Large Growth
  * US Fund Large Value
  * US Fund Miscellaneous Region
  * US Fund Natural Resources
  * US Fund Technology
  * US Fund Trading–Leveraged Equity
  * Utilities

valid_operand_fields

Valid Operand Fields

Permitted Keys/Values# Key | Values  
---|---  
eq_fields | 

  * exchanges
  * peer_group
  * region
  * sector

price | 

  * eodprice
  * fiftytwowkpercentchange
  * intradaymarketcap
  * intradayprice
  * intradaypricechange
  * lastclose52weekhigh.lasttwelvemonths
  * lastclose52weeklow.lasttwelvemonths
  * lastclosemarketcap.lasttwelvemonths
  * percentchange

trading | 

  * avgdailyvol3m
  * beta
  * dayvolume
  * eodvolume
  * pctheldinsider
  * pctheldinst

short_interest | 

  * days_to_cover_short.value
  * short_interest.value
  * short_interest_percentage_change.value
  * short_percentage_of_float.value
  * short_percentage_of_shares_outstanding.value

valuation | 

  * bookvalueshare.lasttwelvemonths
  * lastclosemarketcaptotalrevenue.lasttwelvemonths
  * lastclosepriceearnings.lasttwelvemonths
  * lastclosepricetangiblebookvalue.lasttwelvemonths
  * lastclosetevtotalrevenue.lasttwelvemonths
  * pegratio_5y
  * peratio.lasttwelvemonths
  * pricebookratio.quarterly

profitability | 

  * consecutive_years_of_dividend_growth_count
  * forward_dividend_per_share
  * forward_dividend_yield
  * returnonassets.lasttwelvemonths
  * returnonequity.lasttwelvemonths
  * returnontotalcapital.lasttwelvemonths

leverage | 

  * ebitdainterestexpense.lasttwelvemonths
  * ebitinterestexpense.lasttwelvemonths
  * lastclosetevebit.lasttwelvemonths
  * lastclosetevebitda.lasttwelvemonths
  * ltdebtequity.lasttwelvemonths
  * netdebtebitda.lasttwelvemonths
  * totaldebtebitda.lasttwelvemonths
  * totaldebtequity.lasttwelvemonths

liquidity | 

  * altmanzscoreusingtheaveragestockinformationforaperiod.lasttwelvemonths
  * currentratio.lasttwelvemonths
  * operatingcashflowtocurrentliabilities.lasttwelvemonths
  * quickratio.lasttwelvemonths

income_statement | 

  * basicepscontinuingoperations.lasttwelvemonths
  * dilutedeps1yrgrowth.lasttwelvemonths
  * dilutedepscontinuingoperations.lasttwelvemonths
  * ebit.lasttwelvemonths
  * ebitda.lasttwelvemonths
  * ebitda1yrgrowth.lasttwelvemonths
  * ebitdamargin.lasttwelvemonths
  * epsgrowth.lasttwelvemonths
  * grossprofit.lasttwelvemonths
  * grossprofitmargin.lasttwelvemonths
  * netepsbasic.lasttwelvemonthsnetepsdiluted.lasttwelvemonths
  * netincome1yrgrowth.lasttwelvemonths
  * netincomeis.lasttwelvemonths
  * netincomemargin.lasttwelvemonths
  * operatingincome.lasttwelvemonths
  * quarterlyrevenuegrowth.quarterly
  * totalrevenues.lasttwelvemonths
  * totalrevenues1yrgrowth.lasttwelvemonths

balance_sheet | 

  * totalassets.lasttwelvemonths
  * totalcashandshortterminvestments.lasttwelvemonths
  * totalcommonequity.lasttwelvemonths
  * totalcommonsharesoutstanding.lasttwelvemonths
  * totalcurrentassets.lasttwelvemonths
  * totalcurrentliabilities.lasttwelvemonths
  * totaldebt.lasttwelvemonths
  * totalequity.lasttwelvemonths
  * totalsharesoutstanding

cash_flow | 

  * capitalexpenditure.lasttwelvemonths
  * cashfromoperations.lasttwelvemonths
  * cashfromoperations1yrgrowth.lasttwelvemonths
  * forward_dividend_yield
  * leveredfreecashflow.lasttwelvemonths
  * leveredfreecashflow1yrgrowth.lasttwelvemonths
  * unleveredfreecashflow.lasttwelvemonths

esg | 

  * environmental_score
  * esg_score
  * governance_score
  * highest_controversy
  * social_score

Methods

__init__(_operator : str_, _operand : Real | str | List[EquityQuery]_)

See also

`EquityQuery.valid_operand_fields`

supported operand values for query

`EquityQuery.valid_eq_operand_map`

supported EQ query operand parameters

to_dict() -> Dict

[ __ previous yfinance.download ](yfinance.download.html "previous page") [ next Screener __](yfinance.Screener.html "next page")

__On this page

  * `EquityQuery`

[ __Show Source](../../_sources/reference/api/yfinance.EquityQuery.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="financials">Financials#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * Financials __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * [API Reference](index.html)
  * Financials

# Financials#

[`get_income_stmt`](api/yfinance.Ticker.get_income_stmt.html#yfinance.Ticker.get_income_stmt "yfinance.Ticker.get_income_stmt")([proxy, as_dict, pretty, freq]) |   
---|---  
[`income_stmt`](api/yfinance.Ticker.income_stmt.html#yfinance.Ticker.income_stmt "yfinance.Ticker.income_stmt") |   
[`get_balance_sheet`](api/yfinance.Ticker.get_balance_sheet.html#yfinance.Ticker.get_balance_sheet "yfinance.Ticker.get_balance_sheet")([proxy, as_dict, pretty, freq]) |   
[`balance_sheet`](api/yfinance.Ticker.balance_sheet.html#yfinance.Ticker.balance_sheet "yfinance.Ticker.balance_sheet") |   
[`get_cashflow`](api/yfinance.Ticker.get_cashflow.html#yfinance.Ticker.get_cashflow "yfinance.Ticker.get_cashflow")([proxy, as_dict, pretty, freq]) |   
[`cashflow`](api/yfinance.Ticker.cashflow.html#yfinance.Ticker.cashflow "yfinance.Ticker.cashflow") |   
[`get_earnings`](api/yfinance.Ticker.get_earnings.html#yfinance.Ticker.get_earnings "yfinance.Ticker.get_earnings")([proxy, as_dict, freq]) |   
[`earnings`](api/yfinance.Ticker.earnings.html#yfinance.Ticker.earnings "yfinance.Ticker.earnings") |   
[`calendar`](api/yfinance.Ticker.calendar.html#yfinance.Ticker.calendar "yfinance.Ticker.calendar") | Returns a dictionary of events, earnings, and dividends for the ticker  
[`get_earnings_dates`](api/yfinance.Ticker.get_earnings_dates.html#yfinance.Ticker.get_earnings_dates "yfinance.Ticker.get_earnings_dates")([limit, proxy]) | Get earning dates (future and historic)  
[`earnings_dates`](api/yfinance.Ticker.earnings_dates.html#yfinance.Ticker.earnings_dates "yfinance.Ticker.earnings_dates") |   
[`get_sec_filings`](api/yfinance.Ticker.get_sec_filings.html#yfinance.Ticker.get_sec_filings "yfinance.Ticker.get_sec_filings")([proxy]) |   
[`sec_filings`](api/yfinance.Ticker.sec_filings.html#yfinance.Ticker.sec_filings "yfinance.Ticker.sec_filings") |   
  
[ __ previous yfinance.Ticker.news ](api/yfinance.Ticker.news.html "previous page") [ next yfinance.Ticker.get_income_stmt __](api/yfinance.Ticker.get_income_stmt.html "next page")

[ __Show Source](../_sources/reference/yfinance.financials.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="functions-and-utilities">Functions and Utilities#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * Functions and Utilities __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * [API Reference](index.html)
  * Functions...

# Functions and Utilities#

## Download Market Data#

The download function allows you to retrieve market data for multiple tickers at once.

[`download`](api/yfinance.download.html#yfinance.download "yfinance.download")(tickers[, start, end, actions, ...]) | Download yahoo tickers :Parameters: tickers : str, list List of tickers to download period : str Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max Either Use period parameter or use start and end interval : str Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo Intraday data cannot extend last 60 days start: str Download start date string (YYYY-MM-DD) or _datetime, inclusive. Default is 99 years ago E.g. for start="2020-01-01", the first data point will be on "2020-01-01" end: str Download end date string (YYYY-MM-DD) or _datetime, exclusive. Default is now E.g. for end="2023-01-01", the last data point will be on "2022-12-31" group_by : str Group by 'ticker' or 'column' (default) prepost : bool Include Pre and Post market data in results? Default is False auto_adjust: bool Adjust all OHLC automatically? Default is True repair: bool Detect currency unit 100x mixups and attempt repair Default is False keepna: bool Keep NaN rows returned by Yahoo? Default is False actions: bool Download dividend + stock splits data. Default is False threads: bool / int How many threads to use for mass downloading. Default is True ignore_tz: bool When combining from different timezones, ignore that part of datetime. Default depends on interval. Intraday = False. Day+ = True. proxy: str Optional. Proxy server URL scheme. Default is None rounding: bool Optional. Round values to 2 decimal places? timeout: None or float If not None stops waiting for a response after given number of seconds. (Can also be a fraction of a second e.g. 0.01) session: None or Session Optional. Pass your own session object to be used for all requests multi_level_index: bool Optional. Always return a MultiIndex DataFrame? Default is True.  
---|---  
  
## Query Market Data#

The Sector and Industry modules allow you to access the sector and industry information.

[`EquityQuery`](api/yfinance.EquityQuery.html#yfinance.EquityQuery "yfinance.EquityQuery")(operator, operand) | The EquityQuery class constructs filters for stocks based on specific criteria such as region, sector, exchange, and peer group.  
---|---  
[`Screener`](api/yfinance.Screener.html#yfinance.Screener "yfinance.Screener")([session, proxy]) | The Screener class is used to execute the queries and return the filtered results.  
  
See also

`EquityQuery.valid_operand_fields`

supported operand values for query

`EquityQuery.valid_eq_operand_map`

supported EQ query operand parameters

`Screener.predefined_bodies`

supported predefined screens

## Enable Debug Mode#

Enables logging of debug information for the yfinance package.

[`enable_debug_mode`](api/yfinance.enable_debug_mode.html#yfinance.enable_debug_mode "yfinance.enable_debug_mode")() |   
---|---  
  
## Set Timezone Cache Location#

Sets the cache location for timezone data.

[`set_tz_cache_location`](api/yfinance.set_tz_cache_location.html#yfinance.set_tz_cache_location "yfinance.set_tz_cache_location")(cache_dir) |   
---|---  
  
[ __ previous Industry ](api/yfinance.Industry.html "previous page") [ next yfinance.download __](api/yfinance.download.html "next page")

__On this page

  * Download Market Data
  * Query Market Data
  * Enable Debug Mode
  * Set Timezone Cache Location

[ __Show Source](../_sources/reference/yfinance.functions.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="fundsdata-class">FundsData class#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * FundsData class __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * [API Reference](index.html)
  * FundsD...

# FundsData class#

[`FundsData`](api/yfinance.scrapers.funds.FundsData.html#yfinance.scrapers.funds.FundsData "yfinance.scrapers.funds.FundsData")(data, symbol[, proxy]) | ETF and Mutual Funds Data Queried Modules: quoteType, summaryProfile, fundProfile, topHoldings  
---|---  
  
[ __ previous yfinance.set_tz_cache_location ](api/yfinance.set_tz_cache_location.html "previous page") [ next FundsData __](api/yfinance.scrapers.funds.FundsData.html "next page")

[ __Show Source](../_sources/reference/yfinance.funds_data.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="fundsdata">FundsData#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * FundsData
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [FundsData class](../yfinance.funds_data.html)
  * FundsData

# FundsData#

_class _yfinance.scrapers.funds.FundsData(_data : YfData_, _symbol : str_, _proxy =None_)#

ETF and Mutual Funds Data Queried Modules: quoteType, summaryProfile, fundProfile, topHoldings

Notes: \- fundPerformance module is not implemented as better data is queryable using history

Parameters:

  * **data** (_YfData_) – The YfData object for fetching data.

  * **symbol** (_str_) – The symbol of the fund.

  * **proxy** (_optional_) – Proxy settings for fetching data.

Attributes

asset_classes

Returns the asset classes of the fund.

Returns:

The asset classes.

Return type:

Dict[str, float]

bond_holdings

Returns the bond holdings of the fund.

Returns:

The bond holdings.

Return type:

pd.DataFrame

bond_ratings

Returns the bond ratings of the fund.

Returns:

The bond ratings.

Return type:

Dict[str, float]

description

Returns the description of the fund.

Returns:

The description.

Return type:

str

equity_holdings

Returns the equity holdings of the fund.

Returns:

The equity holdings.

Return type:

pd.DataFrame

fund_operations

Returns the fund operations.

Returns:

The fund operations.

Return type:

pd.DataFrame

fund_overview

Returns the fund overview.

Returns:

The fund overview.

Return type:

Dict[str, Optional[str]]

sector_weightings

Returns the sector weightings of the fund.

Returns:

The sector weightings.

Return type:

Dict[str, float]

top_holdings

Returns the top holdings of the fund.

Returns:

The top holdings.

Return type:

pd.DataFrame

Methods

__init__(_data : YfData_, _symbol : str_, _proxy =None_)

Parameters:

  * **data** (_YfData_) – The YfData object for fetching data.

  * **symbol** (_str_) – The symbol of the fund.

  * **proxy** (_optional_) – Proxy settings for fetching data.

quote_type() -> str

Returns the quote type of the fund.

Returns:

The quote type.

Return type:

str

[ __ previous FundsData class ](../yfinance.funds_data.html "previous page") [ next PriceHistory class __](../yfinance.price_history.html "next page")

__On this page

  * `FundsData`

[ __Show Source](../../_sources/reference/api/yfinance.scrapers.funds.FundsData.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="industry">Industry#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * Industry
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Sector and Industry](../yfinance.sector_industry.html)
  * Industry

# Industry#

_class _yfinance.Industry(_key_ , _session =None_, _proxy =None_)#

Represents an industry within a sector.

Parameters:

  * **key** (_str_) – The key identifier for the industry.

  * **session** (_optional_) – The session to use for requests.

  * **proxy** (_optional_) – The proxy to use for requests.

Attributes

key

Retrieves the key of the domain entity.

Returns:

The unique key of the domain entity.

Return type:

str

name

Retrieves the name of the domain entity.

Returns:

The name of the domain entity.

Return type:

str

overview

Retrieves the overview information of the domain entity.

Returns:

A dictionary containing an overview of the domain entity.

Return type:

Dict

research_reports

Retrieves research reports related to the domain entity.

Returns:

A list of research reports, where each report is a dictionary with metadata.

Return type:

List[Dict[str, str]]

sector_key

Returns the sector key of the industry.

Returns:

The sector key.

Return type:

str

sector_name

Returns the sector name of the industry.

Returns:

The sector name.

Return type:

str

symbol

Retrieves the symbol of the domain entity.

Returns:

The symbol representing the domain entity.

Return type:

str

ticker

Retrieves a Ticker object based on the domain entity’s symbol.

Returns:

A Ticker object associated with the domain entity.

Return type:

[Ticker](yfinance.Ticker.html#yfinance.Ticker "yfinance.Ticker")

top_companies

Retrieves the top companies within the domain entity.

Returns:

A DataFrame containing the top companies in the domain.

Return type:

pandas.DataFrame

top_growth_companies

Returns the top growth companies in the industry.

Returns:

DataFrame containing top growth companies.

Return type:

Optional[pd.DataFrame]

top_performing_companies

Returns the top performing companies in the industry.

Returns:

DataFrame containing top performing companies.

Return type:

Optional[pd.DataFrame]

Methods

__init__(_key_ , _session =None_, _proxy =None_)

Parameters:

  * **key** (_str_) – The key identifier for the industry.

  * **session** (_optional_) – The session to use for requests.

  * **proxy** (_optional_) – The proxy to use for requests.

[ __ previous Sector ](yfinance.Sector.html "previous page") [ next Functions and Utilities __](../yfinance.functions.html "next page")

__On this page

  * `Industry`

[ __Show Source](../../_sources/reference/api/yfinance.Industry.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="logging">Logging#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * Logging
  * [Proxy Server](proxy.html)
  * [Caching](caching.html)
  * [Multi-Level Column Index](multi_level_columns.html)

  * [ __](../index.html)
  * [Advanced](index.html)
  * Logging

# Logging#

yfinance uses the logging module to handle messages. By default, only errors are logged.

If debugging, you can switch to debug mode with custom formatting using:

    import yfinance as yf
    yf.enable_debug_mode()

[ __ previous Advanced ](index.html "previous page") [ next Proxy Server __](proxy.html "next page")

[ __Show Source](../_sources/advanced/logging.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="multi-level-column-index">Multi-Level Column Index#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Logging](logging.html)
  * [Proxy Server](proxy.html)
  * [Caching](caching.html)
  * Multi-Level Column Index

  * [ __](../index.html)
  * [Advanced](index.html)
  * Multi-Level...

# Multi-Level Column Index#

The following answer on Stack Overflow is for [How to deal with multi-level column names downloaded with yfinance?](https://stackoverflow.com/questions/63107801)

  * yfinance returns a pandas.DataFrame with multi-level column names, with a level for the ticker and a level for the stock price data

The answer discusses:

  * How to correctly read the the multi-level columns after saving the dataframe to a csv with pandas.DataFrame.to_csv

  * How to download single or multiple tickers into a singledataframe with single level column names and a ticker column

[ __ previous Caching ](caching.html "previous page") [ next API Reference __](../reference/index.html "next page")

[ __Show Source](../_sources/advanced/multi_level_columns.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="pricehistory-class">PriceHistory class#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * PriceHistory class

  * [ __](../index.html)
  * [API Reference](index.html)
  * PriceH...

# PriceHistory class#

_class _yfinance.scrapers.history.PriceHistory(_data_ , _ticker_ , _tz_ , _session =None_, _proxy =None_)#

get_actions(_proxy =None_) -> Series#

get_capital_gains(_proxy =None_) -> Series#

get_dividends(_proxy =None_) -> Series#

get_history_metadata(_proxy =None_) -> dict#

get_splits(_proxy =None_) -> Series#

history(_period ='1mo'_, _interval ='1d'_, _start =None_, _end =None_, _prepost =False_, _actions =True_, _auto_adjust =True_, _back_adjust =False_, _repair =False_, _keepna =False_, _proxy =None_, _rounding =False_, _timeout =10_, _raise_errors =False_) -> DataFrame#

Parameters:

periodstr

Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max Either Use period parameter or use start and end

intervalstr

Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo Intraday data cannot extend last 60 days

start: str

Download start date string (YYYY-MM-DD) or _datetime, inclusive. Default is 99 years ago E.g. for start=”2020-01-01”, the first data point will be on “2020-01-01”

end: str

Download end date string (YYYY-MM-DD) or _datetime, exclusive. Default is now E.g. for end=”2023-01-01”, the last data point will be on “2022-12-31”

prepostbool

Include Pre and Post market data in results? Default is False

auto_adjust: bool

Adjust all OHLC automatically? Default is True

back_adjust: bool

Back-adjusted data to mimic true historical prices

repair: bool

Detect currency unit 100x mixups and attempt repair. Default is False

keepna: bool

Keep NaN rows returned by Yahoo? Default is False

proxy: str

Optional. Proxy server URL scheme. Default is None

rounding: bool

Round values to 2 decimal places? Optional. Default is False = precision suggested by Yahoo!

timeout: None or float

If not None stops waiting for a response after given number of seconds. (Can also be a fraction of a second e.g. 0.01) Default is 10 seconds.

raise_errors: bool

If True, then raise errors as Exceptions instead of logging.

[ __ previous FundsData ](api/yfinance.scrapers.funds.FundsData.html "previous page") [ next Development __](../development/index.html "next page")

__On this page

  * `PriceHistory`
    * `PriceHistory.get_actions()`
    * `PriceHistory.get_capital_gains()`
    * `PriceHistory.get_dividends()`
    * `PriceHistory.get_history_metadata()`
    * `PriceHistory.get_splits()`
    * `PriceHistory.history()`

[ __Show Source](../_sources/reference/yfinance.price_history.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="proxy-server">Proxy Server#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Logging](logging.html)
  * Proxy Server
  * [Caching](caching.html)
  * [Multi-Level Column Index](multi_level_columns.html)

  * [ __](../index.html)
  * [Advanced](index.html)
  * Proxy Server

# Proxy Server#

You can download data via a proxy:

    msft = yf.Ticker("MSFT")
    msft.history(..., proxy="PROXY_SERVER")

[ __ previous Logging ](logging.html "previous page") [ next Caching __](caching.html "next page")

[ __Show Source](../_sources/advanced/proxy.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="reporting-a-bug">Reporting a Bug#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](../reference/index.html)
  * [ Development ](index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Contributiong to yfinance](contributing.html)
  * [Contribution to the documentation](documentation.html)
  * Reporting a Bug

  * [ __](../index.html)
  * [Development](index.html)
  * Reporting a Bug

# Reporting a Bug#

Open a new issue on our [GitHub](https://github.com/ranaroussi/yfinance/issues).

[ __ previous Contribution to the documentation ](documentation.html "previous page")

[ __Show Source](../_sources/development/reporting_bug.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="screener">Screener#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * Screener
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Functions and Utilities](../yfinance.functions.html)
  * Screener

# Screener#

_class _yfinance.Screener(_session =None_, _proxy =None_)#

The Screener class is used to execute the queries and return the filtered results.

The Screener class provides methods to set and manipulate the body of a screener request, fetch and parse the screener results, and access predefined screener bodies.

Parameters:

  * **session** (_requests.Session_ _,__optional_) – A requests session object to be used for making HTTP requests. Defaults to None.

  * **proxy** (_str_ _,__optional_) – A proxy URL to be used for making HTTP requests. Defaults to None.

See also

`Screener.predefined_bodies`

supported predefined screens

Attributes

body

predefined_bodies

Predefined Screeners

Permitted Keys/Values# Key | Values  
---|---  
aggressive_small_caps | {‘offset’: 0, ‘size’: 25, ‘sortField’: ‘eodvolume’, ‘sortType’: ‘desc’, ‘quoteType’: ‘equity’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NMS’]}, {‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NYQ’]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘LT’, ‘operands’: [‘epsgrowth.lasttwelvemonths’, 15]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
day_gainers | {‘offset’: 0, ‘size’: 25, ‘sortField’: ‘percentchange’, ‘sortType’: ‘DESC’, ‘quoteType’: ‘EQUITY’, ‘query’: {‘operator’: ‘AND’, ‘operands’: [{‘operator’: ‘gt’, ‘operands’: [‘percentchange’, 3]}, {‘operator’: ‘eq’, ‘operands’: [‘region’, ‘us’]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘intradaymarketcap’, 2000000000, 10000000000]}, {‘operator’: ‘BTWN’, ‘operands’: [‘intradaymarketcap’, 10000000000, 100000000000]}, {‘operator’: ‘GT’, ‘operands’: [‘intradaymarketcap’, 100000000000]}]}, {‘operator’: ‘gte’, ‘operands’: [‘intradayprice’, 5]}, {‘operator’: ‘gt’, ‘operands’: [‘dayvolume’, 15000]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
day_losers | {‘offset’: 0, ‘size’: 25, ‘sortField’: ‘percentchange’, ‘sortType’: ‘ASC’, ‘quoteType’: ‘EQUITY’, ‘query’: {‘operator’: ‘AND’, ‘operands’: [{‘operator’: ‘lt’, ‘operands’: [‘percentchange’, -2.5]}, {‘operator’: ‘eq’, ‘operands’: [‘region’, ‘us’]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘intradaymarketcap’, 2000000000, 10000000000]}, {‘operator’: ‘BTWN’, ‘operands’: [‘intradaymarketcap’, 10000000000, 100000000000]}, {‘operator’: ‘GT’, ‘operands’: [‘intradaymarketcap’, 100000000000]}]}, {‘operator’: ‘gte’, ‘operands’: [‘intradayprice’, 5]}, {‘operator’: ‘gt’, ‘operands’: [‘dayvolume’, 20000]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
growth_technology_stocks | {‘offset’: 0, ‘size’: 25, ‘sortField’: ‘eodvolume’, ‘sortType’: ‘desc’, ‘quoteType’: ‘equity’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘quarterlyrevenuegrowth.quarterly’, 50, 100]}, {‘operator’: ‘GT’, ‘operands’: [‘quarterlyrevenuegrowth.quarterly’, 100]}, {‘operator’: ‘BTWN’, ‘operands’: [‘quarterlyrevenuegrowth.quarterly’, 25, 50]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘epsgrowth.lasttwelvemonths’, 25, 50]}, {‘operator’: ‘BTWN’, ‘operands’: [‘epsgrowth.lasttwelvemonths’, 50, 100]}, {‘operator’: ‘GT’, ‘operands’: [‘epsgrowth.lasttwelvemonths’, 100]}]}, {‘operator’: ‘eq’, ‘operands’: [‘sector’, ‘Technology’]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NMS’]}, {‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NYQ’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
most_actives | {‘offset’: 0, ‘size’: 25, ‘sortField’: ‘dayvolume’, ‘sortType’: ‘DESC’, ‘quoteType’: ‘EQUITY’, ‘query’: {‘operator’: ‘AND’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘region’, ‘us’]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘intradaymarketcap’, 10000000000, 100000000000]}, {‘operator’: ‘GT’, ‘operands’: [‘intradaymarketcap’, 100000000000]}, {‘operator’: ‘BTWN’, ‘operands’: [‘intradaymarketcap’, 2000000000, 10000000000]}]}, {‘operator’: ‘gt’, ‘operands’: [‘dayvolume’, 5000000]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
most_shorted_stocks | {‘size’: 25, ‘offset’: 0, ‘sortField’: ‘short_percentage_of_shares_outstanding.value’, ‘sortType’: ‘DESC’, ‘quoteType’: ‘EQUITY’, ‘topOperator’: ‘AND’, ‘query’: {‘operator’: ‘AND’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘region’, ‘us’]}]}, {‘operator’: ‘gt’, ‘operands’: [‘intradayprice’, 1]}, {‘operator’: ‘gt’, ‘operands’: [‘avgdailyvol3m’, 200000]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
small_cap_gainers | {‘offset’: 0, ‘size’: 25, ‘sortField’: ‘eodvolume’, ‘sortType’: ‘desc’, ‘quoteType’: ‘equity’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘lt’, ‘operands’: [‘intradaymarketcap’, 2000000000]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NMS’]}, {‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NYQ’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
undervalued_growth_stocks | {‘offset’: 0, ‘size’: 25, ‘sortType’: ‘DESC’, ‘sortField’: ‘eodvolume’, ‘quoteType’: ‘EQUITY’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘peratio.lasttwelvemonths’, 0, 20]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘LT’, ‘operands’: [‘pegratio_5y’, 1]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘epsgrowth.lasttwelvemonths’, 25, 50]}, {‘operator’: ‘BTWN’, ‘operands’: [‘epsgrowth.lasttwelvemonths’, 50, 100]}, {‘operator’: ‘GT’, ‘operands’: [‘epsgrowth.lasttwelvemonths’, 100]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NMS’]}, {‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NYQ’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
undervalued_large_caps | {‘offset’: 0, ‘size’: 25, ‘sortField’: ‘eodvolume’, ‘sortType’: ‘desc’, ‘quoteType’: ‘equity’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘BTWN’, ‘operands’: [‘peratio.lasttwelvemonths’, 0, 20]}]}, {‘operator’: ‘lt’, ‘operands’: [‘pegratio_5y’, 1]}, {‘operator’: ‘btwn’, ‘operands’: [‘intradaymarketcap’, 10000000000, 100000000000]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NMS’]}, {‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NYQ’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
conservative_foreign_funds | {‘offset’: 0, ‘size’: 25, ‘sortType’: ‘DESC’, ‘sortField’: ‘fundnetassets’, ‘quoteType’: ‘MUTUALFUND’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Large Value’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Large Blend’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Large Growth’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Growth’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Large Blend’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Blend’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Value’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Blend’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Value’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Blend’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Value’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Blend’]}, {‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Foreign Small/Mid Value’]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 4]}, {‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 5]}]}, {‘operator’: ‘lt’, ‘operands’: [‘initialinvestment’, 100001]}, {‘operator’: ‘lt’, ‘operands’: [‘annualreturnnavy1categoryrank’, 50]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘riskratingoverall’, 1]}, {‘operator’: ‘EQ’, ‘operands’: [‘riskratingoverall’, 3]}, {‘operator’: ‘EQ’, ‘operands’: [‘riskratingoverall’, 2]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NAS’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
high_yield_bond | {‘offset’: 0, ‘size’: 25, ‘sortType’: ‘DESC’, ‘sortField’: ‘fundnetassets’, ‘quoteType’: ‘MUTUALFUND’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 4]}, {‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 5]}]}, {‘operator’: ‘lt’, ‘operands’: [‘initialinvestment’, 100001]}, {‘operator’: ‘lt’, ‘operands’: [‘annualreturnnavy1categoryrank’, 50]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘riskratingoverall’, 1]}, {‘operator’: ‘EQ’, ‘operands’: [‘riskratingoverall’, 3]}, {‘operator’: ‘EQ’, ‘operands’: [‘riskratingoverall’, 2]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘High Yield Bond’]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NAS’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
portfolio_anchors | {‘offset’: 0, ‘size’: 25, ‘sortType’: ‘DESC’, ‘sortField’: ‘fundnetassets’, ‘quoteType’: ‘MUTUALFUND’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Large Blend’]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 4]}, {‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 5]}]}, {‘operator’: ‘lt’, ‘operands’: [‘initialinvestment’, 100001]}, {‘operator’: ‘lt’, ‘operands’: [‘annualreturnnavy1categoryrank’, 50]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NAS’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
solid_large_growth_funds | {‘offset’: 0, ‘size’: 25, ‘sortType’: ‘DESC’, ‘sortField’: ‘fundnetassets’, ‘quoteType’: ‘MUTUALFUND’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Large Growth’]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 5]}, {‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 4]}]}, {‘operator’: ‘lt’, ‘operands’: [‘initialinvestment’, 100001]}, {‘operator’: ‘lt’, ‘operands’: [‘annualreturnnavy1categoryrank’, 50]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NAS’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
solid_midcap_growth_funds | {‘offset’: 0, ‘size’: 25, ‘sortType’: ‘DESC’, ‘sortField’: ‘fundnetassets’, ‘quoteType’: ‘MUTUALFUND’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘categoryname’, ‘Mid-Cap Growth’]}]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 5]}, {‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 4]}]}, {‘operator’: ‘lt’, ‘operands’: [‘initialinvestment’, 100001]}, {‘operator’: ‘lt’, ‘operands’: [‘annualreturnnavy1categoryrank’, 50]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NAS’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
top_mutual_funds | {‘offset’: 0, ‘size’: 25, ‘sortType’: ‘DESC’, ‘sortField’: ‘percentchange’, ‘quoteType’: ‘MUTUALFUND’, ‘query’: {‘operator’: ‘and’, ‘operands’: [{‘operator’: ‘gt’, ‘operands’: [‘intradayprice’, 15]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 5]}, {‘operator’: ‘EQ’, ‘operands’: [‘performanceratingoverall’, 4]}]}, {‘operator’: ‘gt’, ‘operands’: [‘initialinvestment’, 1000]}, {‘operator’: ‘or’, ‘operands’: [{‘operator’: ‘eq’, ‘operands’: [‘exchange’, ‘NAS’]}]}]}, ‘userId’: ‘’, ‘userIdType’: ‘guid’}  
  
response

Fetch screen result

Example

    result = screener.response
    symbols = [quote['symbol'] for quote in result['quotes']]

Methods

__init__(_session =None_, _proxy =None_)

Parameters:

  * **session** (_requests.Session_ _,__optional_) – A requests session object to be used for making HTTP requests. Defaults to None.

  * **proxy** (_str_ _,__optional_) – A proxy URL to be used for making HTTP requests. Defaults to None.

See also

`Screener.predefined_bodies`

supported predefined screens

patch_body(_values : Dict_) -> Screener

Patch parts of the body using dictionary input

Parameters:

**body** (_Dict_) – partial query body

Returns:

self

Return type:

Screener

Example

    screener.patch_body({"offset": 100})

set_body(_body : Dict_) -> Screener

Set the fully custom body using dictionary input

Parameters:

**body** (_Dict_) – full query body

Returns:

self

Return type:

Screener

Example

    screener.set_body({
        "offset": 0,
        "size": 100,
        "sortField": "ticker",
        "sortType": "desc",
        "quoteType": "equity",
        "query": qf.to_dict(),
        "userId": "",
        "userIdType": "guid"
    })

set_default_body(_query : Query_, _offset : int = 0_, _size : int = 100_, _sortField : str = 'ticker'_, _sortType : str = 'desc'_, _quoteType : str = 'equity'_, _userId : str = ''_, _userIdType : str = 'guid'_) -> Screener

Set the default body using a custom query.

Parameters:

  * **query** (_Query_) – The Query object to set as the body.

  * **offset** (_Optional_ _[__int_ _]_) – The offset for the results. Defaults to 0.

  * **size** (_Optional_ _[__int_ _]_) – The number of results to return. Defaults to 100. Maximum is 250 as set by Yahoo.

  * **sortField** (_Optional_ _[__str_ _]_) – The field to sort the results by. Defaults to “ticker”.

  * **sortType** (_Optional_ _[__str_ _]_) – The type of sorting (e.g., “asc” or “desc”). Defaults to “desc”.

  * **quoteType** (_Optional_ _[__str_ _]_) – The type of quote (e.g., “equity”). Defaults to “equity”.

  * **userId** (_Optional_ _[__str_ _]_) – The user ID. Defaults to an empty string.

  * **userIdType** (_Optional_ _[__str_ _]_) – The type of user ID (e.g., “guid”). Defaults to “guid”.

Returns:

self

Return type:

Screener

Example

    screener.set_default_body(qf)

set_predefined_body(_predefined_key : str_) -> Screener

Set a predefined body

Parameters:

**predefined_key** (_str_) – key to one of predefined screens

Returns:

self

Return type:

Screener

Example

    screener.set_predefined_body('day_gainers')

See also

`Screener.predefined_bodies`

supported predefined screens

[ __ previous EquityQuery ](yfinance.EquityQuery.html "previous page") [ next yfinance.enable_debug_mode __](yfinance.enable_debug_mode.html "next page")

__On this page

  * `Screener`

[ __Show Source](../../_sources/reference/api/yfinance.Screener.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="search">Search#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * Search
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Search & News](../yfinance.search.html)
  * Search

# Search#

_class _yfinance.Search(_query_ , _max_results =8_, _news_count =8_, _enable_fuzzy_query =False_, _session =None_, _proxy =None_, _timeout =30_, _raise_errors =True_)#

Fetches and organizes search results from Yahoo Finance, including stock quotes and news articles.

Parameters:

  * **query** – The search query (ticker symbol or company name).

  * **max_results** – Maximum number of stock quotes to return (default 8).

  * **news_count** – Number of news articles to include (default 8).

  * **enable_fuzzy_query** – Enable fuzzy search for typos (default False).

  * **session** – Custom HTTP session for requests (default None).

  * **proxy** – Proxy settings for requests (default None).

  * **timeout** – Request timeout in seconds (default 30).

  * **raise_errors** – Raise exceptions on error (default True).

Attributes

news

Get the news from the search results.

quotes

Get the quotes from the search results.

Methods

__init__(_query_ , _max_results =8_, _news_count =8_, _enable_fuzzy_query =False_, _session =None_, _proxy =None_, _timeout =30_, _raise_errors =True_)

Fetches and organizes search results from Yahoo Finance, including stock quotes and news articles.

Parameters:

  * **query** – The search query (ticker symbol or company name).

  * **max_results** – Maximum number of stock quotes to return (default 8).

  * **news_count** – Number of news articles to include (default 8).

  * **enable_fuzzy_query** – Enable fuzzy search for typos (default False).

  * **session** – Custom HTTP session for requests (default None).

  * **proxy** – Proxy settings for requests (default None).

  * **timeout** – Request timeout in seconds (default 30).

  * **raise_errors** – Raise exceptions on error (default True).

[ __ previous Search & News ](../yfinance.search.html "previous page") [ next Sector and Industry __](../yfinance.sector_industry.html "next page")

__On this page

  * `Search`

[ __Show Source](../../_sources/reference/api/yfinance.Search.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="sector-and-industry">Sector and Industry#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * Sector and Industry __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * [API Reference](index.html)
  * Sector and Industry

# Sector and Industry#

## Sector class#

The Sector and Industry modules provide access to the Sector and Industry information.

[`Sector`](api/yfinance.Sector.html#yfinance.Sector "yfinance.Sector")(key[, session, proxy]) | Represents a financial market sector and allows retrieval of sector-related data such as top ETFs, top mutual funds, and industry data.  
---|---  
[`Industry`](api/yfinance.Industry.html#yfinance.Industry "yfinance.Industry")(key[, session, proxy]) | Represents an industry within a sector.  
  
See also

`Sector.industries`

Map of sector and industry

## Sample Code#

To initialize, use the relevant sector or industry key as below.

    import yfinance as yf
    
    tech = yf.Sector('technology')
    software = yf.Industry('software-infrastructure')
    
    # Common information
    tech.key
    tech.name
    tech.symbol
    tech.ticker
    tech.overview
    tech.top_companies
    tech.research_reports
    
    # Sector information
    tech.top_etfs
    tech.top_mutual_funds
    tech.industries
    
    # Industry information
    software.sector_key
    software.sector_name
    software.top_performing_companies
    software.top_growth_companies

The modules can be chained with Ticker as below.

    import yfinance as yf
    # Ticker to Sector and Industry
    msft = yf.Ticker('MSFT')
    tech = yf.Sector(msft.info.get('sectorKey'))
    software = yf.Industry(msft.info.get('industryKey'))
    
    # Sector and Industry to Ticker
    tech_ticker = tech.ticker
    tech_ticker.info
    software_ticker = software.ticker
    software_ticker.history()

[ __ previous Search ](api/yfinance.Search.html "previous page") [ next Sector __](api/yfinance.Sector.html "next page")

__On this page

  * Sector class
  * Sample Code

[ __Show Source](../_sources/reference/yfinance.sector_industry.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="sector">Sector#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * Sector
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Sector and Industry](../yfinance.sector_industry.html)
  * Sector

# Sector#

_class _yfinance.Sector(_key_ , _session =None_, _proxy =None_)#

Represents a financial market sector and allows retrieval of sector-related data such as top ETFs, top mutual funds, and industry data.

Parameters:

  * **key** (_str_) – The key representing the sector.

  * **session** (_requests.Session_ _,__optional_) – A session for making requests. Defaults to None.

  * **proxy** (_dict_ _,__optional_) – A dictionary containing proxy settings for the request. Defaults to None.

See also

`Sector.industries`

Map of sector and industry

Attributes

industries

Gets the industries within the sector.

> Returns:
>     
> 
> pandas.DataFrame: A DataFrame with industries’ key, name, symbol, and market weight.

Permitted Keys/Values# Key | Values  
---|---  
basic-materials | 

  * agricultural-inputs
  * aluminum
  * building-materials
  * chemicals
  * coking-coal
  * copper
  * gold
  * lumber-wood-production
  * other-industrial-metals-mining
  * other-precious-metals-mining
  * paper-paper-products
  * silver
  * specialty-chemicals
  * steel

communication-services | 

  * advertising-agencies
  * broadcasting
  * electronic-gaming-multimedia
  * entertainment
  * internet-content-information
  * publishing
  * telecom-services

consumer-cyclical | 

  * apparel-manufacturing
  * apparel-retail
  * auto-manufacturers
  * auto-parts
  * auto-truck-dealerships
  * department-stores
  * footwear-accessories
  * furnishings-fixtures-appliances
  * gambling
  * home-improvement-retail
  * internet-retail
  * leisure
  * lodging
  * luxury-goods
  * packaging-containers
  * personal-services
  * recreational-vehicles
  * residential-construction
  * resorts-casinos
  * restaurants
  * specialty-retail
  * textile-manufacturing
  * travel-services

consumer-defensive | 

  * beverages-brewers
  * beverages-non-alcoholic
  * beverages-wineries-distilleries
  * confectioners
  * discount-stores
  * education-training-services
  * farm-products
  * food-distribution
  * grocery-stores
  * household-personal-products
  * packaged-foods
  * tobacco

energy | 

  * oil-gas-drilling
  * oil-gas-e-p
  * oil-gas-equipment-services
  * oil-gas-integrated
  * oil-gas-midstream
  * oil-gas-refining-marketing
  * thermal-coal
  * uranium

financial-services | 

  * asset-management
  * banks-diversified
  * banks-regional
  * capital-markets
  * credit-services
  * financial-conglomerates
  * financial-data-stock-exchanges
  * insurance-brokers
  * insurance-diversified
  * insurance-life
  * insurance-property-casualty
  * insurance-reinsurance
  * insurance-specialty
  * mortgage-finance
  * shell-companies

healthcare | 

  * biotechnology
  * diagnostics-research
  * drug-manufacturers-general
  * drug-manufacturers-specialty-generic
  * health-information-services
  * healthcare-plans
  * medical-care-facilities
  * medical-devices
  * medical-distribution
  * medical-instruments-supplies
  * pharmaceutical-retailers

industrials | 

  * aerospace-defense
  * airlines
  * airports-air-services
  * building-products-equipment
  * business-equipment-supplies
  * conglomerates
  * consulting-services
  * electrical-equipment-parts
  * engineering-construction
  * farm-heavy-construction-machinery
  * industrial-distribution
  * infrastructure-operations
  * integrated-freight-logistics
  * marine-shipping
  * metal-fabrication
  * pollution-treatment-controls
  * railroads
  * rental-leasing-services
  * security-protection-services
  * specialty-business-services
  * specialty-industrial-machinery
  * staffing-employment-services
  * tools-accessories
  * trucking
  * waste-management

real-estate | 

  * real-estate-development
  * real-estate-diversified
  * real-estate-services
  * reit-diversified
  * reit-healthcare-facilities
  * reit-hotel-motel
  * reit-industrial
  * reit-mortgage
  * reit-office
  * reit-residential
  * reit-retail
  * reit-specialty

technology | 

  * communication-equipment
  * computer-hardware
  * consumer-electronics
  * electronic-components
  * electronics-computer-distribution
  * information-technology-services
  * scientific-technical-instruments
  * semiconductor-equipment-materials
  * semiconductors
  * software-application
  * software-infrastructure
  * solar

utilities | 

  * utilities-diversified
  * utilities-independent-power-producers
  * utilities-regulated-electric
  * utilities-regulated-gas
  * utilities-regulated-water
  * utilities-renewable

key

Retrieves the key of the domain entity.

Returns:

The unique key of the domain entity.

Return type:

str

name

Retrieves the name of the domain entity.

Returns:

The name of the domain entity.

Return type:

str

overview

Retrieves the overview information of the domain entity.

Returns:

A dictionary containing an overview of the domain entity.

Return type:

Dict

research_reports

Retrieves research reports related to the domain entity.

Returns:

A list of research reports, where each report is a dictionary with metadata.

Return type:

List[Dict[str, str]]

symbol

Retrieves the symbol of the domain entity.

Returns:

The symbol representing the domain entity.

Return type:

str

ticker

Retrieves a Ticker object based on the domain entity’s symbol.

Returns:

A Ticker object associated with the domain entity.

Return type:

[Ticker](yfinance.Ticker.html#yfinance.Ticker "yfinance.Ticker")

top_companies

Retrieves the top companies within the domain entity.

Returns:

A DataFrame containing the top companies in the domain.

Return type:

pandas.DataFrame

top_etfs

Gets the top ETFs for the sector.

Returns:

A dictionary of ETF symbols and names.

Return type:

Dict[str, str]

top_mutual_funds

Gets the top mutual funds for the sector.

Returns:

A dictionary of mutual fund symbols and names.

Return type:

Dict[str, str]

Methods

__init__(_key_ , _session =None_, _proxy =None_)

Parameters:

  * **key** (_str_) – The key representing the sector.

  * **session** (_requests.Session_ _,__optional_) – A session for making requests. Defaults to None.

  * **proxy** (_dict_ _,__optional_) – A dictionary containing proxy settings for the request. Defaults to None.

See also

`Sector.industries`

Map of sector and industry

[ __ previous Sector and Industry ](../yfinance.sector_industry.html "previous page") [ next Industry __](yfinance.Industry.html "next page")

__On this page

  * `Sector`

[ __Show Source](../../_sources/reference/api/yfinance.Sector.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="stock">Stock#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](yfinance.ticker_tickers.html) __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * Stock __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * [API Reference](index.html)
  * Stock

# Stock#

## Ticker stock methods#

[`get_isin`](api/yfinance.Ticker.get_isin.html#yfinance.Ticker.get_isin "yfinance.Ticker.get_isin")([proxy]) |   
---|---  
[`isin`](api/yfinance.Ticker.isin.html#yfinance.Ticker.isin "yfinance.Ticker.isin") |   
[`history`](api/yfinance.Ticker.history.html#yfinance.Ticker.history "yfinance.Ticker.history")(*args, **kwargs) |   
  
See also

[`yfinance.scrapers.history.PriceHistory.history()`](yfinance.price_history.html#yfinance.scrapers.history.PriceHistory.history "yfinance.scrapers.history.PriceHistory.history")

Documentation for history

[`get_history_metadata`](api/yfinance.Ticker.get_history_metadata.html#yfinance.Ticker.get_history_metadata "yfinance.Ticker.get_history_metadata")([proxy]) |   
---|---  
[`get_dividends`](api/yfinance.Ticker.get_dividends.html#yfinance.Ticker.get_dividends "yfinance.Ticker.get_dividends")([proxy]) |   
[`dividends`](api/yfinance.Ticker.dividends.html#yfinance.Ticker.dividends "yfinance.Ticker.dividends") |   
[`get_splits`](api/yfinance.Ticker.get_splits.html#yfinance.Ticker.get_splits "yfinance.Ticker.get_splits")([proxy]) |   
[`splits`](api/yfinance.Ticker.splits.html#yfinance.Ticker.splits "yfinance.Ticker.splits") |   
[`get_actions`](api/yfinance.Ticker.get_actions.html#yfinance.Ticker.get_actions "yfinance.Ticker.get_actions")([proxy]) |   
[`actions`](api/yfinance.Ticker.actions.html#yfinance.Ticker.actions "yfinance.Ticker.actions") |   
[`get_capital_gains`](api/yfinance.Ticker.get_capital_gains.html#yfinance.Ticker.get_capital_gains "yfinance.Ticker.get_capital_gains")([proxy]) |   
[`capital_gains`](api/yfinance.Ticker.capital_gains.html#yfinance.Ticker.capital_gains "yfinance.Ticker.capital_gains") |   
[`get_shares_full`](api/yfinance.Ticker.get_shares_full.html#yfinance.Ticker.get_shares_full "yfinance.Ticker.get_shares_full")([start, end, proxy]) |   
[`get_info`](api/yfinance.Ticker.get_info.html#yfinance.Ticker.get_info "yfinance.Ticker.get_info")([proxy]) |   
[`info`](api/yfinance.Ticker.info.html#yfinance.Ticker.info "yfinance.Ticker.info") |   
[`get_fast_info`](api/yfinance.Ticker.get_fast_info.html#yfinance.Ticker.get_fast_info "yfinance.Ticker.get_fast_info")([proxy]) |   
[`fast_info`](api/yfinance.Ticker.fast_info.html#yfinance.Ticker.fast_info "yfinance.Ticker.fast_info") |   
[`get_news`](api/yfinance.Ticker.get_news.html#yfinance.Ticker.get_news "yfinance.Ticker.get_news")([proxy]) |   
[`news`](api/yfinance.Ticker.news.html#yfinance.Ticker.news "yfinance.Ticker.news") |   
  
[ __ previous Tickers ](api/yfinance.Tickers.html "previous page") [ next yfinance.Ticker.get_isin __](api/yfinance.Ticker.get_isin.html "next page")

__On this page

  * Ticker stock methods

[ __Show Source](../_sources/reference/yfinance.stock.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="ticker-and-tickers">Ticker and Tickers#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../index.html)

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../advanced/index.html)
  * [ API Reference ](index.html)
  * [ Development ](../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * Ticker and Tickers __
    * [Ticker](api/yfinance.Ticker.html)
    * [Tickers](api/yfinance.Tickers.html)
  * [Stock](yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](api/yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](api/yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](api/yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](api/yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](api/yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](api/yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](api/yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](api/yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](api/yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](api/yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](api/yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](api/yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](api/yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](api/yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](api/yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](api/yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](api/yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](api/yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](api/yfinance.Ticker.news.html)
  * [Financials](yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](api/yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](api/yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](api/yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](api/yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](api/yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](api/yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](api/yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](api/yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](api/yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](api/yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](api/yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](api/yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](api/yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](api/yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](api/yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](api/yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](api/yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](api/yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](api/yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](api/yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](api/yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](api/yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](api/yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](api/yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](api/yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](api/yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](api/yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](api/yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](api/yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](api/yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](api/yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](api/yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](api/yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](api/yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](api/yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](api/yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](api/yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](api/yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](api/yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](api/yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](api/yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](api/yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](api/yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](api/yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](api/yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](api/yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](api/yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](api/yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](api/yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](yfinance.search.html) __
    * [Search](api/yfinance.Search.html)
  * [Sector and Industry](yfinance.sector_industry.html) __
    * [Sector](api/yfinance.Sector.html)
    * [Industry](api/yfinance.Industry.html)
  * [Functions and Utilities](yfinance.functions.html) __
    * [yfinance.download](api/yfinance.download.html)
    * [EquityQuery](api/yfinance.EquityQuery.html)
    * [Screener](api/yfinance.Screener.html)
    * [yfinance.enable_debug_mode](api/yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](api/yfinance.set_tz_cache_location.html)
  * [FundsData class](yfinance.funds_data.html) __
    * [FundsData](api/yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](yfinance.price_history.html)

  * [ __](../index.html)
  * [API Reference](index.html)
  * Ticker and Tickers

# Ticker and Tickers#

## Class#

The Ticker module, allows you to access ticker data in a Pythonic way.

[`Ticker`](api/yfinance.Ticker.html#yfinance.Ticker "yfinance.Ticker")(ticker[, session, proxy]) |   
---|---  
[`Tickers`](api/yfinance.Tickers.html#yfinance.Tickers "yfinance.Tickers")(tickers[, session]) |   
  
## Ticker Sample Code#

The Ticker module, allows you to access ticker data in a Pythonic way.

    import yfinance as yf
    
    dat = yf.Ticker("MSFT")
    
    # get historical market data
    dat.history(period='1mo')
    
    # options
    dat.option_chain(dat.options[0]).calls
    
    # get financials
    dat.balance_sheet
    dat.quarterly_income_stmt
    
    # dates
    dat.calendar
    
    # general info
    dat.info
    
    # analysis
    dat.analyst_price_targets

To initialize multiple Ticker objects, use

    import yfinance as yf
    
    tickers = yf.Tickers('msft aapl goog')
    
    # access each ticker using (example)
    tickers.tickers['MSFT'].info
    tickers.tickers['AAPL'].history(period="1mo")
    tickers.tickers['GOOG'].actions

For tickers that are ETFs/Mutual Funds, Ticker.funds_data provides access to fund related data.

Funds’ Top Holdings and other data with category average is returned as pd.DataFrame.

    import yfinance as yf
    spy = yf.Ticker('SPY')
    data = spy.funds_data
    
    # show fund description
    data.description
    
    # show operational information
    data.fund_overview
    data.fund_operations
    
    # show holdings related information
    data.asset_classes
    data.top_holdings
    data.equity_holdings
    data.bond_holdings
    data.bond_ratings
    data.sector_weightings

If you want to use a proxy server for downloading data, use:

    import yfinance as yf
    
    msft = yf.Ticker("MSFT")
    
    msft.history(..., proxy="PROXY_SERVER")
    msft.get_actions(proxy="PROXY_SERVER")
    msft.get_dividends(proxy="PROXY_SERVER")
    msft.get_splits(proxy="PROXY_SERVER")
    msft.get_capital_gains(proxy="PROXY_SERVER")
    msft.get_balance_sheet(proxy="PROXY_SERVER")
    msft.get_cashflow(proxy="PROXY_SERVER")
    msft.option_chain(..., proxy="PROXY_SERVER")
    ...

To initialize multiple Ticker objects, use Tickers module

    import yfinance as yf
    
    tickers = yf.Tickers('msft aapl goog')
    
    # access each ticker using (example)
    tickers.tickers['MSFT'].info
    tickers.tickers['AAPL'].history(period="1mo")
    tickers.tickers['GOOG'].actions

[ __ previous API Reference ](index.html "previous page") [ next Ticker __](api/yfinance.Ticker.html "next page")

__On this page

  * Class
  * Ticker Sample Code

[ __Show Source](../_sources/reference/yfinance.ticker_tickers.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="ticker">Ticker#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * Ticker
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Ticker and Tickers](../yfinance.ticker_tickers.html)
  * Ticker

# Ticker#

_class _yfinance.Ticker(_ticker_ , _session =None_, _proxy =None_)#

Attributes

actions

analyst_price_targets

balance_sheet

balancesheet

basic_info

calendar

Returns a dictionary of events, earnings, and dividends for the ticker

capital_gains

cash_flow

cashflow

dividends

earnings

earnings_dates

earnings_estimate

earnings_history

eps_revisions

eps_trend

fast_info

financials

funds_data

growth_estimates

history_metadata

income_stmt

incomestmt

info

insider_purchases

insider_roster_holders

insider_transactions

institutional_holders

isin

major_holders

mutualfund_holders

news

options

quarterly_balance_sheet

quarterly_balancesheet

quarterly_cash_flow

quarterly_cashflow

quarterly_earnings

quarterly_financials

quarterly_income_stmt

quarterly_incomestmt

recommendations

recommendations_summary

revenue_estimate

sec_filings

shares

splits

sustainability

upgrades_downgrades

Methods

__init__(_ticker_ , _session =None_, _proxy =None_)

get_actions(_proxy =None_) -> Series

get_analyst_price_targets(_proxy =None_) -> dict

Keys: current low high mean median

get_balance_sheet(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)

Parameters:

as_dict: bool

Return table as Python dict Default is False

pretty: bool

Format row names nicely for readability Default is False

freq: str

“yearly” or “quarterly” Default is “yearly”

proxy: str

Optional. Proxy server URL scheme Default is None

get_balancesheet(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)

get_calendar(_proxy =None_) -> dict

get_capital_gains(_proxy =None_) -> Series

get_cash_flow(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_) -> DataFrame | dict

Parameters:

as_dict: bool

Return table as Python dict Default is False

pretty: bool

Format row names nicely for readability Default is False

freq: str

“yearly” or “quarterly” Default is “yearly”

proxy: str

Optional. Proxy server URL scheme Default is None

get_cashflow(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)

get_dividends(_proxy =None_) -> Series

get_earnings(_proxy =None_, _as_dict =False_, _freq ='yearly'_)

Parameters:

as_dict: bool

Return table as Python dict Default is False

freq: str

“yearly” or “quarterly” Default is “yearly”

proxy: str

Optional. Proxy server URL scheme Default is None

get_earnings_dates(_limit =12_, _proxy =None_) -> DataFrame | None

Get earning dates (future and historic)

Parameters:

  * **limit** (_int_) – max amount of upcoming and recent earnings dates to return. Default value 12 should return next 4 quarters and last 8 quarters. Increase if more history is needed.

  * **proxy** – requests proxy to use.

Returns:

pd.DataFrame

get_earnings_estimate(_proxy =None_, _as_dict =False_)

Index: 0q +1q 0y +1y Columns: numberOfAnalysts avg low high yearAgoEps growth

get_earnings_history(_proxy =None_, _as_dict =False_)

Index: pd.DatetimeIndex Columns: epsEstimate epsActual epsDifference surprisePercent

get_eps_revisions(_proxy =None_, _as_dict =False_)

Index: 0q +1q 0y +1y Columns: upLast7days upLast30days downLast7days downLast30days

get_eps_trend(_proxy =None_, _as_dict =False_)

Index: 0q +1q 0y +1y Columns: current 7daysAgo 30daysAgo 60daysAgo 90daysAgo

get_fast_info(_proxy =None_)

get_financials(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)

get_funds_data(_proxy =None_) -> [FundsData](yfinance.scrapers.funds.FundsData.html#yfinance.scrapers.funds.FundsData "yfinance.scrapers.funds.FundsData") | None

get_growth_estimates(_proxy =None_, _as_dict =False_)

Index: 0q +1q 0y +1y +5y -5y Columns: stock industry sector index

get_history_metadata(_proxy =None_) -> dict

get_income_stmt(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)

Parameters:

as_dict: bool

Return table as Python dict Default is False

pretty: bool

Format row names nicely for readability Default is False

freq: str

“yearly” or “quarterly” Default is “yearly”

proxy: str

Optional. Proxy server URL scheme Default is None

get_incomestmt(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)

get_info(_proxy =None_) -> dict

get_insider_purchases(_proxy =None_, _as_dict =False_)

get_insider_roster_holders(_proxy =None_, _as_dict =False_)

get_insider_transactions(_proxy =None_, _as_dict =False_)

get_institutional_holders(_proxy =None_, _as_dict =False_)

get_isin(_proxy =None_) -> str | None

get_major_holders(_proxy =None_, _as_dict =False_)

get_mutualfund_holders(_proxy =None_, _as_dict =False_)

get_news(_proxy =None_) -> list

get_recommendations(_proxy =None_, _as_dict =False_)

Returns a DataFrame with the recommendations Columns: period strongBuy buy hold sell strongSell

get_recommendations_summary(_proxy =None_, _as_dict =False_)

get_revenue_estimate(_proxy =None_, _as_dict =False_)

Index: 0q +1q 0y +1y Columns: numberOfAnalysts avg low high yearAgoRevenue growth

get_sec_filings(_proxy =None_) -> dict

get_shares(_proxy =None_, _as_dict =False_) -> DataFrame | dict

get_shares_full(_start =None_, _end =None_, _proxy =None_)

get_splits(_proxy =None_) -> Series

get_sustainability(_proxy =None_, _as_dict =False_)

get_upgrades_downgrades(_proxy =None_, _as_dict =False_)

Returns a DataFrame with the recommendations changes (upgrades/downgrades) Index: date of grade Columns: firm toGrade fromGrade action

history(_* args_, _** kwargs_) -> DataFrame

option_chain(_date =None_, _tz =None_)

[ __ previous Ticker and Tickers ](../yfinance.ticker_tickers.html "previous page") [ next Tickers __](yfinance.Tickers.html "next page")

__On this page

  * `Ticker`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="tickers">Tickers#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * Tickers
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Ticker and Tickers](../yfinance.ticker_tickers.html)
  * Tickers

# Tickers#

_class _yfinance.Tickers(_tickers_ , _session =None_)#

Methods

__init__(_tickers_ , _session =None_)

download(_period ='1mo'_, _interval ='1d'_, _start =None_, _end =None_, _prepost =False_, _actions =True_, _auto_adjust =True_, _repair =False_, _proxy =None_, _threads =True_, _group_by ='column'_, _progress =True_, _timeout =10_, _** kwargs_)

history(_period ='1mo'_, _interval ='1d'_, _start =None_, _end =None_, _prepost =False_, _actions =True_, _auto_adjust =True_, _repair =False_, _proxy =None_, _threads =True_, _group_by ='column'_, _progress =True_, _timeout =10_, _** kwargs_)

news()

[ __ previous Ticker ](yfinance.Ticker.html "previous page") [ next Stock __](../yfinance.stock.html "next page")

__On this page

  * `Tickers`

[ __Show Source](../../_sources/reference/api/yfinance.Tickers.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h3 id="yfinance-documentation">yfinance documentation#</h3>

Skip to main content

__Back to top

__ `Ctrl`+`K`

yfinance

  * [ Advanced ](advanced/index.html)
  * [ API Reference ](reference/index.html)
  * [ Development ](development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](advanced/index.html)
  * [ API Reference ](reference/index.html)
  * [ Development ](development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

# yfinance documentation#

## Download Market Data from Yahoo! Finance’s API#

IMPORTANT LEGAL DISCLAIMER

**Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc.**

yfinance is **not** affiliated, endorsed, or vetted by Yahoo, Inc. It’s an open-source tool that uses Yahoo’s publicly available APIs, and is intended for research and educational purposes.

**You should refer to Yahoo!’s terms of use** ([here](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm)), ([here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html)), and ([here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) for details on your rights to use the actual data downloaded. Remember - the Yahoo! finance API is intended for personal use only.

## Install#

    $ pip install yfinance

## Quick start#

Showing a small sample of yfinance API, the full API is much bigger and covered in [API Reference](reference/index.html).

    import yfinance as yf
    dat = yf.Ticker("MSFT")

One ticker symbol

    dat = yf.Ticker("MSFT")
    dat.info
    dat.calendar
    dat.analyst_price_targets
    dat.quarterly_income_stmt
    dat.history(period='1mo')
    dat.option_chain(dat.options[0]).calls

Multiple ticker symbols

    tickers = yf.Tickers('MSFT AAPL GOOG')
    tickers.tickers['MSFT'].info
    yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')

Funds

    spy = yf.Ticker('SPY').funds_data
    spy.description
    spy.top_holdings

  * [Advanced](advanced/index.html)
  * [API Reference](reference/index.html)
  * [Development](development/index.html)

[ next Advanced __](advanced/index.html "next page")

__On this page

  * Download Market Data from Yahoo! Finance’s API
  * Install
  * Quick start

[ __Show Source](_sources/index.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickeractions">yfinance.Ticker.actions#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * yfinance.Ticker.actions
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.actions#

_property _Ticker.actions _: DataFrame_#

[ __ previous yfinance.Ticker.get_actions ](yfinance.Ticker.get_actions.html "previous page") [ next yfinance.Ticker.get_capital_gains __](yfinance.Ticker.get_capital_gains.html "next page")

__On this page

  * `Ticker.actions`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.actions.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickeranalyst_price_targets">yfinance.Ticker.analyst_price_targets#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * yfinance.Ticker.analyst_price_targets
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.analyst_price_targets#

_property _Ticker.analyst_price_targets _: dict_#

[ __ previous yfinance.Ticker.get_analyst_price_targets ](yfinance.Ticker.get_analyst_price_targets.html "previous page") [ next yfinance.Ticker.get_earnings_estimate __](yfinance.Ticker.get_earnings_estimate.html "next page")

__On this page

  * `Ticker.analyst_price_targets`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.analyst_price_targets.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerbalance_sheet">yfinance.Ticker.balance_sheet#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * yfinance.Ticker.balance_sheet
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.balance_sheet#

_property _Ticker.balance_sheet _: DataFrame_#

[ __ previous yfinance.Ticker.get_balance_sheet ](yfinance.Ticker.get_balance_sheet.html "previous page") [ next yfinance.Ticker.get_cashflow __](yfinance.Ticker.get_cashflow.html "next page")

__On this page

  * `Ticker.balance_sheet`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.balance_sheet.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickercalendar">yfinance.Ticker.calendar#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * yfinance.Ticker.calendar
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.calendar#

_property _Ticker.calendar _: dict_#

Returns a dictionary of events, earnings, and dividends for the ticker

[ __ previous yfinance.Ticker.earnings ](yfinance.Ticker.earnings.html "previous page") [ next yfinance.Ticker.get_earnings_dates __](yfinance.Ticker.get_earnings_dates.html "next page")

__On this page

  * `Ticker.calendar`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.calendar.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickercapital_gains">yfinance.Ticker.capital_gains#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * yfinance.Ticker.capital_gains
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.capital_gains#

_property _Ticker.capital_gains _: Series_#

[ __ previous yfinance.Ticker.get_capital_gains ](yfinance.Ticker.get_capital_gains.html "previous page") [ next yfinance.Ticker.get_shares_full __](yfinance.Ticker.get_shares_full.html "next page")

__On this page

  * `Ticker.capital_gains`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.capital_gains.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickercashflow">yfinance.Ticker.cashflow#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * yfinance.Ticker.cashflow
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.cashflow#

_property _Ticker.cashflow _: DataFrame_#

[ __ previous yfinance.Ticker.get_cashflow ](yfinance.Ticker.get_cashflow.html "previous page") [ next yfinance.Ticker.get_earnings __](yfinance.Ticker.get_earnings.html "next page")

__On this page

  * `Ticker.cashflow`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.cashflow.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerdividends">yfinance.Ticker.dividends#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * yfinance.Ticker.dividends
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.dividends#

_property _Ticker.dividends _: Series_#

[ __ previous yfinance.Ticker.get_dividends ](yfinance.Ticker.get_dividends.html "previous page") [ next yfinance.Ticker.get_splits __](yfinance.Ticker.get_splits.html "next page")

__On this page

  * `Ticker.dividends`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.dividends.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerearnings">yfinance.Ticker.earnings#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * yfinance.Ticker.earnings
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.earnings#

_property _Ticker.earnings _: DataFrame_#

[ __ previous yfinance.Ticker.get_earnings ](yfinance.Ticker.get_earnings.html "previous page") [ next yfinance.Ticker.calendar __](yfinance.Ticker.calendar.html "next page")

__On this page

  * `Ticker.earnings`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.earnings.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerearnings_dates">yfinance.Ticker.earnings_dates#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * yfinance.Ticker.earnings_dates
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.earnings_dates#

_property _Ticker.earnings_dates _: DataFrame_#

[ __ previous yfinance.Ticker.get_earnings_dates ](yfinance.Ticker.get_earnings_dates.html "previous page") [ next yfinance.Ticker.get_sec_filings __](yfinance.Ticker.get_sec_filings.html "next page")

__On this page

  * `Ticker.earnings_dates`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.earnings_dates.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerearnings_estimate">yfinance.Ticker.earnings_estimate#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * yfinance.Ticker.earnings_estimate
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.earnings_estimate#

_property _Ticker.earnings_estimate _: DataFrame_#

[ __ previous yfinance.Ticker.get_earnings_estimate ](yfinance.Ticker.get_earnings_estimate.html "previous page") [ next yfinance.Ticker.get_revenue_estimate __](yfinance.Ticker.get_revenue_estimate.html "next page")

__On this page

  * `Ticker.earnings_estimate`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.earnings_estimate.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerearnings_history">yfinance.Ticker.earnings_history#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * yfinance.Ticker.earnings_history
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.earnings_history#

_property _Ticker.earnings_history _: DataFrame_#

[ __ previous yfinance.Ticker.get_earnings_history ](yfinance.Ticker.get_earnings_history.html "previous page") [ next yfinance.Ticker.get_eps_trend __](yfinance.Ticker.get_eps_trend.html "next page")

__On this page

  * `Ticker.earnings_history`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.earnings_history.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickereps_revisions">yfinance.Ticker.eps_revisions#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * yfinance.Ticker.eps_revisions
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.eps_revisions#

_property _Ticker.eps_revisions _: DataFrame_#

[ __ previous yfinance.Ticker.get_eps_revisions ](yfinance.Ticker.get_eps_revisions.html "previous page") [ next yfinance.Ticker.get_growth_estimates __](yfinance.Ticker.get_growth_estimates.html "next page")

__On this page

  * `Ticker.eps_revisions`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.eps_revisions.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickereps_trend">yfinance.Ticker.eps_trend#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * yfinance.Ticker.eps_trend
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.eps_trend#

_property _Ticker.eps_trend _: DataFrame_#

[ __ previous yfinance.Ticker.get_eps_trend ](yfinance.Ticker.get_eps_trend.html "previous page") [ next yfinance.Ticker.get_eps_revisions __](yfinance.Ticker.get_eps_revisions.html "next page")

__On this page

  * `Ticker.eps_trend`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.eps_trend.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerfast_info">yfinance.Ticker.fast_info#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * yfinance.Ticker.fast_info
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.fast_info#

_property _Ticker.fast_info#

[ __ previous yfinance.Ticker.get_fast_info ](yfinance.Ticker.get_fast_info.html "previous page") [ next yfinance.Ticker.get_news __](yfinance.Ticker.get_news.html "next page")

__On this page

  * `Ticker.fast_info`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.fast_info.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerfunds_data">yfinance.Ticker.funds_data#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * yfinance.Ticker.funds_data
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.funds_data#

_property _Ticker.funds_data _: [FundsData](yfinance.scrapers.funds.FundsData.html#yfinance.scrapers.funds.FundsData "yfinance.scrapers.funds.FundsData")_#

[ __ previous yfinance.Ticker.get_funds_data ](yfinance.Ticker.get_funds_data.html "previous page") [ next yfinance.Ticker.get_insider_purchases __](yfinance.Ticker.get_insider_purchases.html "next page")

__On this page

  * `Ticker.funds_data`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.funds_data.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_actions">yfinance.Ticker.get_actions#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * yfinance.Ticker.get_actions
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_actions#

Ticker.get_actions(_proxy =None_) -> Series#

[ __ previous yfinance.Ticker.splits ](yfinance.Ticker.splits.html "previous page") [ next yfinance.Ticker.actions __](yfinance.Ticker.actions.html "next page")

__On this page

  * `Ticker.get_actions()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_actions.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_analyst_price_targets">yfinance.Ticker.get_analyst_price_targets#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * yfinance.Ticker.get_analyst_price_targets
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_analyst_price_targets#

Ticker.get_analyst_price_targets(_proxy =None_) -> dict#

Keys: current low high mean median

[ __ previous yfinance.Ticker.sustainability ](yfinance.Ticker.sustainability.html "previous page") [ next yfinance.Ticker.analyst_price_targets __](yfinance.Ticker.analyst_price_targets.html "next page")

__On this page

  * `Ticker.get_analyst_price_targets()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_analyst_price_targets.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_balance_sheet">yfinance.Ticker.get_balance_sheet#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * yfinance.Ticker.get_balance_sheet
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.get_balance_sheet#

Ticker.get_balance_sheet(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)#

Parameters:

as_dict: bool

Return table as Python dict Default is False

pretty: bool

Format row names nicely for readability Default is False

freq: str

“yearly” or “quarterly” Default is “yearly”

proxy: str

Optional. Proxy server URL scheme Default is None

[ __ previous yfinance.Ticker.income_stmt ](yfinance.Ticker.income_stmt.html "previous page") [ next yfinance.Ticker.balance_sheet __](yfinance.Ticker.balance_sheet.html "next page")

__On this page

  * `Ticker.get_balance_sheet()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_balance_sheet.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_capital_gains">yfinance.Ticker.get_capital_gains#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * yfinance.Ticker.get_capital_gains
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_capital_gains#

Ticker.get_capital_gains(_proxy =None_) -> Series#

[ __ previous yfinance.Ticker.actions ](yfinance.Ticker.actions.html "previous page") [ next yfinance.Ticker.capital_gains __](yfinance.Ticker.capital_gains.html "next page")

__On this page

  * `Ticker.get_capital_gains()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_capital_gains.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_cashflow">yfinance.Ticker.get_cashflow#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * yfinance.Ticker.get_cashflow
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.get_cashflow#

Ticker.get_cashflow(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)#

[ __ previous yfinance.Ticker.balance_sheet ](yfinance.Ticker.balance_sheet.html "previous page") [ next yfinance.Ticker.cashflow __](yfinance.Ticker.cashflow.html "next page")

__On this page

  * `Ticker.get_cashflow()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_cashflow.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_dividends">yfinance.Ticker.get_dividends#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * yfinance.Ticker.get_dividends
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_dividends#

Ticker.get_dividends(_proxy =None_) -> Series#

[ __ previous yfinance.Ticker.get_history_metadata ](yfinance.Ticker.get_history_metadata.html "previous page") [ next yfinance.Ticker.dividends __](yfinance.Ticker.dividends.html "next page")

__On this page

  * `Ticker.get_dividends()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_dividends.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_earnings">yfinance.Ticker.get_earnings#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * yfinance.Ticker.get_earnings
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.get_earnings#

Ticker.get_earnings(_proxy =None_, _as_dict =False_, _freq ='yearly'_)#

Parameters:

as_dict: bool

Return table as Python dict Default is False

freq: str

“yearly” or “quarterly” Default is “yearly”

proxy: str

Optional. Proxy server URL scheme Default is None

[ __ previous yfinance.Ticker.cashflow ](yfinance.Ticker.cashflow.html "previous page") [ next yfinance.Ticker.earnings __](yfinance.Ticker.earnings.html "next page")

__On this page

  * `Ticker.get_earnings()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_earnings.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_earnings_dates">yfinance.Ticker.get_earnings_dates#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * yfinance.Ticker.get_earnings_dates
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.get_earnings_dates#

Ticker.get_earnings_dates(_limit =12_, _proxy =None_) -> DataFrame | None#

Get earning dates (future and historic)

Parameters:

  * **limit** (_int_) – max amount of upcoming and recent earnings dates to return. Default value 12 should return next 4 quarters and last 8 quarters. Increase if more history is needed.

  * **proxy** – requests proxy to use.

Returns:

pd.DataFrame

[ __ previous yfinance.Ticker.calendar ](yfinance.Ticker.calendar.html "previous page") [ next yfinance.Ticker.earnings_dates __](yfinance.Ticker.earnings_dates.html "next page")

__On this page

  * `Ticker.get_earnings_dates()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_earnings_dates.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_earnings_estimate">yfinance.Ticker.get_earnings_estimate#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * yfinance.Ticker.get_earnings_estimate
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_earnings_estimate#

Ticker.get_earnings_estimate(_proxy =None_, _as_dict =False_)#

Index: 0q +1q 0y +1y Columns: numberOfAnalysts avg low high yearAgoEps growth

[ __ previous yfinance.Ticker.analyst_price_targets ](yfinance.Ticker.analyst_price_targets.html "previous page") [ next yfinance.Ticker.earnings_estimate __](yfinance.Ticker.earnings_estimate.html "next page")

__On this page

  * `Ticker.get_earnings_estimate()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_earnings_estimate.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_earnings_history">yfinance.Ticker.get_earnings_history#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * yfinance.Ticker.get_earnings_history
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_earnings_history#

Ticker.get_earnings_history(_proxy =None_, _as_dict =False_)#

Index: pd.DatetimeIndex Columns: epsEstimate epsActual epsDifference surprisePercent

[ __ previous yfinance.Ticker.revenue_estimate ](yfinance.Ticker.revenue_estimate.html "previous page") [ next yfinance.Ticker.earnings_history __](yfinance.Ticker.earnings_history.html "next page")

__On this page

  * `Ticker.get_earnings_history()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_earnings_history.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_eps_revisions">yfinance.Ticker.get_eps_revisions#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * yfinance.Ticker.get_eps_revisions
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_eps_revisions#

Ticker.get_eps_revisions(_proxy =None_, _as_dict =False_)#

Index: 0q +1q 0y +1y Columns: upLast7days upLast30days downLast7days downLast30days

[ __ previous yfinance.Ticker.eps_trend ](yfinance.Ticker.eps_trend.html "previous page") [ next yfinance.Ticker.eps_revisions __](yfinance.Ticker.eps_revisions.html "next page")

__On this page

  * `Ticker.get_eps_revisions()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_eps_revisions.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_eps_trend">yfinance.Ticker.get_eps_trend#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * yfinance.Ticker.get_eps_trend
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_eps_trend#

Ticker.get_eps_trend(_proxy =None_, _as_dict =False_)#

Index: 0q +1q 0y +1y Columns: current 7daysAgo 30daysAgo 60daysAgo 90daysAgo

[ __ previous yfinance.Ticker.earnings_history ](yfinance.Ticker.earnings_history.html "previous page") [ next yfinance.Ticker.eps_trend __](yfinance.Ticker.eps_trend.html "next page")

__On this page

  * `Ticker.get_eps_trend()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_eps_trend.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_fast_info">yfinance.Ticker.get_fast_info#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * yfinance.Ticker.get_fast_info
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_fast_info#

Ticker.get_fast_info(_proxy =None_)#

[ __ previous yfinance.Ticker.info ](yfinance.Ticker.info.html "previous page") [ next yfinance.Ticker.fast_info __](yfinance.Ticker.fast_info.html "next page")

__On this page

  * `Ticker.get_fast_info()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_fast_info.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_funds_data">yfinance.Ticker.get_funds_data#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * yfinance.Ticker.get_funds_data
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_funds_data#

Ticker.get_funds_data(_proxy =None_) -> [FundsData](yfinance.scrapers.funds.FundsData.html#yfinance.scrapers.funds.FundsData "yfinance.scrapers.funds.FundsData") | None#

[ __ previous yfinance.Ticker.growth_estimates ](yfinance.Ticker.growth_estimates.html "previous page") [ next yfinance.Ticker.funds_data __](yfinance.Ticker.funds_data.html "next page")

__On this page

  * `Ticker.get_funds_data()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_funds_data.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_growth_estimates">yfinance.Ticker.get_growth_estimates#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * yfinance.Ticker.get_growth_estimates
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_growth_estimates#

Ticker.get_growth_estimates(_proxy =None_, _as_dict =False_)#

Index: 0q +1q 0y +1y +5y -5y Columns: stock industry sector index

[ __ previous yfinance.Ticker.eps_revisions ](yfinance.Ticker.eps_revisions.html "previous page") [ next yfinance.Ticker.growth_estimates __](yfinance.Ticker.growth_estimates.html "next page")

__On this page

  * `Ticker.get_growth_estimates()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_growth_estimates.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_history_metadata">yfinance.Ticker.get_history_metadata#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * yfinance.Ticker.get_history_metadata
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_history_metadata#

Ticker.get_history_metadata(_proxy =None_) -> dict#

[ __ previous yfinance.Ticker.history ](yfinance.Ticker.history.html "previous page") [ next yfinance.Ticker.get_dividends __](yfinance.Ticker.get_dividends.html "next page")

__On this page

  * `Ticker.get_history_metadata()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_history_metadata.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_income_stmt">yfinance.Ticker.get_income_stmt#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * yfinance.Ticker.get_income_stmt
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.get_income_stmt#

Ticker.get_income_stmt(_proxy =None_, _as_dict =False_, _pretty =False_, _freq ='yearly'_)#

Parameters:

as_dict: bool

Return table as Python dict Default is False

pretty: bool

Format row names nicely for readability Default is False

freq: str

“yearly” or “quarterly” Default is “yearly”

proxy: str

Optional. Proxy server URL scheme Default is None

[ __ previous Financials ](../yfinance.financials.html "previous page") [ next yfinance.Ticker.income_stmt __](yfinance.Ticker.income_stmt.html "next page")

__On this page

  * `Ticker.get_income_stmt()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_income_stmt.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_info">yfinance.Ticker.get_info#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * yfinance.Ticker.get_info
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_info#

Ticker.get_info(_proxy =None_) -> dict#

[ __ previous yfinance.Ticker.get_shares_full ](yfinance.Ticker.get_shares_full.html "previous page") [ next yfinance.Ticker.info __](yfinance.Ticker.info.html "next page")

__On this page

  * `Ticker.get_info()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_info.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_insider_purchases">yfinance.Ticker.get_insider_purchases#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * yfinance.Ticker.get_insider_purchases
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_insider_purchases#

Ticker.get_insider_purchases(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.funds_data ](yfinance.Ticker.funds_data.html "previous page") [ next yfinance.Ticker.insider_purchases __](yfinance.Ticker.insider_purchases.html "next page")

__On this page

  * `Ticker.get_insider_purchases()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_insider_purchases.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_insider_roster_holders">yfinance.Ticker.get_insider_roster_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * yfinance.Ticker.get_insider_roster_holders
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_insider_roster_holders#

Ticker.get_insider_roster_holders(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.insider_transactions ](yfinance.Ticker.insider_transactions.html "previous page") [ next yfinance.Ticker.insider_roster_holders __](yfinance.Ticker.insider_roster_holders.html "next page")

__On this page

  * `Ticker.get_insider_roster_holders()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_insider_roster_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_insider_transactions">yfinance.Ticker.get_insider_transactions#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * yfinance.Ticker.get_insider_transactions
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_insider_transactions#

Ticker.get_insider_transactions(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.insider_purchases ](yfinance.Ticker.insider_purchases.html "previous page") [ next yfinance.Ticker.insider_transactions __](yfinance.Ticker.insider_transactions.html "next page")

__On this page

  * `Ticker.get_insider_transactions()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_insider_transactions.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_institutional_holders">yfinance.Ticker.get_institutional_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * yfinance.Ticker.get_institutional_holders
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_institutional_holders#

Ticker.get_institutional_holders(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.major_holders ](yfinance.Ticker.major_holders.html "previous page") [ next yfinance.Ticker.institutional_holders __](yfinance.Ticker.institutional_holders.html "next page")

__On this page

  * `Ticker.get_institutional_holders()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_institutional_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_isin">yfinance.Ticker.get_isin#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * yfinance.Ticker.get_isin
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_isin#

Ticker.get_isin(_proxy =None_) -> str | None#

[ __ previous Stock ](../yfinance.stock.html "previous page") [ next yfinance.Ticker.isin __](yfinance.Ticker.isin.html "next page")

__On this page

  * `Ticker.get_isin()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_isin.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_major_holders">yfinance.Ticker.get_major_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * yfinance.Ticker.get_major_holders
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_major_holders#

Ticker.get_major_holders(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.insider_roster_holders ](yfinance.Ticker.insider_roster_holders.html "previous page") [ next yfinance.Ticker.major_holders __](yfinance.Ticker.major_holders.html "next page")

__On this page

  * `Ticker.get_major_holders()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_major_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_mutualfund_holders">yfinance.Ticker.get_mutualfund_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * yfinance.Ticker.get_mutualfund_holders
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_mutualfund_holders#

Ticker.get_mutualfund_holders(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.institutional_holders ](yfinance.Ticker.institutional_holders.html "previous page") [ next yfinance.Ticker.mutualfund_holders __](yfinance.Ticker.mutualfund_holders.html "next page")

__On this page

  * `Ticker.get_mutualfund_holders()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_mutualfund_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_news">yfinance.Ticker.get_news#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * yfinance.Ticker.get_news
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_news#

Ticker.get_news(_proxy =None_) -> list#

[ __ previous yfinance.Ticker.fast_info ](yfinance.Ticker.fast_info.html "previous page") [ next yfinance.Ticker.news __](yfinance.Ticker.news.html "next page")

__On this page

  * `Ticker.get_news()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_news.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_recommendations">yfinance.Ticker.get_recommendations#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * yfinance.Ticker.get_recommendations
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_recommendations#

Ticker.get_recommendations(_proxy =None_, _as_dict =False_)#

Returns a DataFrame with the recommendations Columns: period strongBuy buy hold sell strongSell

[ __ previous Analysis & Holdings ](../yfinance.analysis.html "previous page") [ next yfinance.Ticker.recommendations __](yfinance.Ticker.recommendations.html "next page")

__On this page

  * `Ticker.get_recommendations()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_recommendations.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_recommendations_summary">yfinance.Ticker.get_recommendations_summary#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * yfinance.Ticker.get_recommendations_summary
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_recommendations_summary#

Ticker.get_recommendations_summary(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.recommendations ](yfinance.Ticker.recommendations.html "previous page") [ next yfinance.Ticker.recommendations_summary __](yfinance.Ticker.recommendations_summary.html "next page")

__On this page

  * `Ticker.get_recommendations_summary()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_recommendations_summary.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_revenue_estimate">yfinance.Ticker.get_revenue_estimate#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * yfinance.Ticker.get_revenue_estimate
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_revenue_estimate#

Ticker.get_revenue_estimate(_proxy =None_, _as_dict =False_)#

Index: 0q +1q 0y +1y Columns: numberOfAnalysts avg low high yearAgoRevenue growth

[ __ previous yfinance.Ticker.earnings_estimate ](yfinance.Ticker.earnings_estimate.html "previous page") [ next yfinance.Ticker.revenue_estimate __](yfinance.Ticker.revenue_estimate.html "next page")

__On this page

  * `Ticker.get_revenue_estimate()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_revenue_estimate.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_sec_filings">yfinance.Ticker.get_sec_filings#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * yfinance.Ticker.get_sec_filings
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.get_sec_filings#

Ticker.get_sec_filings(_proxy =None_) -> dict#

[ __ previous yfinance.Ticker.earnings_dates ](yfinance.Ticker.earnings_dates.html "previous page") [ next yfinance.Ticker.sec_filings __](yfinance.Ticker.sec_filings.html "next page")

__On this page

  * `Ticker.get_sec_filings()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_sec_filings.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_shares_full">yfinance.Ticker.get_shares_full#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * yfinance.Ticker.get_shares_full
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_shares_full#

Ticker.get_shares_full(_start =None_, _end =None_, _proxy =None_)#

[ __ previous yfinance.Ticker.capital_gains ](yfinance.Ticker.capital_gains.html "previous page") [ next yfinance.Ticker.get_info __](yfinance.Ticker.get_info.html "next page")

__On this page

  * `Ticker.get_shares_full()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_shares_full.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_splits">yfinance.Ticker.get_splits#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * yfinance.Ticker.get_splits
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.get_splits#

Ticker.get_splits(_proxy =None_) -> Series#

[ __ previous yfinance.Ticker.dividends ](yfinance.Ticker.dividends.html "previous page") [ next yfinance.Ticker.splits __](yfinance.Ticker.splits.html "next page")

__On this page

  * `Ticker.get_splits()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_splits.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_sustainability">yfinance.Ticker.get_sustainability#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * yfinance.Ticker.get_sustainability
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_sustainability#

Ticker.get_sustainability(_proxy =None_, _as_dict =False_)#

[ __ previous yfinance.Ticker.upgrades_downgrades ](yfinance.Ticker.upgrades_downgrades.html "previous page") [ next yfinance.Ticker.sustainability __](yfinance.Ticker.sustainability.html "next page")

__On this page

  * `Ticker.get_sustainability()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_sustainability.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerget_upgrades_downgrades">yfinance.Ticker.get_upgrades_downgrades#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * yfinance.Ticker.get_upgrades_downgrades
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.get_upgrades_downgrades#

Ticker.get_upgrades_downgrades(_proxy =None_, _as_dict =False_)#

Returns a DataFrame with the recommendations changes (upgrades/downgrades) Index: date of grade Columns: firm toGrade fromGrade action

[ __ previous yfinance.Ticker.recommendations_summary ](yfinance.Ticker.recommendations_summary.html "previous page") [ next yfinance.Ticker.upgrades_downgrades __](yfinance.Ticker.upgrades_downgrades.html "next page")

__On this page

  * `Ticker.get_upgrades_downgrades()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.get_upgrades_downgrades.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickergrowth_estimates">yfinance.Ticker.growth_estimates#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * yfinance.Ticker.growth_estimates
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.growth_estimates#

_property _Ticker.growth_estimates _: DataFrame_#

[ __ previous yfinance.Ticker.get_growth_estimates ](yfinance.Ticker.get_growth_estimates.html "previous page") [ next yfinance.Ticker.get_funds_data __](yfinance.Ticker.get_funds_data.html "next page")

__On this page

  * `Ticker.growth_estimates`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.growth_estimates.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerhistory">yfinance.Ticker.history#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * yfinance.Ticker.history
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.history#

Ticker.history(_* args_, _** kwargs_) -> DataFrame#

[ __ previous yfinance.Ticker.isin ](yfinance.Ticker.isin.html "previous page") [ next yfinance.Ticker.get_history_metadata __](yfinance.Ticker.get_history_metadata.html "next page")

__On this page

  * `Ticker.history()`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.history.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerincome_stmt">yfinance.Ticker.income_stmt#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * yfinance.Ticker.income_stmt
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.income_stmt#

_property _Ticker.income_stmt _: DataFrame_#

[ __ previous yfinance.Ticker.get_income_stmt ](yfinance.Ticker.get_income_stmt.html "previous page") [ next yfinance.Ticker.get_balance_sheet __](yfinance.Ticker.get_balance_sheet.html "next page")

__On this page

  * `Ticker.income_stmt`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.income_stmt.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerinfo">yfinance.Ticker.info#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * yfinance.Ticker.info
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Ticker.info

# yfinance.Ticker.info#

_property _Ticker.info _: dict_#

[ __ previous yfinance.Ticker.get_info ](yfinance.Ticker.get_info.html "previous page") [ next yfinance.Ticker.get_fast_info __](yfinance.Ticker.get_fast_info.html "next page")

__On this page

  * `Ticker.info`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.info.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerinsider_purchases">yfinance.Ticker.insider_purchases#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * yfinance.Ticker.insider_purchases
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.insider_purchases#

_property _Ticker.insider_purchases _: DataFrame_#

[ __ previous yfinance.Ticker.get_insider_purchases ](yfinance.Ticker.get_insider_purchases.html "previous page") [ next yfinance.Ticker.get_insider_transactions __](yfinance.Ticker.get_insider_transactions.html "next page")

__On this page

  * `Ticker.insider_purchases`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.insider_purchases.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerinsider_roster_holders">yfinance.Ticker.insider_roster_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * yfinance.Ticker.insider_roster_holders
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.insider_roster_holders#

_property _Ticker.insider_roster_holders _: DataFrame_#

[ __ previous yfinance.Ticker.get_insider_roster_holders ](yfinance.Ticker.get_insider_roster_holders.html "previous page") [ next yfinance.Ticker.get_major_holders __](yfinance.Ticker.get_major_holders.html "next page")

__On this page

  * `Ticker.insider_roster_holders`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.insider_roster_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerinsider_transactions">yfinance.Ticker.insider_transactions#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * yfinance.Ticker.insider_transactions
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.insider_transactions#

_property _Ticker.insider_transactions _: DataFrame_#

[ __ previous yfinance.Ticker.get_insider_transactions ](yfinance.Ticker.get_insider_transactions.html "previous page") [ next yfinance.Ticker.get_insider_roster_holders __](yfinance.Ticker.get_insider_roster_holders.html "next page")

__On this page

  * `Ticker.insider_transactions`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.insider_transactions.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerinstitutional_holders">yfinance.Ticker.institutional_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * yfinance.Ticker.institutional_holders
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.institutional_holders#

_property _Ticker.institutional_holders _: DataFrame_#

[ __ previous yfinance.Ticker.get_institutional_holders ](yfinance.Ticker.get_institutional_holders.html "previous page") [ next yfinance.Ticker.get_mutualfund_holders __](yfinance.Ticker.get_mutualfund_holders.html "next page")

__On this page

  * `Ticker.institutional_holders`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.institutional_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerisin">yfinance.Ticker.isin#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * yfinance.Ticker.isin
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Ticker.isin

# yfinance.Ticker.isin#

_property _Ticker.isin#

[ __ previous yfinance.Ticker.get_isin ](yfinance.Ticker.get_isin.html "previous page") [ next yfinance.Ticker.history __](yfinance.Ticker.history.html "next page")

__On this page

  * `Ticker.isin`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.isin.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickermajor_holders">yfinance.Ticker.major_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * yfinance.Ticker.major_holders
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.major_holders#

_property _Ticker.major_holders _: DataFrame_#

[ __ previous yfinance.Ticker.get_major_holders ](yfinance.Ticker.get_major_holders.html "previous page") [ next yfinance.Ticker.get_institutional_holders __](yfinance.Ticker.get_institutional_holders.html "next page")

__On this page

  * `Ticker.major_holders`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.major_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickermutualfund_holders">yfinance.Ticker.mutualfund_holders#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * yfinance.Ticker.mutualfund_holders
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.mutualfund_holders#

_property _Ticker.mutualfund_holders _: DataFrame_#

[ __ previous yfinance.Ticker.get_mutualfund_holders ](yfinance.Ticker.get_mutualfund_holders.html "previous page") [ next Search & News __](../yfinance.search.html "next page")

__On this page

  * `Ticker.mutualfund_holders`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.mutualfund_holders.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickernews">yfinance.Ticker.news#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * yfinance.Ticker.news
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Ticker.news

# yfinance.Ticker.news#

_property _Ticker.news _: list_#

[ __ previous yfinance.Ticker.get_news ](yfinance.Ticker.get_news.html "previous page") [ next Financials __](../yfinance.financials.html "next page")

__On this page

  * `Ticker.news`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.news.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerrecommendations">yfinance.Ticker.recommendations#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * yfinance.Ticker.recommendations
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.recommendations#

_property _Ticker.recommendations#

[ __ previous yfinance.Ticker.get_recommendations ](yfinance.Ticker.get_recommendations.html "previous page") [ next yfinance.Ticker.get_recommendations_summary __](yfinance.Ticker.get_recommendations_summary.html "next page")

__On this page

  * `Ticker.recommendations`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.recommendations.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerrecommendations_summary">yfinance.Ticker.recommendations_summary#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * yfinance.Ticker.recommendations_summary
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.recommendations_summary#

_property _Ticker.recommendations_summary#

[ __ previous yfinance.Ticker.get_recommendations_summary ](yfinance.Ticker.get_recommendations_summary.html "previous page") [ next yfinance.Ticker.get_upgrades_downgrades __](yfinance.Ticker.get_upgrades_downgrades.html "next page")

__On this page

  * `Ticker.recommendations_summary`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.recommendations_summary.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerrevenue_estimate">yfinance.Ticker.revenue_estimate#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * yfinance.Ticker.revenue_estimate
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.revenue_estimate#

_property _Ticker.revenue_estimate _: DataFrame_#

[ __ previous yfinance.Ticker.get_revenue_estimate ](yfinance.Ticker.get_revenue_estimate.html "previous page") [ next yfinance.Ticker.get_earnings_history __](yfinance.Ticker.get_earnings_history.html "next page")

__On this page

  * `Ticker.revenue_estimate`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.revenue_estimate.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickersec_filings">yfinance.Ticker.sec_filings#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * yfinance.Ticker.sec_filings
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Financials](../yfinance.financials.html)
  * yfinance.Tic...

# yfinance.Ticker.sec_filings#

_property _Ticker.sec_filings _: dict_#

[ __ previous yfinance.Ticker.get_sec_filings ](yfinance.Ticker.get_sec_filings.html "previous page") [ next Analysis & Holdings __](../yfinance.analysis.html "next page")

__On this page

  * `Ticker.sec_filings`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.sec_filings.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickersplits">yfinance.Ticker.splits#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * yfinance.Ticker.splits
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Stock](../yfinance.stock.html)
  * yfinance.Tic...

# yfinance.Ticker.splits#

_property _Ticker.splits _: Series_#

[ __ previous yfinance.Ticker.get_splits ](yfinance.Ticker.get_splits.html "previous page") [ next yfinance.Ticker.get_actions __](yfinance.Ticker.get_actions.html "next page")

__On this page

  * `Ticker.splits`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.splits.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickersustainability">yfinance.Ticker.sustainability#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * yfinance.Ticker.sustainability
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.sustainability#

_property _Ticker.sustainability _: DataFrame_#

[ __ previous yfinance.Ticker.get_sustainability ](yfinance.Ticker.get_sustainability.html "previous page") [ next yfinance.Ticker.get_analyst_price_targets __](yfinance.Ticker.get_analyst_price_targets.html "next page")

__On this page

  * `Ticker.sustainability`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.sustainability.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancetickerupgrades_downgrades">yfinance.Ticker.upgrades_downgrades#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * yfinance.Ticker.upgrades_downgrades
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Analysis & Holdings](../yfinance.analysis.html)
  * yfinance.Tic...

# yfinance.Ticker.upgrades_downgrades#

_property _Ticker.upgrades_downgrades#

[ __ previous yfinance.Ticker.get_upgrades_downgrades ](yfinance.Ticker.get_upgrades_downgrades.html "previous page") [ next yfinance.Ticker.get_sustainability __](yfinance.Ticker.get_sustainability.html "next page")

__On this page

  * `Ticker.upgrades_downgrades`

[ __Show Source](../../_sources/reference/api/yfinance.Ticker.upgrades_downgrades.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinancedownload">yfinance.download#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * yfinance.download
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Functions and Utilities](../yfinance.functions.html)
  * yfinance.download

# yfinance.download#

yfinance.download(_tickers_ , _start =None_, _end =None_, _actions =False_, _threads =True_, _ignore_tz =None_, _group_by ='column'_, _auto_adjust =True_, _back_adjust =False_, _repair =False_, _keepna =False_, _progress =True_, _period ='max'_, _interval ='1d'_, _prepost =False_, _proxy =None_, _rounding =False_, _timeout =10_, _session =None_, _multi_level_index =True_) -> DataFrame | None#

Download yahoo tickers :Parameters:

> tickersstr, list
>     
> 
> List of tickers to download
> 
> periodstr
>     
> 
> Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max Either Use period parameter or use start and end
> 
> intervalstr
>     
> 
> Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo Intraday data cannot extend last 60 days
> 
> start: str
>     
> 
> Download start date string (YYYY-MM-DD) or _datetime, inclusive. Default is 99 years ago E.g. for start=”2020-01-01”, the first data point will be on “2020-01-01”
> 
> end: str
>     
> 
> Download end date string (YYYY-MM-DD) or _datetime, exclusive. Default is now E.g. for end=”2023-01-01”, the last data point will be on “2022-12-31”
> 
> group_bystr
>     
> 
> Group by ‘ticker’ or ‘column’ (default)
> 
> prepostbool
>     
> 
> Include Pre and Post market data in results? Default is False
> 
> auto_adjust: bool
>     
> 
> Adjust all OHLC automatically? Default is True
> 
> repair: bool
>     
> 
> Detect currency unit 100x mixups and attempt repair Default is False
> 
> keepna: bool
>     
> 
> Keep NaN rows returned by Yahoo? Default is False
> 
> actions: bool
>     
> 
> Download dividend + stock splits data. Default is False
> 
> threads: bool / int
>     
> 
> How many threads to use for mass downloading. Default is True
> 
> ignore_tz: bool
>     
> 
> When combining from different timezones, ignore that part of datetime. Default depends on interval. Intraday = False. Day+ = True.
> 
> proxy: str
>     
> 
> Optional. Proxy server URL scheme. Default is None
> 
> rounding: bool
>     
> 
> Optional. Round values to 2 decimal places?
> 
> timeout: None or float
>     
> 
> If not None stops waiting for a response after given number of seconds. (Can also be a fraction of a second e.g. 0.01)
> 
> session: None or Session
>     
> 
> Optional. Pass your own session object to be used for all requests
> 
> multi_level_index: bool
>     
> 
> Optional. Always return a MultiIndex DataFrame? Default is True

[ __ previous Functions and Utilities ](../yfinance.functions.html "previous page") [ next EquityQuery __](yfinance.EquityQuery.html "next page")

__On this page

  * `download()`

[ __Show Source](../../_sources/reference/api/yfinance.download.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinanceenable_debug_mode">yfinance.enable_debug_mode#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * yfinance.enable_debug_mode
    * [yfinance.set_tz_cache_location](yfinance.set_tz_cache_location.html)
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Functions and Utilities](../yfinance.functions.html)
  * yfinance.ena...

# yfinance.enable_debug_mode#

yfinance.enable_debug_mode()#

[ __ previous Screener ](yfinance.Screener.html "previous page") [ next yfinance.set_tz_cache_location __](yfinance.set_tz_cache_location.html "next page")

__On this page

  * `enable_debug_mode()`

[ __Show Source](../../_sources/reference/api/yfinance.enable_debug_mode.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---


<h4 id="yfinanceset_tz_cache_location">yfinance.set_tz_cache_location#</h4>

Skip to main content

__Back to top

__ `Ctrl`+`K`

[ yfinance ](../../index.html)

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

  * [ Advanced ](../../advanced/index.html)
  * [ API Reference ](../index.html)
  * [ Development ](../../development/index.html)

  * [__ GitHub](https://github.com/ranaroussi/yfinance "GitHub")

Section Navigation

  * [Ticker and Tickers](../yfinance.ticker_tickers.html) __
    * [Ticker](yfinance.Ticker.html)
    * [Tickers](yfinance.Tickers.html)
  * [Stock](../yfinance.stock.html) __
    * [yfinance.Ticker.get_isin](yfinance.Ticker.get_isin.html)
    * [yfinance.Ticker.isin](yfinance.Ticker.isin.html)
    * [yfinance.Ticker.history](yfinance.Ticker.history.html)
    * [yfinance.Ticker.get_history_metadata](yfinance.Ticker.get_history_metadata.html)
    * [yfinance.Ticker.get_dividends](yfinance.Ticker.get_dividends.html)
    * [yfinance.Ticker.dividends](yfinance.Ticker.dividends.html)
    * [yfinance.Ticker.get_splits](yfinance.Ticker.get_splits.html)
    * [yfinance.Ticker.splits](yfinance.Ticker.splits.html)
    * [yfinance.Ticker.get_actions](yfinance.Ticker.get_actions.html)
    * [yfinance.Ticker.actions](yfinance.Ticker.actions.html)
    * [yfinance.Ticker.get_capital_gains](yfinance.Ticker.get_capital_gains.html)
    * [yfinance.Ticker.capital_gains](yfinance.Ticker.capital_gains.html)
    * [yfinance.Ticker.get_shares_full](yfinance.Ticker.get_shares_full.html)
    * [yfinance.Ticker.get_info](yfinance.Ticker.get_info.html)
    * [yfinance.Ticker.info](yfinance.Ticker.info.html)
    * [yfinance.Ticker.get_fast_info](yfinance.Ticker.get_fast_info.html)
    * [yfinance.Ticker.fast_info](yfinance.Ticker.fast_info.html)
    * [yfinance.Ticker.get_news](yfinance.Ticker.get_news.html)
    * [yfinance.Ticker.news](yfinance.Ticker.news.html)
  * [Financials](../yfinance.financials.html) __
    * [yfinance.Ticker.get_income_stmt](yfinance.Ticker.get_income_stmt.html)
    * [yfinance.Ticker.income_stmt](yfinance.Ticker.income_stmt.html)
    * [yfinance.Ticker.get_balance_sheet](yfinance.Ticker.get_balance_sheet.html)
    * [yfinance.Ticker.balance_sheet](yfinance.Ticker.balance_sheet.html)
    * [yfinance.Ticker.get_cashflow](yfinance.Ticker.get_cashflow.html)
    * [yfinance.Ticker.cashflow](yfinance.Ticker.cashflow.html)
    * [yfinance.Ticker.get_earnings](yfinance.Ticker.get_earnings.html)
    * [yfinance.Ticker.earnings](yfinance.Ticker.earnings.html)
    * [yfinance.Ticker.calendar](yfinance.Ticker.calendar.html)
    * [yfinance.Ticker.get_earnings_dates](yfinance.Ticker.get_earnings_dates.html)
    * [yfinance.Ticker.earnings_dates](yfinance.Ticker.earnings_dates.html)
    * [yfinance.Ticker.get_sec_filings](yfinance.Ticker.get_sec_filings.html)
    * [yfinance.Ticker.sec_filings](yfinance.Ticker.sec_filings.html)
  * [Analysis & Holdings](../yfinance.analysis.html) __
    * [yfinance.Ticker.get_recommendations](yfinance.Ticker.get_recommendations.html)
    * [yfinance.Ticker.recommendations](yfinance.Ticker.recommendations.html)
    * [yfinance.Ticker.get_recommendations_summary](yfinance.Ticker.get_recommendations_summary.html)
    * [yfinance.Ticker.recommendations_summary](yfinance.Ticker.recommendations_summary.html)
    * [yfinance.Ticker.get_upgrades_downgrades](yfinance.Ticker.get_upgrades_downgrades.html)
    * [yfinance.Ticker.upgrades_downgrades](yfinance.Ticker.upgrades_downgrades.html)
    * [yfinance.Ticker.get_sustainability](yfinance.Ticker.get_sustainability.html)
    * [yfinance.Ticker.sustainability](yfinance.Ticker.sustainability.html)
    * [yfinance.Ticker.get_analyst_price_targets](yfinance.Ticker.get_analyst_price_targets.html)
    * [yfinance.Ticker.analyst_price_targets](yfinance.Ticker.analyst_price_targets.html)
    * [yfinance.Ticker.get_earnings_estimate](yfinance.Ticker.get_earnings_estimate.html)
    * [yfinance.Ticker.earnings_estimate](yfinance.Ticker.earnings_estimate.html)
    * [yfinance.Ticker.get_revenue_estimate](yfinance.Ticker.get_revenue_estimate.html)
    * [yfinance.Ticker.revenue_estimate](yfinance.Ticker.revenue_estimate.html)
    * [yfinance.Ticker.get_earnings_history](yfinance.Ticker.get_earnings_history.html)
    * [yfinance.Ticker.earnings_history](yfinance.Ticker.earnings_history.html)
    * [yfinance.Ticker.get_eps_trend](yfinance.Ticker.get_eps_trend.html)
    * [yfinance.Ticker.eps_trend](yfinance.Ticker.eps_trend.html)
    * [yfinance.Ticker.get_eps_revisions](yfinance.Ticker.get_eps_revisions.html)
    * [yfinance.Ticker.eps_revisions](yfinance.Ticker.eps_revisions.html)
    * [yfinance.Ticker.get_growth_estimates](yfinance.Ticker.get_growth_estimates.html)
    * [yfinance.Ticker.growth_estimates](yfinance.Ticker.growth_estimates.html)
    * [yfinance.Ticker.get_funds_data](yfinance.Ticker.get_funds_data.html)
    * [yfinance.Ticker.funds_data](yfinance.Ticker.funds_data.html)
    * [yfinance.Ticker.get_insider_purchases](yfinance.Ticker.get_insider_purchases.html)
    * [yfinance.Ticker.insider_purchases](yfinance.Ticker.insider_purchases.html)
    * [yfinance.Ticker.get_insider_transactions](yfinance.Ticker.get_insider_transactions.html)
    * [yfinance.Ticker.insider_transactions](yfinance.Ticker.insider_transactions.html)
    * [yfinance.Ticker.get_insider_roster_holders](yfinance.Ticker.get_insider_roster_holders.html)
    * [yfinance.Ticker.insider_roster_holders](yfinance.Ticker.insider_roster_holders.html)
    * [yfinance.Ticker.get_major_holders](yfinance.Ticker.get_major_holders.html)
    * [yfinance.Ticker.major_holders](yfinance.Ticker.major_holders.html)
    * [yfinance.Ticker.get_institutional_holders](yfinance.Ticker.get_institutional_holders.html)
    * [yfinance.Ticker.institutional_holders](yfinance.Ticker.institutional_holders.html)
    * [yfinance.Ticker.get_mutualfund_holders](yfinance.Ticker.get_mutualfund_holders.html)
    * [yfinance.Ticker.mutualfund_holders](yfinance.Ticker.mutualfund_holders.html)
  * [Search & News](../yfinance.search.html) __
    * [Search](yfinance.Search.html)
  * [Sector and Industry](../yfinance.sector_industry.html) __
    * [Sector](yfinance.Sector.html)
    * [Industry](yfinance.Industry.html)
  * [Functions and Utilities](../yfinance.functions.html) __
    * [yfinance.download](yfinance.download.html)
    * [EquityQuery](yfinance.EquityQuery.html)
    * [Screener](yfinance.Screener.html)
    * [yfinance.enable_debug_mode](yfinance.enable_debug_mode.html)
    * yfinance.set_tz_cache_location
  * [FundsData class](../yfinance.funds_data.html) __
    * [FundsData](yfinance.scrapers.funds.FundsData.html)
  * [PriceHistory class](../yfinance.price_history.html)

  * [ __](../../index.html)
  * [API Reference](../index.html)
  * [Functions and Utilities](../yfinance.functions.html)
  * yfinance.set...

# yfinance.set_tz_cache_location#

yfinance.set_tz_cache_location(_cache_dir : str_)#

[ __ previous yfinance.enable_debug_mode ](yfinance.enable_debug_mode.html "previous page") [ next FundsData class __](../yfinance.funds_data.html "next page")

__On this page

  * `set_tz_cache_location()`

[ __Show Source](../../_sources/reference/api/yfinance.set_tz_cache_location.rst.txt)

© Copyright 2017-2019 Ran Aroussi.   

Created using [Sphinx](https://www.sphinx-doc.org/) 8.0.2.   

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

---

