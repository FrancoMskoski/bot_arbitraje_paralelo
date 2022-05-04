from multiprocessing import current_process
import Binance
import huobi 
import json 
# buscar los tikers de los diferentes exchange 
# Exchange = binance , huovi , etc
# ver di se puede arbitrar = ada/btc, ada/usdt, sol/btc, sol/usdt , btc/usdt 


def buy_binance_sell_huobi(cripto:str):
    precio_cripto_binance = float(Binance.tikers_de_binance[cripto]['bid'])
    precio_cripto_huobi = float(huobi.tikers_de_huobi[cripto.lower()]['ask'])
    buy_binance_sell_huobi = precio_cripto_binance / precio_cripto_huobi
    return(buy_binance_sell_huobi)

cripto = open("Tikers entre huobi y binance.json", "r") 
cadenajson = json.load(cripto)

for i in range (len(cadenajson['tikers'])):
    criptos = cadenajson['tikers'][i]
    divicines = (buy_binance_sell_huobi(criptos))
    if divicines > 1.0:
        print(criptos , divicines  )

#print("buy_price        exchange_buy        exchange_sell       pair        sell_price ")
