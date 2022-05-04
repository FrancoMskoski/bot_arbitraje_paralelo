import Binance
import huobi 


for i in range(len(huobi.precios_globales_precios['data'])):
    for x in range(len(Binance.precios_globales_precios)):
        texto = str(huobi.precios_globales_precios['data'][i]['symbol'])
        if texto.upper() == Binance.precios_globales_precios[x]['symbol']:
            print('"' + texto.upper() + '" ,')