# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

import dotenv
import json
import os
from pymongo import MongoClient


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


dotenv.load_dotenv()
client = MongoClient(os.getenv('URL'))


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


def restaurar_db():
    print ('--------------------------------------------------------------------ENTRANDO----------------------------------------------------------------------')
    bases_existentes = client.list_database_names()
    # DEBERÍA PLANTEARME METER COMO ARGUMENTOS EL NOMBRRE DE LA DB Y EL NOMBRE DE LA COLECCIÓN PARA QUE FUESE MÁS DINÁMICA LA FUNCIÓN
    #print(client.list_database_names())

    if 'quotes' not in bases_existentes:
        
        db = client['quotes']
        coleccion = db['sentiment']
        archivo = open(('data/quotes_collection.json'), 'r')
        for linea in archivo: 
            dic = json.loads(linea)
            coleccion.insert_many(dic)
            
    else:

        print ('La Base de Datos ya existe')
        # Soy consciente de que a partir de aquí todo es redundante, que podría haber metido estos condicionales en el primer if, pero necesitaba cierto orden en mi cabeza
        # y que ese orden se reflejase visualmente. En un momento dado si todo me funciona cambiaré esta función.
        db = client['quotes']
        coleccion = db['sentiment']        
        if "sentiment" in db.list_collection_names() == False or coleccion.estimated_document_count() == 0:
            
            archivo = open(('data/quotes_collection.json'), 'r')
            for linea in archivo: 
                dic = json.loads(linea)
                coleccion.insert_many(dic)
                
        else:
            print ('Todo está preparado para funcionar')