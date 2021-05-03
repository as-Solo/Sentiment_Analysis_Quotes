# realizado por 'Solo' a 03/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

from config.configuration import db, coleccion

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------



def coincidencia(a_buscar):
  
    datos = list(coleccion.find())
    
    for elem in datos:
        if a_buscar in elem['cita']:
            return True
    
    return False


def lista_coincidencias(a_buscar):
    
    datos = list(coleccion.find({},{'_id' : 1, 'autor' : 1, 'cita' : 1}))
    lista_coincidencias = []

    for elem in datos:
        if a_buscar in elem['cita']:
            lista_coincidencias.append(elem)
    
    if len(lista_coincidencias) > 0:
        return lista_coincidencias
    else:
        return 'No se han encontrado coincidencias'