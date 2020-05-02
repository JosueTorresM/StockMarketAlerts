import os
import requests
import json
import time
from iexfinance.stocks import Stock
from forex_python.converter import CurrencyRates
from datetime import datetime

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

RTCER_KEY = os.getenv('RTCER_KEY')

stock_list = ["AAPL","AXP"]
average_cost = {"AAPL":6000.00,
                "AXP":2200.00}

def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key): 
	base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
	main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
	req_ob = requests.get(main_url) 
	result = req_ob.json() 
	return float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage?chat_id=' + TELEGRAM_CHAT_ID + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)

def check_stocks(exchange_rate):
    for stock in stock_list:
        symbol = Stock(stock)
        mxn_average_cost = average_cost[stock]
        symbol_data = symbol.get_quote()
        usd_price = symbol_data["latestPrice"]
        mxn_price = usd_price * exchange_rate
        print(stock + ": " + str(usd_price) + " USD/ " + str("{:.2f}".format(mxn_price)) + " MXN")
        if mxn_price<mxn_average_cost:
            telegram_bot_sendtext(stock + ":" + 
                                    "\nCurrent price: " + str(usd_price) + " USD/ " + str("{:.2f}".format(mxn_price)) + " MXN" +
                                    "\nAverage cost: " + str(mxn_average_cost) + " MXN"
                                    )

if __name__ == "__main__":
    now = datetime.now()
    market_open_time = now.replace(hour=8, minute=30, second=0, microsecond=0)
    market_close_time = now.replace(hour=15, minute=0, second=0, microsecond=0)
    if now.weekday() < 5 and now > market_open_time and now < market_close_time:
        exchange_rate = RealTimeCurrencyExchangeRate("USD", "MXN", RTCER_KEY)
        check_stocks(exchange_rate)