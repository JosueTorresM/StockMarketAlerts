# StockMarketAlerts
Use your Telegram account to get notified about stock market changes.

## Services used in the project
### Currency Exchange Rate
Since the information of stock options is only in USD, with this service you are able to get the lastest exchange rate.
Claim your [free API Key](https://www.alphavantage.co/support/#api-key).

### Telegram Bot
To get notified with Telegram messages you have to:
- [Create a bot account](https://medium.com/shibinco/create-a-telegram-bot-using-botfather-and-get-the-api-token-900ba00e0f39)
- [Obtain your chat id](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)

### Stock Options realtime information
[IEX Cloud](https://iexcloud.io/) provide an API to get stock option information in realtime. Not only Price but also alot of valuable information like Volume, Change, Market Cap, PER, etc.
Create your account and use your PUBLISHABLE token. I recomend to use first your testing API token using the Sandbox Testing option.

## Set up

To start using this, you have to create the following environment variables:

```
#IEXCloud token
export IEX_TOKEN="your-iex-token"

#Telegram bot token
export TELEGRAM_BOT_TOKEN="your-telegram-bot-token"

#Telegram chat id
export TELEGRAM_CHAT_ID="your-chat-id"

#RealTimeCurrencyExchangeRate
export RTCER_KEY="your-rtcer-key"
```
After this, set the variable **stock_list** with a list of symbols that you want to be getting notified. Then the variable **average_cost** alows you to put the average cost of your stock options.

If you want to see the information in your local currency, the variable **exchange_rate** has the latest exchange rate, if you want to see the information in **USD** just remove this step.

If the **latestPrice** is lower thant the **average_cost** a Telegram message will be sent with the detail, so you could go to your Broker Software and trade with them.