# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

import json
import tools.query_tools as qt
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

    if len(seguro) > 0:
        coleccion.remove({'_id' : int(numero)})
        gdb.hacer_backup()
    else:
        print ('No se ha encontrado tu cita')

def modificar_cita(antigua, buena):
    seguro = list(coleccion.find({'cita' : antigua}))
    
    if qt.coincidencia(buena):
        return 'Esa frase ya se encuentra en la base de datos'
    
    cita_reducido = td.reduce_quote(buena)
    cita_sentiment = [td.sentiment_pos(buena), td.sentiment_neg(buena), td.sentiment_compound(buena)]

    if len(seguro) > 0:
        coleccion.update({'cita': antigua},{'$set':{'cita' : buena}})
        coleccion.update({'cita_reducido': seguro[0]['cita_reducido']},{'$set':{'cita_reducido' : cita_reducido}})
        coleccion.update({'cita_sentiment_(P/N/C)': seguro[0]['cita_sentiment_(P/N/C)']},{'$set':{'cita_sentiment_(P/N/C)' : cita_sentiment}})
        gdb.hacer_backup()
    else:
        print ('No se ha encontrado tu cita')

def modificar_autor_de_cita(cita, autor):
    seguro = list(coleccion.find({'cita' : cita}))
    
    if len(seguro) > 0:
        coleccion.update({'autor': seguro[0]['autor']},{'$set':{'autor' : autor}})
        gdb.hacer_backup()
    else:
        print ('No se ha encontrado tu cita')


def modificar_autor_por_index(index, autor):
    seguro = list(coleccion.find({'_id' : int(index)}))
    
    if len(seguro) > 0:
        coleccion.update({'autor': seguro[0]['autor']},{'$set':{'autor' : autor}})
        gdb.hacer_backup()
    else:
        print ('No se ha encontrado tu cita')


def modificar_cita_por_index(index, cita):
    if qt.coincidencia(cita):
        return 'Esa frase ya se encuentra en la base de datos'

    seguro = list(coleccion.find({'_id' : int(index)}))

    cita_reducido = td.reduce_quote(cita)
    cita_sentiment = [td.sentiment_pos(cita), td.sentiment_neg(cita), td.sentiment_compound(cita)]
    
    if len(seguro) > 0:
        coleccion.update({'cita': seguro[0]['cita']},{'$set':{'cita' : cita}})
        coleccion.update({'cita_reducido': seguro[0]['cita_reducido']},{'$set':{'cita_reducido' : cita_reducido}})
        coleccion.update({'cita_sentiment_(P/N/C)': seguro[0]['cita_sentiment_(P/N/C)']},{'$set':{'cita_sentiment_(P/N/C)' : cita_sentiment}})
        gdb.hacer_backup()
    else:
        print ('No se ha encontrado tu cita')


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
