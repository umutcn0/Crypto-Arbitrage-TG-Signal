import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
from collections import OrderedDict
import traceback
import sys
import telebot
from datetime import datetime, timedelta
#09.06.2021 21:50 Güncelleme

Bot_Token = "1712159334:AAGwq25dFU_YjbVG9fuiM_6DwV16oG1JEX8"
Chat_ID = "-558315860"
TradeBot = telebot.TeleBot(Bot_Token)

def SendToTelegram(message):
    requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendMessage?chat_id=" + Chat_ID + "&text=" + message)

coins = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOGEUSDT", "XRPUSDT", "DOTUSDT", "UNIUSDT", "ICPUSDT", "BCHUSDT",
         "LINKUSDT", "LTCUSDT", "MATICUSDT", "SOLUSDT", "XLMUSDT", "THETAUSDT", "VETUSDT", "BTCUSDT", "ETCUSDT",
         "WBTCUSDT", "FILUSDT", "EOSUSDT", "TRXUSDT", "XMRUSDT", "DAIUSDT", "AAVEUSDT", "NEOUSDT", "MKRUSDT", "KSMUSDT",
         "SHIBUSDT", "CAKEUSDT", "KLAYUSDT", "FTTUSDT", "BSVUSDT", "ATOMUSDT", "ALGOUSDT", "HTUSDT", "BTTUSDT", "LUNAUSDT",
         "XTZUSDT", "AVAXUSDT", "COMPUSDT", "HBARUSDT", "DASHUSDT", "ZECUSDT", "DCRUSDT", "CELUSDT", "EGLDUSDT",
         "XEMUSDT", "CHZUSDT", "YFIUSDT", "SUSHIUSDT", "HOTUSDT", "WAVESUSDT", "ZILUSDT", "SNXUSDT", "MANAUSDT",
         "NEARUSDT", "ENJUSDT", "STXUSDT", "PAXUSDT", "ZENUSDT", "BATUSDT", "QTUMUSDT", "NANOUSDT", "MDXUSDT", "BTGUSDT",
         "REVUSDT", "GRTUSDT", "ONEUSDT", "UMAUSDT", "DGBUSDT", "ONTUSDT", "CRVUSDT", "BNTUSDT", "ZRXUSDT", "SCUSDT",
         "OMGUSDT", "FTMUSDT", "CELOUSDT", "ICXUSDT", "RVNUSDT", "ANKRUSDT", "KCSUSDT", "FLOWUSDT", "LPTUSDT",
         "1INCHUSDT", "RENUSDT", "XVGUSDT", "IOSTUSDT", "ARUSDT", "WRXUSDT", "CKBUSDT", "RSRUSDT", "LSKUSDT",
         "KNCUSDT", "LRCUSDT", "WINUSDT", "RLCUSDT", "RENUSDT", "SKLUSDT", "CFXUSDT", "SNTUSDT", "KAVAUSDT",
         "OCEANUSDT", "STORJUSDT", "GLMUSDT", "REEFUSDT", "OGNUSDT", "BTCSTUSDT", "NUUSDT", "SUNUSDT", "REPUSDT",
         "CTSIUSDT", "INJUSDT", "WAXPUSDT", "NKNUSDT", "IOTXUSDT", "CELRUSDT", "ALPHAUSDT", "SRMUSDT", "SANDUSDT",
         "NMRUSDT", "OXTUSDT", "CVCUSDT", "STEEMUSDT", "BALUSDT", "SXPUSDT", "KMDUSDT", "ORBSUSDT", "DODOUSDT", "MLNUSDT",
         "ANTUSDT", "CSPRUSDT", "HIVEUSDT", "BANDUSDT", "ZKSUSDT", "BTSUSDT", "PHAUSDT", "JSTUSDT", "UTKUSDT", "COTIUSDT",
         "BADGERUSDT", "AVAUSDT", "PUNDIXUSDT", "MIRUSDT", "AXSUSDT", "ORNUSDT", "LINAUSDT", "FORTHUSDT", "TOMOUSDT"]

driver = webdriver.Chrome()
while True:
    now = datetime.now()
    now = now + timedelta(hours=3)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    SendToTelegram(f"--Bot Active-- \nTime : {dt_string}")
    for coin in coins:
        try:


            url = f"https://tr.tradingview.com/symbols/{coin}/markets/"
            driver.get(url)
            time.sleep(5)
            liste = {}

            htmlSource = driver.page_source
            soup = BeautifulSoup(htmlSource, "html.parser")
            doviz_deger = soup.find_all("tr","tv-data-table__row tv-data-table__stroke tv-screener-table__result-row tv-screener-table__result-row--focused cursor")

            say = 0
            for i in doviz_deger:
                i = i.text
                veri = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', i)
                veri_say = 0
                for i in veri:
                    if i == None:
                        veri.pop(veri_say)
                    veri_say += 1
                for j in veri[:-1]:
                    if j == "KuCoin" or j == "Huobi" or j == "Bittrex" or j == "Poloniex" or j == "OKex" or j == "Coinbase" or j == "Binance":
                        key = j
                        value = veri[(say + 1)]
                        liste[key] = float(value)
                    say += 1
            d_sorted_by_value = OrderedDict(sorted(liste.items(), key=lambda x: x[1]))
            borsa_list = list(d_sorted_by_value.keys())
            borsa_list = borsa_list[:-1]
            value_list = list(d_sorted_by_value.values())
            value_list = value_list[:-1]
            """print(borsa_list)
            print(value_list)
            print(d_sorted_by_value,"\n")"""
            deger = (((value_list[-1]/value_list[0])*100)-100)
            if value_list[0]*1.02 < value_list[-1]:
                message = f"*ARBİTRAGE* \nCoin: {coin} \nBuy:{borsa_list[0]} - {value_list[0]} \nSell:{borsa_list[-1]} - {value_list[-1]} \nMarj:{deger}"
                SendToTelegram(message)
                print(message)
        except:
            traceback.print_exception(*sys.exc_info())
            pass

    message= "Scan Completed"
    SendToTelegram(message)
    time.sleep(5600)


