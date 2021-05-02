import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('stopwords')
nltk.download('vader_lexicon')

def limpiar_autores(elem):
    if '??' in elem:
        return elem.replace('?', '').strip(' / ')
    else:
        return elem


def nombre_apellido_may(elem):
    return elem.title().strip(',')


def quitar_nonsource(elem):
    return re.sub(r'attributed-no-source;', '', elem)


def list_tag(elem):
    return elem.split(';')


def eliminar_misattributed(elem):
    for tag in elem:
        if 'misattributed' in tag:
            elem.remove(tag)
    return elem

def columna_str_tags(elem):
    return ','.join(elem)


def reduce_quote(elem):
    respuesta = []
    eliminar = elem.maketrans('', '', ',.:;-_?¿/*-+¡!')
    elem = elem.translate(eliminar)
    lista_reducida = elem.split(' ')

    stop_words = set(stopwords.words('english'))

    for palabra in lista_reducida:
        if palabra.lower() not in stop_words:
            respuesta.append(palabra)
    
    return " ".join(respuesta)


def sentiment_compound(elem):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(elem)['compound']


def sentiment_pos(elem):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(elem)['pos']



def sentiment_neg(elem):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(elem)['neg']

