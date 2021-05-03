# realizado por 'Solo' a 02/05/2021


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


from flask import Flask, request
import markdown.extensions.fenced_code
from flask import jsonify

import tools.get_data as get
import tools.post_data as post

#import config.configuration # En algún momento puede que no sea necesario tener este import MIRA A VER SI PUEDES QUITARLO

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
print ('''

-----------------------------------------------------------------------------------------
MAIN   MAIN  MAIN   MAIN   MAIN   MAIN     MAIN   MAIN   MAIN   MAIN   MAIN   MAIN
-----------------------------------------------------------------------------------------

''')
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

app = Flask(__name__)

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


@app.route('/')
def index():
    readme_file = open('README.md', 'r')
    ms_template = markdown.markdown(readme_file.read(), extensions = ['fenced_code'])
    return ms_template

@app.route('/<name>')
def autor(name):
    frases = get.mensaje_autor_HTML(name)
    return frases

@app.route('/random')
def aleatorio():
    frase = get.mensaje_aleatorio_HTML()
    return jsonify(frase)

@app.route('/mensaje_autor<nombre>')
def mensaje_autor(nombre):
    frase = get.mensaje_autor(nombre)
    return jsonify(frase)

@app.route('/citas_positivas<mayor>_<numero>')
def citas_pos(mayor, numero):
    citas = get.citas_positivas(mayor, numero)
    return jsonify(citas)

@app.route('/citas_negativas<mayor>_<numero>')
def citas_neg(mayor, numero):
    citas = get.citas_negativas(mayor, numero)
    return jsonify(citas)

@app.route('/citas_compound_pos<mayor>_<numero>')
def citas_com_pos(mayor, numero):
    citas = get.citas_compound_pos(mayor, numero)
    return jsonify(citas)

@app.route('/citas_compound_neg<menor>_<numero>')
def citas_com_neg(menor, numero):
    citas = get.citas_compound_neg(menor, numero)
    return jsonify(citas)


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

app.run('localhost', '5000', debug = True)