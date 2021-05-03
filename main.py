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

@app.route('/citas_que_contienen<extracto>')
def citas_contains(extracto):
    citas = get.citas_coincidencias(extracto)
    return jsonify(citas)


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------


@app.route('/nueva_cita', methods = ['POST'])
def inserta_frase():
    autor = request.form.get('autor')
    cita = request.form.get('cita')
    etiquetas = request.form.get('etiquetas').split(' ')
    post.entrada_nueva(autor, cita, etiquetas)
    return {'mensaje' : 'Gracias por tu aportación.'}


@app.route('/borrar_coleccion', methods = ['POST'])
def borrar_todo():
    post.borrar_coleccion()
    return 'Pues ya hemos borrado todo'


@app.route('/restaurar_coleccion', methods = ['POST'])
def restaurar_coleccion():
    original = request.form.get('original')
    post.restaurar_db(original)
    return 'Espero que se haya restaurado'


@app.route('/eliminar_cita', methods = ['POST'])
def quitar_cita():
    numero = request.form.get('_id')
    post.eliminar_cita(numero)
    return 'La cita ha sido eliminada'

@app.route('/modificar_cita', methods = ['POST'])
def cambiar_cita():
    antigua = request.form.get('antigua')
    buena = request.form.get('buena')
    post.modificar_cita(antigua, buena)
    return 'La cita ha sido modificada'

@app.route('/modificar_autor_de_cita', methods = ['POST'])
def cambiar_autor_cita():
    cita = request.form.get('cita')
    autor = request.form.get('autor')
    post.modificar_autor_de_cita(cita, autor)
    return 'El autor ha sido cambiado'

@app.route('/modificar_autor_por_indice', methods = ['POST'])
def cambiar_autor_index():
    index = request.form.get('index')
    autor = request.form.get('autor')
    post.modificar_autor_por_index(index, autor)
    return 'El autor ha sido cambiado'

@app.route('/modificar_cita_por_indice', methods = ['POST'])
def cambiar_cita_index():
    index = request.form.get('index')
    cita = request.form.get('cita')
    post.modificar_cita_por_index(index, cita)
    return 'La cita ha sido cambiada'


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

app.run('localhost', '5000', debug = True)