import telebot
import requests
import time


TOKEN = "yourbot token"
CHANNEL_ID = "@your_channel_id"
Base_URL = "https://api.kucoin.com"
bot = telebot.TeleBot(TOKEN)

bot.send_message(CHANNEL_ID,f"bot has been updated🤑")

while True:
    try:
        params={'symbol':'BTC-USDT'}
        response=requests.get(Base_URL + "/api/v1/market/orderbook/level1",params=params)
        price=response.json()['data']['price']
        bot.send_message(CHANNEL_ID,f"BTC price: {price}💲")
        print('i send the price into the channel')
    except Exception as e:
        print('error', e)

    time.sleep(10)
