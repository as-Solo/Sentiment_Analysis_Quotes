# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

import tools.query_tools as qt
import random
from config.configuration import db, coleccion

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


def mensaje_autor_HTML(personaje):
    #implementado
    personaje = personaje.title()
    query = {"autor" : f'{personaje}'}
    frases = list(coleccion.find(query, {"_id" : 0, 'cita' : 1}))
    cadena = str()
    numero = 1
    for elem in frases:
        cadena += str(numero) + '.- "' + str(elem["cita"]) + '"' + "<br />" + "<br />"
        numero += 1
    if len(cadena) > 0:
        return cadena
    else:
        return 'No se han encontrado coincidencias'

def mensaje_autor(personaje):
    #implementado
    personaje = personaje.title()
    query = {"autor" : f'{personaje}'}
    frases = list(coleccion.find(query, {"_id" : 0, 'cita' : 1}))
    return frases
    
def mensaje_aleatorio_HTML():
    #implementado
    numero = random.randint(0, 2964)
    query = {"_id" : numero}
    frase_aleatoria = list(coleccion.find(query, {"_id" : 0, 'cita' : 1}))
    return frase_aleatoria[0]['cita']

def mensaje_aleatorio():
    #implementado
    numero = random.randint(0, 2964)
    query = {"_id" : numero}
    frase_aleatoria = list(coleccion.find(query, {"_id" : 0, 'cita' : 1}))
    return frase_aleatoria


def citas_positivas(mayor_que, numero_citas):
    #implementado
    return list(coleccion.find({'cita_sentiment_(P/N/C).0' : {'$gte' : float(mayor_que)}}, {"cita_sentiment_(P/N/C)" : {'$slice' : [0,1]}, 'cita' : 1, 'autor' : 1, '_id' : 0}).limit(int(numero_citas)) )


def citas_negativas(mayor_que, numero_citas):
    return list(coleccion.find({'cita_sentiment_(P/N/C).1' : {'$gte' : float(mayor_que)}}, {"cita_sentiment_(P/N/C)" : {'$slice' : [1,1]}, 'cita' : 1, 'autor' : 1, '_id' : 0}).limit(int(numero_citas)) )


def citas_compound_pos(mayor_que, numero_citas):
    return list(coleccion.find({'cita_sentiment_(P/N/C).2' : {'$gte' : float(mayor_que)}}, {"cita_sentiment_(P/N/C)" : {'$slice' : [2,3]}, 'cita' : 1, 'autor' : 1, '_id' : 0}).limit(int(numero_citas)) )


def citas_compound_neg(menor_que, numero_citas):
    return list(coleccion.find({'cita_sentiment_(P/N/C).2' : {'$lte' : float(menor_que)}}, {"cita_sentiment_(P/N/C)" : {'$slice' : [2,3]}, 'cita' : 1, 'autor' : 1, '_id' : 0}).limit(int(numero_citas)) )


def citas_coincidencias(a_buscar):
    respuesta = qt.lista_coincidencias(a_buscar)
    return respuesta
    


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------