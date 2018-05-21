import requests
import matplotlib.pyplot as plt
import numpy as np

function_string = "DIGITAL_CURRENCY_INTRADAY"
symbol = "IOTA"
market = "EUR"
api_key = "S1HJY4RZECSBCBEO"
metadata = None
price_key = "1b. price (USD)"
volume = "2. volume"
market_cap = "3. market cap (USD)"
array_time = []
array_price = []

intraday_data = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=IOTA&market=EUR&apikey=S1HJY4RZECSBCBEO")
intraday_data = intraday_data.json()
array_data = intraday_data["Time Series (Digital Currency Intraday)"]

for key in array_data:
    array_time.append(key)
    array_price.append(array_data[key][price_key])
    # print(key, array_data[key][price_key])

plt.figure(1)
plt.plot(array_time[:10], array_price[:10])
plt.title("IOTA Price")
plt.show()
