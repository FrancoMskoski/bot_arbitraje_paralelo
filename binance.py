import requests

tikers_info = {}

precios_globales_url = "https://api1.binance.com/api/v3/ticker/bookTicker"
precios_globales_datos = requests.get (precios_globales_url)
precios_globales_precios  = precios_globales_datos.json()


for i in range(len(precios_globales_precios)):
    tikers_info  [precios_globales_precios[i]['symbol']] = { 'bid' : precios_globales_precios[i]['bidPrice'] ,'bidQty' :  precios_globales_precios[i]['bidQty'] , 'ask' : precios_globales_precios[i]['askPrice'], 'askQty' : precios_globales_precios[i]['askQty'] }

