# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


import config.creacion_df as crd
import src.gestion_db as gdb
import dotenv
import os
from pymongo import MongoClient

dotenv.load_dotenv()


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


archivo_csv = "data/quotes_sentiment.csv"
archivo_json = "data/quotes_collection.json"


if os.path.isfile(archivo_csv):
    print ('El archivo necesario "csv" existe')
else:
    print ('Por favor espere unos minutos, estamos preparando la base de datos')
    crd.crear_csv()


if os.path.isfile(archivo_json):
    print ('La colección "quotes_collection" existe')
else:
    crd.crear_json()

gdb.restaurar_db()


client = MongoClient(os.getenv('URL'))
db = client['quotes']
coleccion = db['sentiment']

#print ('''
#-----------------------------------------------------------------------------------------
#CONFIGURACIÓN   CONFIGURACIÓN  CONFIGURACIÓN  CONFIGURACIÓN  CONFIGURACIÓN
#-----------------------------------------------------------------------------------------
#''')

