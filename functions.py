class Stocks:
    def company_name(ticker):
        return ticker["quote"]["companyName"]
    
    def close_price(ticker):
        close = ticker["quote"]["close"]
        return close

    def latest_price(ticker):
        latest_price = ticker["quote"]["latestPrice"]
        return latest_price

    def exchange(ticker):
        exchange = ticker["quote"]["primaryExchange"]
        return exchange
    
    def change_percentage(ticker):
        change = ticker["quote"]["changePercent"]
        return change
    
    def volume(ticker):
        volume = ticker["quote"]["latestVolume"]
        return volume

    def market_cap(ticker):
        market_cap = ticker["quote"]["marketCap"]
        return market_cap
    
    def week_52_h(ticker):
        week52H = ticker["quote"]["week52High"]
        return week52H

    def week_52_l(ticker):
        week52L = ticker["quote"]["week52Low"]
        return week52L

    def ytd_change(ticker):
        ytd_change = ticker["quote"]["ytdChange"]
        return ytd_change

    def industry(ticker):
        industry = ticker["company"]["industry"]
        return industry
    
    def sector(ticker):
        sector = ticker["company"]["sector"]
        return sector
    
    def website(ticker):
        website = ticker["company"]["website"]
        return website
    
    def ceo(ticker):
        ceo = ticker["company"]["CEO"]
        return ceo
    
    def description(ticker):
        description = ticker["company"]["description"]
        return description