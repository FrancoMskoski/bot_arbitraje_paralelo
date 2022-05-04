import requests

tikers_info = {}

precios_globales_url = "https://api.huobi.pro/market/tickers"
precios_globales_datos = requests.get (precios_globales_url)
precios_globales_precios  = precios_globales_datos.json()
    

for i in range(len(precios_globales_precios['data'])):
    tikers_info  [(precios_globales_precios['data'][i]['symbol']).upper()] = {'price' : precios_globales_precios['data'][i]['close'] , 'bid' : precios_globales_precios['data'][i]['bid'], 'bidSize' : precios_globales_precios['data'][i]['bidSize'] , 'ask' : precios_globales_precios['data'][i]['ask'],'askSize' : precios_globales_precios['data'][i]['askSize'] }
    
#print(tikers_info["SOLUSDT"])

