# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

import src.tratamiento_datos as td
from config.configuration import db, coleccion
import tools.query_tools as qt

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
                        'cita_sentiment_(P/N/C)' : 'ESTÁ POR HACER',
                        'etiquetas' : etiquetas,
                        'cita_reducido' : cita_reducido,
        }

        coleccion.insert_one(estructura)
        return {'mensaje' : 'Gracias por tu aportación'}


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
