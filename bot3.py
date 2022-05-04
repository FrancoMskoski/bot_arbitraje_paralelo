from multiprocessing import current_process
import binance
import huobi 
import json 
import MySql 
# buscar los tikers de los diferentes exchange 
# Exchange = binance , huovi , etc
# ver di se puede arbitrar = ada/btc, ada/usdt, sol/btc, sol/usdt , btc/usdt 


def best_buy_best_sell(cripto:str, comicionesBinance:float , comicionesHuibi:float ):
    #BINACNE
    price_binance_bid = [float(binance.tikers_info[cripto]['bid']) , "Binance"]
    price_binance_ask = [float(binance.tikers_info[cripto]['ask']) , "Binance"]
    #HUOBI
    price_huobi_bid   = [float(huobi.tikers_info[cripto]['bid']) , "Huobi"]
    price_huobi_ask   = [float(huobi.tikers_info[cripto]['ask']) , "Huobi"]
    #BUYS AND SELLS
    buys = [price_binance_ask , price_huobi_ask]    #tiene que ser el mas bajo
    sells= [price_binance_bid, price_huobi_bid]     #tiene que ser el mas alto 
    #BEST BUYS AND BEST SELLS
    best_buy  = buys[0]
    best_sell = sells[0]

    for i in range(len(buys)):
        if buys[i][0] < best_buy[0]:
            best_buy = buys[i]

    for i in range(len(sells)):
        if sells[i][0] > best_sell[0]:
            best_sell = sells[i] 
    #Calcular comicion

    if best_buy[1] == "Binance":
        best_buy_and_comicion = best_buy[0] * (1 + comicionesBinance)
    if best_buy[1] == "Huobi":
        best_buy_and_comicion = best_buy[0] * (1 + comicionesHuibi)

    if best_sell[1] == "Binance":
        best_sell_and_comicion = best_sell[0] * (1 - comicionesBinance)
    if best_sell[1] == "Huobi":
        best_sell_and_comicion = best_sell[0] * (1 - comicionesHuibi)

    
        
    profit = (best_sell_and_comicion / best_buy_and_comicion) - 1
    salida = {"pair" : cripto , "buy_price" : best_buy[0] , "exchange_buy" : best_buy[1] , 'exchange_sell' : best_sell[1] , 'sell_price' : best_sell[0] , "proffit" : profit}
    #return ("pair= ", cripto , "buy_price= " , best_buy[0] , "exchange_buy= " , best_buy[1] , 'exchange_sell= ' , best_sell[1] , 'sell_price= ', best_sell[0] , "proffit= ", profit , "price_binance_bid = " , price_binance_bid , "price_binance_ask = ", price_binance_ask , "price_huobi_bid = " , price_huobi_bid , "price_huobi_ask =" , price_huobi_ask , "buys = " , buys  , "sells = " , sells, "best_buy = " , best_buy , "best_sell = " , best_sell)
    return(salida)



cripto = open("Tikers entre huobi y binance.json", "r") 
cadenajson = json.load(cripto)


for i in range (len(cadenajson['tikers'])):
    criptos = cadenajson['tikers'][i]
    info_cripto = best_buy_best_sell(criptos, 0.1, 0.2)
    if info_cripto['proffit'] > 0.0:
        print(info_cripto)

        buy_price = info_cripto['buy_price']
        buy_exchange = info_cripto['exchange_buy']
        sell_price = info_cripto['sell_price']
        sell_exchange = info_cripto['exchange_sell']
        pair = info_cripto['pair']
        profit = info_cripto['proffit']


        #MySql.intoducir_info_en_la_db(buy_price , buy_exchange, sell_price, sell_exchange, pair, profit)