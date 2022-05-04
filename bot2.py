from multiprocessing import current_process
import Binance
import huobi 
import json 
# buscar los tikers de los diferentes exchange 
# Exchange = binance , huovi , etc
# ver di se puede arbitrar = ada/btc, ada/usdt, sol/btc, sol/usdt , btc/usdt 


def buy_binance_sell_huobi(cripto:str):
    result = []
    if float(Binance.tikers_de_binance[cripto]['bid']) > float(huobi.tikers_de_huobi[cripto.lower()]['ask']):
        best_sell = float(Binance.tikers_de_binance[cripto]['bid'])
        best_buy  = float(huobi.tikers_de_huobi[cripto.lower()]['ask'])
        try:    
                calculo = best_sell / best_buy
        except:
                calculo =  0.0 #por que no se encontro nada 
        result.append([calculo , " Buy Binance - Sell Huobi"])
    
    if float(huobi.tikers_de_huobi[cripto.lower()]['ask']) > float(Binance.tikers_de_binance[cripto]['bid']):
        best_sell2 = float(huobi.tikers_de_huobi[cripto.lower()]['ask'])
        best_buy2 = float(Binance.tikers_de_binance[cripto]['bid'])
        try:    
            calculo2 = best_sell2 / best_buy2
        except:
            calculo2 = 0.0 #por que no se encontro nada 
        result.append([calculo2 , " Buy Huobi - Sell Binance"])
    try:
        return(result[0])
    except:
        return("No se que puta paso xd ")
        

cripto = open("Tikers entre huobi y binance.json", "r") 
cadenajson = json.load(cripto)

for i in range (len(cadenajson['tikers'])):
    criptos = cadenajson['tikers'][i]
    divicines = (buy_binance_sell_huobi(criptos))
    if divicines != 'No se que puta paso xd ' :
        if divicines[0] > 1.1:
            print(criptos, "\n" , divicines  )

#print("buy_price        exchange_buy        exchange_sell       pair        sell_price ")
   