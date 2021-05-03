# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

import json
import src.gestion_db as gdb
import src.tratamiento_datos as td
import tools.query_tools as qt

from bson import ObjectId
from config.configuration import db, coleccion

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------



def entrada_nueva(autor, cita, etiquetas):

    if qt.coincidencia(cita) == True:

        return {'mensaje' : 'Esa cita ya se encuentra en la base de datos'}
    
    else:
        indice_max = list(coleccion.find().sort('_id', -1).limit(1))[0]['_id']
        cita_reducido = td.reduce_quote(cita)
        cita_sentiment = [td.sentiment_pos(cita), td.sentiment_neg(cita), td.sentiment_compound(cita)]

        estructura = {'_id' : indice_max + 1,
                        'autor' : f'{autor}',
                        'cita' : f'{cita}',
                        'cita_sentiment_(P/N/C)' : cita_sentiment,
                        'etiquetas' : etiquetas,
                        'cita_reducido' : cita_reducido,
        }

        coleccion.insert_one(estructura)
    gdb.hacer_backup()
    return {'mensaje' : 'Gracias por tu aportación'}


def borrar_coleccion():
    #gdb.hacer_backup()
    coleccion.remove({})
    #return 'Pues ya hemos borrado todo'


def restaurar_db(original):

    coleccion.remove({})

    if original == 'original':        
        archivo = open(('data/quotes_collection.json'), 'r')
        for linea in archivo: 
            dic = json.loads(linea)
            coleccion.insert_many(dic)
    else:
        archivo = open(('data/quotes_collection_backup.json'), 'r')
        for linea in archivo: 
            dic = json.loads(linea)
            coleccion.insert_many(dic)
    
    #return 'Espero que se haya restaurado'


def eliminar_cita(numero):
    seguro = list(coleccion.find({'_id' : int(numero)}))
    print('.............seguro.........................')
    print (seguro)
    #coleccion.remove({"cita" : seguro[0]['cita']})
    
    if len(seguro) > 0:
        coleccion.remove({'_id' : int(numero)})
        #coleccion.delete_one({"cita" : seguro[0]['cita']})
    else:
        print ('No se ha encontrado tu cita')


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
