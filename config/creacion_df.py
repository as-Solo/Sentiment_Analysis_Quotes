# realizado por 'Solo' a 02/05/2021



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


import pandas as pd
import sys

import src.tratamiento_datos as td

#sys.path.append("../")


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------



def crear_csv():

    frases = pd.read_csv('data/quotes.csv', index_col = 0)

    frases = frases[frases['quote'].notna()]

    frases = frases.drop(frases[frases['quote'].str.contains('\?\?\?')].index)

    frases.author = frases.author.apply(td.limpiar_autores)

    frases = frases.drop(frases[frases['author'].str.contains('\?')].index)

    frases.author = frases.author.apply(td.nombre_apellido_may)

    frases.tags = frases.tags.apply(td.quitar_nonsource)

    frases.tags = frases.tags.apply(td.list_tag)

    frases.tags = frases.tags.apply(td.eliminar_misattributed)

    frases['tags_words'] = frases.tags.apply(td.columna_str_tags)

    frases['quote_words'] = frases.quote.apply(td.reduce_quote)

    frases['quote_compound'] = frases.quote_words.apply(td.sentiment_compound)

    frases['quote_positive'] = frases.quote_words.apply(td.sentiment_pos)

    frases['quote_negative'] = frases.quote_words.apply(td.sentiment_neg)

    # he decidido hacer más liviano el csv y el json, no estaba utilizando para nada estos datos en este proyecto en particular y no tenía sentido tenerlos en mi base de datos.

    #frases['tags_compound'] = frases.tags_words.apply(td.sentiment_compound)

    #frases['tags_positive'] = frases.tags_words.apply(td.sentiment_pos)

    #frases['tags_negative'] = frases.tags_words.apply(td.sentiment_neg)

    #quotes = frases[['author', 'quote', 'quote_words', 'quote_compound', 'quote_positive', 'quote_negative', 'tags', 'tags_words', 'tags_compound', 'tags_positive',  'tags_negative', 'likes']]
    
    quotes = frases[['author', 'quote', 'quote_words', 'quote_compound', 'quote_positive', 'quote_negative', 'tags', 'tags_words']]

    quotes.to_csv('data/quotes_sentiment.csv', index = False)


def crear_json():
    
    try:
        prueba = pd.read_csv('data/quotes_sentiment.csv')
    except FileNotFoundError:
        print ('El archivo "quotes_sentiment.csv" no existe')

    coleccion = []
    for index, row in prueba.iterrows():
        estructura = {
        '_id' : index,
        'autor' : row.author,
        'cita' : row.quote,
        'cita_sentiment_(P/N/C)' : [row.quote_positive, row.quote_negative, row.quote_compound],
        'etiquetas' : [elem for elem in row.tags_words.split(',')],
        #'etiquetas_sentiment_(P/N/C)' : [row.tags_positive, row.tags_negative, row.tags_compound],
        #'likes' : row.likes,
        'cita_reducido' : row.quote_words,
        #'etiquetas_reducido' : row.tags_words,
    }
        coleccion.append(estructura)


    coleccion = pd.DataFrame(coleccion)
    coleccion.to_json("data/quotes_collection.json", orient="records")
 