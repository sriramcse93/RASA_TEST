import stockquotes

def stockrate(name):
    stockname = stockquotes.Stock(name)
    print(stockname)
    stockprice = stockname.current_price
    print(stockprice)
    return (stockprice)