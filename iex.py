from functions import Stocks
import click
import json
import requests

# Retrieving stock_data from IEX API
def get_stock_data(ticker):
    # Enabling persistent HTTP connection
    live_response = requests.Session()
    # Passing ticker to get company information
    response = live_response.get(
    "https://api.iextrading.com/1.0/stock/" + ticker + "/batch?types=quote,company"
    )
    # Assigning JSON data to stock_data
    stock_data = json.loads(response.text)
    return stock_data


def get_info(stock_data):
    company_name = Stocks.company_name(stock_data)
    latest_price = Stocks.latest_price(stock_data)
    exchange = Stocks.exchange(stock_data)
    change = Stocks.change_percentage(stock_data)
    volume = Stocks.volume(stock_data)
    market_cap = Stocks.market_cap(stock_data)
    week_52_high = Stocks.week_52_h(stock_data)
    week_52_low = Stocks.week_52_l(stock_data)
    week_52_range = str(week_52_low) + " - " + str(week_52_high)
    ytd_change = Stocks.ytd_change(stock_data)
    industry = Stocks.industry(stock_data)
    sector = Stocks.sector(stock_data)
    website = Stocks.website(stock_data)
    ceo = Stocks.ceo(stock_data)
    description = Stocks.description(stock_data)
    dic = {
        "company_name": company_name,
        "latest_price": latest_price,
        "exchange": exchange,
        "change": change,
        "volume": volume,
        "market_cap": market_cap,
        "week_52_range": week_52_range,
        "ytd_change": ytd_change,
        "industry": industry,
        "sector": sector,
        "website": website,
        "ceo": ceo,
        "description": description
    }
    return dic


@click.group()
def cli():
    pass


@cli.command()
@click.argument("ticker")
def summary(ticker):
    try:
        stock_data = get_stock_data(ticker)
        company_info = get_info(stock_data)
        company_name = company_info["company_name"]
        latest_price = company_info["latest_price"]
        exchange = company_info["exchange"]
        change = company_info["change"]
        volume = company_info["volume"]
        market_cap = company_info["market_cap"]
        week_52_range = company_info["week_52_range"]
        ytd_change = company_info["ytd_change"]
        industry = company_info["industry"]
        sector = company_info["sector"]
        website = company_info["website"]
        ceo = company_info["ceo"]
        description = company_info["description"]
        print(
            f"\u001b[4m\u001b[1m{ticker.upper()} OVERVIEW\u001b[0m\u001b[0m",
            f"\n{'Price:':<15}{latest_price:>30}",
            f"\n{'Exchange:':<15}{exchange:>30}",
            f"\n{'Change:':<15}{change:>30.3f}",
            f"\n{'Volume:':<15}{volume:>30}",
            f"\n{'Market Cap:':<15}{market_cap:>30}",
            f"\n{'52 Week Range:':<15}{week_52_range:>30}",
            f"\n{'YTD Change:':<15}{ytd_change:>30.3f}",
            f"\n",
            f"\n\u001b[4m\u001b[1mCOMPANY INFO\u001b[0m\u001b[0m",    
            f"\n{'Company Name:':<15}{company_name:>30}",
            f"\n{'Industry:':<15}{industry:>30}",
            f"\n{'Sector:':<15}{sector:>30}",
            f"\n{'Website:':<15}{website:>30}",
            f"\n{'CEO:':<15}{ceo:>30}",
            f"\n",
            f"\n\u001b[4m\u001b[1mDESCRIPTION\u001b[0m\u001b[0m",
            f"\n{description:100}",            
        )
    except:
        print("Invalid ticker symbol, try again! (Usage: iex summary TICKER)")