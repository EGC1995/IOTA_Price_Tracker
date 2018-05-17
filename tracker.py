import requests


function_string = "DIGITAL_CURRENCY_INTRADAY"
symbol = "IOTA"
market = "EUR"
api_key = "S1HJY4RZECSBCBEO"
metadata = None

intraday_data = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=IOTA&market=EUR&apikey=S1HJY4RZECSBCBEO")
intraday_data = intraday_data.json()
array_data = intraday_data["Time Series (Digital Currency Intraday)"]
print(array_data)
