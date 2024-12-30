# https://api.simplywall.st/docs/

![](images/logo.png)

Ã Close menu

#### Introduction

  * Welcome
  * Get API Access
  * Example #1: Find Tesla's UUID for future usage.
  * Example #2: Get Basic Company Information
  * Example #3: Get Basic Company Information via ticker symbol and exchange
  * Example #4: List Exchanges Supported
  * Example #5: Get Companies by Exchange



#### Operations

  * #####  Queries

    * companies
    * company
    * companyByExchangeAndTickerSymbol
    * exchanges
    * searchCompanies
  *   * 


#### Types

  * Boolean
  * ClassificationStatus
  * Company
  * DateTime
  * Exchange
  * Float
  * ID
  * Industry
  * InsiderTransaction
  * Int
  * JSONObject
  * Market
  * Member
  * Owner
  * OwnerType
  * Statement
  * StatementArea
  * StatementSeverity
  * StatementType
  * String
  * TransactionType



All topics

# Simply Wall St - Pro API Reference

Welcome to the SimplyWallSt Pro API documentation!

You can use our API to retrieve company data, historical, pricing information, company insights and more.

This documentation is designed to help you get started with our API and to provide you with all the information you need about the operations and types we support.

If you have any questions, please submit a _Pro API / Developer_ [support ticket](https://support.simplywall.st/hc/en-us/requests/new) or leave us [feedback](https://investor-research.typeform.com/to/DSd3LSrh).

Note: this in early access mode, meaning we reserve the right to make changes, have outages, etc... and we make no guarantees on service availabilty or accuracy whilst in this phase.

##### API Endpoints
    
    
    https://api.simplywall.st/graphql

## Get API Access

  1. Register via our [Beta Lab](https://simplywall.st/user/beta-lab) to our Pro Offering Early-Access Program (EAP)
  2. Receive a welcome invitation via email to our Pro Offering
  3. Create an API key at <https://simplywall.st/user/pro>



## Example #1: Find Tesla's UUID for future usage.

Search for companies using 'tesla' as the query.

_* Note: Replace`<pro-api-token>` with your own generated API key_
    
    
    curl --location 'https://api.simplywall.st/graphql' \
    --header 'Authorization: Bearer <pro-api-token>' \
    --header 'Content-Type: application/json' \
    --data '{"query":"query searchCompanies($query: String!) {searchCompanies(query: $query) {id,name,exchangeSymbol,tickerSymbol}}","variables":{"query":"tesla"}}'
    

## Example #2: Get Basic Company Information

Once you have retrieved the UUID of a company from the example above, you can use it to perform a query to retrieve basic company information about tesla
    
    
    curl --location 'https://api.simplywall.st/graphql' \
    --header 'Authorization: Bearer <pro-api-token>' \
    --header 'Content-Type: application/json' \
    --data '{"query":"query Query($id: ID!) {company (id: $id) {id,name,tickerSymbol}}","variables":{"id":"65dce5ea-70d6-417f-9cac-1eaa92fb7f1c"}}'
    

## Example #3: Get Basic Company Information via ticker symbol and exchange

Another option is to retriev the company information about tesla via ticker symbol and exchange. Remember that ticker symbols might change.
    
    
    curl --location 'https://api.simplywall.st/graphql' \
    --header 'Authorization: Bearer <pro-api-token>' \
    --header 'Content-Type: application/json' \
    --data '{"query":"query companyByExchangeAndTickerSymbol($exchange: String!,$symbol:String!) {\n  companyByExchangeAndTickerSymbol(exchange: $exchange,tickerSymbol:$symbol) {id,name,exchangeSymbol,tickerSymbol}\n}\n","variables":{"exchange":"NasdaqGS","symbol":"TSLA"}}'
    

## Example #4: List Exchanges Supported

Get a list of exchanges.
    
    
    curl --location 'https://api.simplywall.st/graphql' \
    --header 'Authorization: Bearer <pro-api-token>' \
    --header 'Content-Type: application/json' \
    --data '{"query":"query {exchanges {symbol}}","variables":{}}'
    

## Example #5: Get Companies by Exchange

Get a paginated list of ASX companies, showing 10 results per page, offset by the 2nd page.
    
    
    curl --location 'https://api.simplywall.st/graphql' \
    --header 'Authorization: Bearer <pro-api-token>' \
    --header 'Content-Type: application/json' \
    --data '{"query":"query {companies(exchange: \"ASX\", limit: 10, offset: 2) {id,name,tickerSymbol}}","variables":{}}'
    

# Queries

##  `companies`

##### Response

Returns `[Company!]!`

##### Arguments

Name | Description  
---|---  
`exchange` \- `String!` |  The exchange to select companies from   
`offset` \- `Int!` |  Offset to select companies from. Default = `0`  
`limit` \- `Int!` |  Total amount of companies to select. Default = `100`  
  
#### Example

##### Query
    
    
    query Companies(
      $exchange: String!,
      $offset: Int!,
      $limit: Int!
    ) {
      companies(
        exchange: $exchange,
        offset: $offset,
        limit: $limit
      ) {
        id
        exchangeSymbol
        tickerSymbol
        name
        marketCapUSD
        primaryIndustry {
          name
        }
        secondaryIndustry {
          name
        }
        tertiaryIndustry {
          name
        }
        market {
          name
          iso2
        }
        closingPrices
        statements {
          name
          title
          area
          type
          value
          outcome
          description
          state
          severity
          outcomeName
        }
        listings {
          id
          exchangeSymbol
          tickerSymbol
          name
          marketCapUSD
          primaryIndustry {
            ...IndustryFragment
          }
          secondaryIndustry {
            ...IndustryFragment
          }
          tertiaryIndustry {
            ...IndustryFragment
          }
          market {
            ...MarketFragment
          }
          closingPrices
          statements {
            ...StatementFragment
          }
          listings {
            ...CompanyFragment
          }
          owners {
            ...OwnerFragment
          }
          insiderTransactions {
            ...InsiderTransactionFragment
          }
          members {
            ...MemberFragment
          }
          active
          classificationStatus
        }
        owners {
          name
          type
          sharesHeld
          percentOfSharesOutstanding
          holdingDate
          periodStartDate
          periodEndDate
          rankSharesHeld
          rankSharesSold
        }
        insiderTransactions {
          type
          ownerName
          ownerType
          description
          tradeDateMin
          tradeDateMax
          shares
          priceMin
          priceMax
          transactionValue
          percentageSharesTraded
          percentageChangeTransShares
          isManagementInsider
          filingDate
        }
        members {
          age
          name
          title
          tenure
          compensation
        }
        active
        classificationStatus
      }
    }
    

##### Variables
    
    
    {
      "exchange": "abc123",
      "offset": 0,
      "limit": 100
    }
    

##### Response
    
    
    {
      "data": {
        "companies": [
          {
            "id": 4,
            "exchangeSymbol": "xyz789",
            "tickerSymbol": "abc123",
            "name": "xyz789",
            "marketCapUSD": 123.45,
            "primaryIndustry": Industry,
            "secondaryIndustry": Industry,
            "tertiaryIndustry": Industry,
            "market": Market,
            "closingPrices": {},
            "statements": [Statement],
            "listings": [Company],
            "owners": [Owner],
            "insiderTransactions": [InsiderTransaction],
            "members": [Member],
            "active": false,
            "classificationStatus": "ACTIVE"
          }
        ]
      }
    }
    

Queries

##  `company`

##### Description

A representation of a legal entity engaged in operating a business.

##### Response

Returns a `Company!`

##### Arguments

Name | Description  
---|---  
`id` \- `ID!` |  The company UUID. This will remain constant throughout the lifetime of the company even if it changes ticker symbols.   
  
#### Example

##### Query
    
    
    query Company($id: ID!) {
      company(id: $id) {
        id
        exchangeSymbol
        tickerSymbol
        name
        marketCapUSD
        primaryIndustry {
          name
        }
        secondaryIndustry {
          name
        }
        tertiaryIndustry {
          name
        }
        market {
          name
          iso2
        }
        closingPrices
        statements {
          name
          title
          area
          type
          value
          outcome
          description
          state
          severity
          outcomeName
        }
        listings {
          id
          exchangeSymbol
          tickerSymbol
          name
          marketCapUSD
          primaryIndustry {
            ...IndustryFragment
          }
          secondaryIndustry {
            ...IndustryFragment
          }
          tertiaryIndustry {
            ...IndustryFragment
          }
          market {
            ...MarketFragment
          }
          closingPrices
          statements {
            ...StatementFragment
          }
          listings {
            ...CompanyFragment
          }
          owners {
            ...OwnerFragment
          }
          insiderTransactions {
            ...InsiderTransactionFragment
          }
          members {
            ...MemberFragment
          }
          active
          classificationStatus
        }
        owners {
          name
          type
          sharesHeld
          percentOfSharesOutstanding
          holdingDate
          periodStartDate
          periodEndDate
          rankSharesHeld
          rankSharesSold
        }
        insiderTransactions {
          type
          ownerName
          ownerType
          description
          tradeDateMin
          tradeDateMax
          shares
          priceMin
          priceMax
          transactionValue
          percentageSharesTraded
          percentageChangeTransShares
          isManagementInsider
          filingDate
        }
        members {
          age
          name
          title
          tenure
          compensation
        }
        active
        classificationStatus
      }
    }
    

##### Variables
    
    
    {"id": 4}
    

##### Response
    
    
    {
      "data": {
        "company": {
          "id": 4,
          "exchangeSymbol": "abc123",
          "tickerSymbol": "abc123",
          "name": "abc123",
          "marketCapUSD": 987.65,
          "primaryIndustry": Industry,
          "secondaryIndustry": Industry,
          "tertiaryIndustry": Industry,
          "market": Market,
          "closingPrices": {},
          "statements": [Statement],
          "listings": [Company],
          "owners": [Owner],
          "insiderTransactions": [InsiderTransaction],
          "members": [Member],
          "active": true,
          "classificationStatus": "ACTIVE"
        }
      }
    }
    

Queries

##  `companyByExchangeAndTickerSymbol`

##### Description

A representation of a legal entity engaged in operating a business.

##### Response

Returns a `Company!`

##### Arguments

Name | Description  
---|---  
`exchange` \- `String!` |  The exchange of the company.   
`tickerSymbol` \- `String!` |  The ticker symbol of the company.   
  
#### Example

##### Query
    
    
    query CompanyByExchangeAndTickerSymbol(
      $exchange: String!,
      $tickerSymbol: String!
    ) {
      companyByExchangeAndTickerSymbol(
        exchange: $exchange,
        tickerSymbol: $tickerSymbol
      ) {
        id
        exchangeSymbol
        tickerSymbol
        name
        marketCapUSD
        primaryIndustry {
          name
        }
        secondaryIndustry {
          name
        }
        tertiaryIndustry {
          name
        }
        market {
          name
          iso2
        }
        closingPrices
        statements {
          name
          title
          area
          type
          value
          outcome
          description
          state
          severity
          outcomeName
        }
        listings {
          id
          exchangeSymbol
          tickerSymbol
          name
          marketCapUSD
          primaryIndustry {
            ...IndustryFragment
          }
          secondaryIndustry {
            ...IndustryFragment
          }
          tertiaryIndustry {
            ...IndustryFragment
          }
          market {
            ...MarketFragment
          }
          closingPrices
          statements {
            ...StatementFragment
          }
          listings {
            ...CompanyFragment
          }
          owners {
            ...OwnerFragment
          }
          insiderTransactions {
            ...InsiderTransactionFragment
          }
          members {
            ...MemberFragment
          }
          active
          classificationStatus
        }
        owners {
          name
          type
          sharesHeld
          percentOfSharesOutstanding
          holdingDate
          periodStartDate
          periodEndDate
          rankSharesHeld
          rankSharesSold
        }
        insiderTransactions {
          type
          ownerName
          ownerType
          description
          tradeDateMin
          tradeDateMax
          shares
          priceMin
          priceMax
          transactionValue
          percentageSharesTraded
          percentageChangeTransShares
          isManagementInsider
          filingDate
        }
        members {
          age
          name
          title
          tenure
          compensation
        }
        active
        classificationStatus
      }
    }
    

##### Variables
    
    
    {
      "exchange": "xyz789",
      "tickerSymbol": "abc123"
    }
    

##### Response
    
    
    {
      "data": {
        "companyByExchangeAndTickerSymbol": {
          "id": "4",
          "exchangeSymbol": "xyz789",
          "tickerSymbol": "abc123",
          "name": "xyz789",
          "marketCapUSD": 123.45,
          "primaryIndustry": Industry,
          "secondaryIndustry": Industry,
          "tertiaryIndustry": Industry,
          "market": Market,
          "closingPrices": {},
          "statements": [Statement],
          "listings": [Company],
          "owners": [Owner],
          "insiderTransactions": [InsiderTransaction],
          "members": [Member],
          "active": false,
          "classificationStatus": "ACTIVE"
        }
      }
    }
    

Queries

##  `exchanges`

##### Response

Returns `[Exchange!]!`

#### Example

##### Query
    
    
    query Exchanges {
      exchanges {
        symbol
        companiesCount
      }
    }
    

##### Response
    
    
    {
      "data": {
        "exchanges": [
          {
            "symbol": "xyz789",
            "companiesCount": 987
          }
        ]
      }
    }
    

Queries

##  `searchCompanies`

##### Description

Searches for companies using an input query.

##### Response

Returns `[Company!]!`

##### Arguments

Name | Description  
---|---  
`query` \- `String!` |  The search query.   
  
#### Example

##### Query
    
    
    query SearchCompanies($query: String!) {
      searchCompanies(query: $query) {
        id
        exchangeSymbol
        tickerSymbol
        name
        marketCapUSD
        primaryIndustry {
          name
        }
        secondaryIndustry {
          name
        }
        tertiaryIndustry {
          name
        }
        market {
          name
          iso2
        }
        closingPrices
        statements {
          name
          title
          area
          type
          value
          outcome
          description
          state
          severity
          outcomeName
        }
        listings {
          id
          exchangeSymbol
          tickerSymbol
          name
          marketCapUSD
          primaryIndustry {
            ...IndustryFragment
          }
          secondaryIndustry {
            ...IndustryFragment
          }
          tertiaryIndustry {
            ...IndustryFragment
          }
          market {
            ...MarketFragment
          }
          closingPrices
          statements {
            ...StatementFragment
          }
          listings {
            ...CompanyFragment
          }
          owners {
            ...OwnerFragment
          }
          insiderTransactions {
            ...InsiderTransactionFragment
          }
          members {
            ...MemberFragment
          }
          active
          classificationStatus
        }
        owners {
          name
          type
          sharesHeld
          percentOfSharesOutstanding
          holdingDate
          periodStartDate
          periodEndDate
          rankSharesHeld
          rankSharesSold
        }
        insiderTransactions {
          type
          ownerName
          ownerType
          description
          tradeDateMin
          tradeDateMax
          shares
          priceMin
          priceMax
          transactionValue
          percentageSharesTraded
          percentageChangeTransShares
          isManagementInsider
          filingDate
        }
        members {
          age
          name
          title
          tenure
          compensation
        }
        active
        classificationStatus
      }
    }
    

##### Variables
    
    
    {"query": "abc123"}
    

##### Response
    
    
    {
      "data": {
        "searchCompanies": [
          {
            "id": "4",
            "exchangeSymbol": "abc123",
            "tickerSymbol": "abc123",
            "name": "abc123",
            "marketCapUSD": 987.65,
            "primaryIndustry": Industry,
            "secondaryIndustry": Industry,
            "tertiaryIndustry": Industry,
            "market": Market,
            "closingPrices": {},
            "statements": [Statement],
            "listings": [Company],
            "owners": [Owner],
            "insiderTransactions": [InsiderTransaction],
            "members": [Member],
            "active": false,
            "classificationStatus": "ACTIVE"
          }
        ]
      }
    }
    

# Types

## Boolean

##### Description

The `Boolean` scalar type represents `true` or `false`.

##### Example
    
    
    true
    

Types

## ClassificationStatus

##### Values

Enum Value | Description  
---|---  
`ACTIVE` |   
`ACTIVE_NOT_TRADING` |   
`UNKNOWN` |   
`MERGED` |   
`INACTIVE` |   
  
##### Example
    
    
    "ACTIVE"
    

Types

## Company

##### Description

A representation of a legal entity engaged in operating a business.

##### Fields

Field Name | Description  
---|---  
`id` \- `ID!` |  The UUID of a company. This will remain constant throughout the lifetime of the company even if it changes ticker symbols. Use this value to perform lookups on a company.   
`exchangeSymbol` \- `String!` |  A short abbreviation used to uniquely identify publicly traded shares of a particular stock on a particular stock market   
`tickerSymbol` \- `String!` |  A unique series of letters assigned to a security for trading purposes   
`name` \- `String!` |  Name of company   
`marketCapUSD` \- `Float!` |  Total market cap value represented in US dollars   
`primaryIndustry` \- `Industry` |  Primary tier industry classification   
`secondaryIndustry` \- `Industry` |  Secondary tier industry classification   
`tertiaryIndustry` \- `Industry` |  Tertiary tier industry classification   
`market` \- `Market!` |  The market where parties can engage in economic transactions   
`closingPrices` \- `JSONObject!` |  A historical collection of the last price traded during a regular trading session   
`statements` \- `[Statement!]!` |  A collection of evaluated opinions about a company   
  
#####  Arguments 

###### `types` \- `[StatementType!]`  
  
`listings` \- `[Company!]!` |  A listing for a company whose shares are bought and sold to the public through a stock exchange   
`owners` \- `[Owner!]!` |   
`insiderTransactions` \- `[InsiderTransaction!]!` |   
`members` \- `[Member!]!` |   
`active` \- `Boolean!` |  Whether or not this listing is active.   
`classificationStatus` \- `ClassificationStatus!` |  The classification status of the listing.   
  
##### Example
    
    
    {
      "id": "4",
      "exchangeSymbol": "abc123",
      "tickerSymbol": "abc123",
      "name": "abc123",
      "marketCapUSD": 987.65,
      "primaryIndustry": Industry,
      "secondaryIndustry": Industry,
      "tertiaryIndustry": Industry,
      "market": Market,
      "closingPrices": {},
      "statements": [Statement],
      "listings": [Company],
      "owners": [Owner],
      "insiderTransactions": [InsiderTransaction],
      "members": [Member],
      "active": true,
      "classificationStatus": "ACTIVE"
    }
    

Types

## DateTime

##### Description

A date-time string at UTC, such as 2019-12-03T09:54:33Z, compliant with the date-time format.

##### Example
    
    
    "2007-12-03T10:15:30Z"
    

Types

## Exchange

##### Fields

Field Name | Description  
---|---  
`symbol` \- `String!` |   
`companiesCount` \- `Int!` |   
  
##### Example
    
    
    {"symbol": "xyz789", "companiesCount": 987}
    

Types

## Float

##### Description

The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

##### Example
    
    
    123.45
    

Types

## ID

##### Description

The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

##### Example
    
    
    4
    

Types

## Industry

##### Description

Group of companies that are related based on their primary business activities.

##### Fields

Field Name | Description  
---|---  
`name` \- `String!` |   
  
##### Example
    
    
    {"name": "xyz789"}
    

Types

## InsiderTransaction

##### Description

A transaction that represents a trade of stocks and securities based on non-public insider information.

##### Fields

Field Name | Description  
---|---  
`type` \- `TransactionType!` |  Determines if the transaction is a BUY or SELL type   
`ownerName` \- `String!` |  Name of transaction owner   
`ownerType` \- `OwnerType!` |  Type of owner. Can be an `Individual` or `Company`  
`description` \- `String!` |  Description of the insider transaction   
`tradeDateMin` \- `DateTime` |  First trade date   
`tradeDateMax` \- `DateTime` |  Last trade date   
`shares` \- `Float!` |  Number of shares   
`priceMin` \- `Float!` |  The minimum price traded   
`priceMax` \- `Float!` |  The maximum price traded   
`transactionValue` \- `Float!` |  Total transaction value   
`percentageSharesTraded` \- `Float` |  Percentage of owner shares traded   
`percentageChangeTransShares` \- `Float` |  Percentage changed when transacting shares   
`isManagementInsider` \- `Boolean!` |  Flag to signify if the owner is a management member   
`filingDate` \- `DateTime` |  Date when the transaction was filed   
  
##### Example
    
    
    {
      "type": "BUY",
      "ownerName": "abc123",
      "ownerType": "INDIVIDUAL",
      "description": "xyz789",
      "tradeDateMin": "2007-12-03T10:15:30Z",
      "tradeDateMax": "2007-12-03T10:15:30Z",
      "shares": 987.65,
      "priceMin": 123.45,
      "priceMax": 123.45,
      "transactionValue": 987.65,
      "percentageSharesTraded": 123.45,
      "percentageChangeTransShares": 987.65,
      "isManagementInsider": true,
      "filingDate": "2007-12-03T10:15:30Z"
    }
    

Types

## Int

##### Description

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

##### Example
    
    
    123
    

Types

## JSONObject

##### Description

The `JSONObject` scalar type represents JSON objects as specified by [ECMA-404](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf).

##### Example
    
    
    {}
    

Types

## Market

##### Description

The market where parties can engage in economic transactions

##### Fields

Field Name | Description  
---|---  
`name` \- `String!` |  Name of the market   
`iso2` \- `String!` |  Country of the market in ISO alpha-2 format   
  
##### Example
    
    
    {
      "name": "abc123",
      "iso2": "xyz789"
    }
    

Types

## Member

##### Description

A member of the board.

##### Fields

Field Name | Description  
---|---  
`age` \- `Int` |  Age of member   
`name` \- `String!` |  Name of member   
`title` \- `String` |  Title of member   
`tenure` \- `Float` |  Number of years member has been on the board   
`compensation` \- `Float` |  Total compensation value in the currency of exchange where the company is listed.   
  
##### Example
    
    
    {
      "age": 987,
      "name": "xyz789",
      "title": "abc123",
      "tenure": 987.65,
      "compensation": 987.65
    }
    

Types

## Owner

##### Description

An `Individual` or `Company` that owns outstanding shares of the company.

##### Fields

Field Name | Description  
---|---  
`name` \- `String!` |  Name of the owner   
`type` \- `OwnerType!` |  Type of owner. This can be an `Individual` or `Company`  
`sharesHeld` \- `Float!` |  Number of shares held   
`percentOfSharesOutstanding` \- `Float!` |  Ownership represented in percantage   
`holdingDate` \- `DateTime` |  Date when the holdings were traded   
`periodStartDate` \- `DateTime` |  Date when holdings were held   
`periodEndDate` \- `DateTime` |  Date when holdings ceased to be held   
`rankSharesHeld` \- `Float` |  Order of rank for the number of shares held, compared to other top shareholders   
`rankSharesSold` \- `Float` |  Order of rank for the number of shares sold, compared to other top shareholders   
  
##### Example
    
    
    {
      "name": "abc123",
      "type": "INDIVIDUAL",
      "sharesHeld": 987.65,
      "percentOfSharesOutstanding": 987.65,
      "holdingDate": "2007-12-03T10:15:30Z",
      "periodStartDate": "2007-12-03T10:15:30Z",
      "periodEndDate": "2007-12-03T10:15:30Z",
      "rankSharesHeld": 123.45,
      "rankSharesSold": 123.45
    }
    

Types

## OwnerType

##### Description

Type of owner. This can be an `Individual` or `Company`

##### Values

Enum Value | Description  
---|---  
`INDIVIDUAL` |   
`COMPANY` |   
  
##### Example
    
    
    "INDIVIDUAL"
    

Types

## Statement

##### Description

An evaluated opinion about a company.

##### Fields

Field Name | Description  
---|---  
`name` \- `String!` |  Unique identifying name of the statement   
`title` \- `String!` |  Title of statement   
`area` \- `StatementArea!` |  Represents a specific area or focal point of a company being evaluated.   
`type` \- `StatementType!` |  Represents specific behavioural traits about a statement. For example, the results of a `RISKS` statement translates to a different outcome compared to a `REWARDS` statement   
`value` \- `Boolean` |  The evaluation outcome   
`outcome` \- `Int!` |  A number that represents a contextualised evaluation outcome. It extends the "value" field as it is possible to have more than one variant of an evaluation outcome.   
`description` \- `String` |  Provides a description of the statement being evaluated   
`state` \- `String` |  Specific to `RISKS` and `REWARDS` `StatementType`, these represent whether their outcomes pass as a risky or rewardful outcome   
`severity` \- `StatementSeverity` |  Specific to `RISKS` and `REWARDS` `StatementType`, this value represents the degree of the outcome   
`outcomeName` \- `String!` |  Represents a specific outcome of the evaluated value   
  
##### Example
    
    
    {
      "name": "xyz789",
      "title": "abc123",
      "area": "BANK_DIVIDENDS",
      "type": "RISKS",
      "value": false,
      "outcome": 987,
      "description": "xyz789",
      "state": "abc123",
      "severity": "MINOR",
      "outcomeName": "abc123"
    }
    

Types

## StatementArea

##### Description

Represents a specific area or focal point of a company being evaluated.

##### Values

Enum Value | Description  
---|---  
`BANK_DIVIDENDS` |   
`MISC` |   
`BANK_HEALTH` |   
`MARKET` |   
`DIVIDENDS` |   
`PAST` |   
`FUTURE` |   
`RISKS` |   
`HEALTH` |   
`REWARDS` |   
`MANAGEMENT` |   
`VALUE` |   
  
##### Example
    
    
    "BANK_DIVIDENDS"
    

Types

## StatementSeverity

##### Description

Specific to `RISKS` and `REWARDS` `StatementType`, and depending on the outcome, this value represents whether it is a minor or major risk/reward.

##### Values

Enum Value | Description  
---|---  
`MINOR` |   
`MAJOR` |   
  
##### Example
    
    
    "MINOR"
    

Types

## StatementType

##### Description

The type of statement being evaluated.

`RISKS` statements are checks that are more oriented towards the risky aspects of the company which can threaten the future existence of the business, cause investors to face unnecessary capital volatility, or offers lack of data which hinders informed decision making.

`REWARDS` statement checks are more oriented towards what investors should expect to get in the future, whether it is capital gains through capital appreciation as mispriced shares approach fair valuation (value) or the company becomes more valuable as it grows (future), or dividend income.

`STATEMENTS` are a catch-all evaluation of statements about a company.

##### Values

Enum Value | Description  
---|---  
`RISKS` |   
`REWARDS` |   
`STATEMENTS` |   
  
##### Example
    
    
    "RISKS"
    

Types

## String

##### Description

The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

##### Example
    
    
    "abc123"
    

Types

## TransactionType

##### Description

Determines if the transaction is a `BUY` or `SELL` type.

##### Values

Enum Value | Description  
---|---  
`BUY` |   
`SELL` |   
  
##### Example
    
    
    "BUY"
    
