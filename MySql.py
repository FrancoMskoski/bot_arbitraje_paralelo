from sqlite3 import connect
import mysql.connector
from mysql.connector import Error 
import datetime


def intoducir_info_en_la_db(buy_price , buy_exchange, sell_price, sell_exchange, pair, profit):
    try:
        coneccion = mysql.connector.connect(host = 'localhost' , port = 3306, user = 'root' , password = '123' , db = 'prueba')
        rigthnaw = datetime.datetime.now()
        if coneccion.is_connected():
            #print('coneccion exitosa')
            cursor = coneccion.cursor()
            cursor.execute("insert into cripto (fecha, buy_price, buy_exchange, sell_price, sell_exchange, pair, profit)values('{}', '{}', '{}', '{}', '{}', '{}', '{}')" . format(rigthnaw , buy_price , buy_exchange , sell_price , sell_exchange , pair , profit))
            coneccion.commit() # Confirma la accion que acabamos de hacer en la base de datos
            print("Registrado con exito ")

    except Error as ex:
        print('Error papu , fijate = ' , ex)

    finally:
        if coneccion.is_connected():
            coneccion.close() #para cerrar la coneccion 
            #print("Se serro la coneccion")


#intoducir_info_en_la_db( 0.1 , 'no se xd ', 0.11 , 'tu mama', 'USDTBTC', '0.1546')



