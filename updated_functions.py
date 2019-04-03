class Stocks:
    def __init__(self, ticker):
        self.ticker = ticker

    def _get_field(self, endpoint, field):
        data = getattr(self, "get_%s" % endpoint)(filter_=field)
        if self.output_format == 'json':
            if self.n_symbols == 1:
                data = data[field]
            else:
                data = {symbol: data[symbol][field] for symbol in self.symbols}
        return data

    def get_company_name(self):
        return self._get_field("quote", "companyName")