![Portada](https://github.com/as-Solo/Sentimentanalysis_Quotes/blob/main/img/portada_readme.jpg)

## DOCUMENTACIÓN DE LA API QUOTES SENTIMENT

#### En esta documentación se explicará de la manera más simple posible cuáles son las funciones .get y .post implementadas para poder hacer querys a la base de datos 'quote sentiment'.

#### Antes de nada mostrar un ejemplo de la estructura de los datos a los que podréis acceder.

```
estructura = {
  '_id': 0,
  'autor': 'Oscar Wilde',
  'cita': 'Be yourself; everyone else is already taken.',
  'cita_sentiment_(P/N/C)': [0.0, 0.0, 0.0],
  'etiquetas': ['be-yourself', 'honesty', 'inspirational'],
  'cita_reducido': 'everyone else already taken',
  }
```

#### Todos los métodos tienen una estructura muy similar, donde lo importante es saber cuál es la url a la que hacer la request y qué argumentos son los necesarios para la misma, en caso de que sean necesarios los argumentos.

#### Separaremos esta documentación en dos partes, las funciones GET y las funciones POST

<br/>

## FUNCIONES GET

### CITAS DE AUTOR
Esta función devuelve todas las citas de un autor que se pasará por parámetro que se encuentren en la base de datos.
#### Los dos parámetros a tener en cuenta son:
URL : 'http://localhost:5000/mensaje_autor'

nombre = *

Se concatenarán ambos argumentos para obtener dicha información

#### Un ejemplo de request sería:

```
url_citas = 'http://localhost:5000/mensaje_autor'
nombre = 'Oscar Wilde'

rases = requests.get(url_citas + nombre).json()
frases
```
[Output]:

```
[{'cita': 'Be yourself; everyone else is already taken.'},
 {'cita': 'We are all in the gutter, but some of us are looking at the stars.'},
 {'cita': 'A man who does not think for himself does not think at all.'},
 {'cita': 'But we never get back our youth… The pulse of joy that beats in us at twenty becomes sluggish. Our limbs fail, our senses rot. We degenerate into hideous puppets, haunted by the memory of the passions of which we were too much afraid, and the exquisite temptations that we had not the courage to yield to.'},
 {'cita': "The ugly and stupid have the best of it in this world. They can sit at their ease and gape at the play. If they know nothing of victory, they are at least spared the knowledge of defeat. They live as we all should live-- undisturbed, indifferent, and without disquiet. They never bring ruin upon others, nor ever receive it from alien hands. Your rank and wealth, Henry; my brains, such as they are-- my art, whatever it may be worth; Dorian Gray's good looks-- we shall all suffer for what the gods have given us, suffer terribly."},
 {'cita': 'What fire does not destroy, it hardens'},
 {'cita': 'Life is one fool thing after another whereas love is two fool things after each other.'}]

```
<br/>

### CITA RANDOM
Esta función devuelve cita aleatoria que se encuentren en la base de datos.
#### El único parámetro a tener en cuenta son:
URL : 'http://localhost:5000/random'

#### Un ejemplo de request sería:

```
url_query = "http://localhost:5000/random"
data = requests.get (url_query).json()
data
```
[Output]:

```
'God, grant me the serenity to accept the things I cannot change, the courage to change the things I can, and the wisdom to know the difference.'

```
<br/>

### CITAS POSITIVAS
Esta función devuelve un numero de citas a determinar con una valoración del Sentiment positiva con un valor a elegir.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/citas_positivas'

mayor = (puede ser int o float y determina qué valor debe tener el sentiment como mínimo para que la frase sea mostrada)

numero = *(debe ser un int y determina el número de citas a mostrar)

#### Un ejemplo de request sería:

```
url_pos = "http://localhost:5000/citas_positivas"
mayor = '0.8'
numero = '2'
citas = requests.get(url_pos + mayor + '_' + numero).json()
citas
```
[Output]:

```
[{'autor': 'Mother Teresa',
  'cita': 'Peace begins with a smile..',
  'cita_sentiment_(P/N/C)': [0.857]},
 {'autor': 'Walt Disney',
  'cita': "It's kind of fun to do the impossible.",
  'cita_sentiment_(P/N/C)': [0.87]}]

```

<br/>

### CITAS NEGATIVAS
Esta función devuelve un numero de citas a determinar con una valoración del Sentiment negativa con un valor a elegir.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/citas_negativas'

mayor = (puede ser int o float y determina qué valor debe tener el sentiment como mínimo para que la frase sea mostrada)

numero = *(debe ser un int y determina el número de citas a mostrar)

#### Un ejemplo de request sería:

```
url_neg = "http://localhost:5000/citas_negativas"
mayor = '0.8'
numero = '2'
citas = requests.get(url_neg + mayor + '_' + numero).json()
citas
```
[Output]:

```
[{'autor': 'William Shakespeare',
  'cita': 'Hell is empty and all the devils are here.',
  'cita_sentiment_(P/N/C)': [1.0]},
 {'autor': 'Roy T. Bennett',
  'cita': 'Do not fear failure but rather fear not trying.',
  'cita_sentiment_(P/N/C)': [0.829]}]

```

<br/>

### CITAS COMPOUND NEGATIVAS
Esta función devuelve un numero de citas a determinar con una valoración del Sentiment compound negativa con un valor a elegir.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/citas_compound_neg'

mayor = (puede ser int o float y determina qué valor debe tener el compound como máximo para que la frase sea mostrada)

numero = *(debe ser un int y determina el número de citas a mostrar)

#### Un ejemplo de request sería:

```
url_cneg = "http://localhost:5000/citas_compound_neg"
menor = '-0.8'
numero = '2'
citas = requests.get(url_cneg + menor + '_' + numero).json()
citas
```
[Output]:

```
[{'autor': 'Ralph Waldo Emerson',
  'cita': 'What lies behind us and what lies before us are tiny matters compared to what lies within us.',
  'cita_sentiment_(P/N/C)': [-0.8074]},
 {'autor': 'Nicholas Klein',
  'cita': 'First they ignore you. Then they ridicule you. And then they attack you and want to burn you. And then they build monuments to you.',
  'cita_sentiment_(P/N/C)': [-0.8074]}]

```

<br/>

### CITAS COMPOUND POSITIVAS
Esta función devuelve un numero de citas a determinar con una valoración del Sentiment compound positiva con un valor a elegir.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/citas_compound_pos'

mayor = (puede ser int o float y determina qué valor debe tener el compound como mínimo para que la frase sea mostrada)

numero = *(debe ser un int y determina el número de citas a mostrar)

#### Un ejemplo de request sería:

```
url_cpos = "http://localhost:5000/citas_compound_pos"
mayor = '0.6'
numero = '2'
citas = requests.get(url_cpos + mayor + '_' + numero).json()
citas
```
[Output]:

```
[{'autor': 'Stephen Chbosky',
  'cita': 'We accept the love we think we deserve.',
  'cita_sentiment_(P/N/C)': [0.7783]},
 {'autor': 'Bill Keane',
  'cita': 'Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.',
  'cita_sentiment_(P/N/C)': [0.6124]}]

```

<br/>

### CITAS CON UN CONTENIDO ESPECÍFICO
Esta función devuelve todas las citas que tengan un contenido a determinar por el usuario.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/citas_que_contienen'

extracto = (es el contenido que se busca que tenga la cita)

Se concatenarán ambos parámetros

#### Un ejemplo de request sería:

```
url_cont = "http://localhost:5000/citas_que_contienen"
extracto = 'live is'
citas = requests.get(url_cont + extracto).json()
citas
```
[Output]:

```
[{'_id': 100,
  'autor': 'Agatha Christie',
  'cita': 'I like living. I have sometimes been wildly, despairingly, acutely miserable, racked with sorrow; but through it all I still know quite certainly that just to be alive is a grand thing.'},
 {'_id': 723,
  'autor': 'Emily Dickinson',
  'cita': 'To live is so startling it leaves little time for anything else.'},
 {'_id': 733,
  'autor': 'Louis C.K.',
  'cita': 'I’m bored’ is a useless thing to say. I mean, you live in a great, big, vast world that you’ve seen none percent of. Even the inside of your own mind is endless; it goes on forever, inwardly, do you understand? The fact that you’re alive is amazing, so you don’t get to say ‘I’m bored.'},
 {'_id': 1199,
  'autor': 'Michel Houellebecq',
  'cita': 'The absence of the will to live is, alas, not sufficient to make one want to die.'},
 {'_id': 2950,
  'autor': 'Kofi Annan',
  'cita': 'To live is to choose. But to choose well, you must know who you are and what you stand for, where you want to go and why you want to get there.'}]
```



<br/>

## FUNCIONES POST

<br/>

### INTRODUCIR UNA NUEVA CITA
Esta función permite al usuario introducir una nueva cita en la base de datos, para ello tendrá que ofrecer la cita, el autor y al menos una eitiqueta. Si la frase ya se encuentra en la base de datos no se añadirá.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/nueva_cita'

autor = *

cita = +

etiquetas = (Debe ser una string, separando las distintas etiquetas con un espacio)

#### Un ejemplo de request sería:

```
url = 'http://localhost:5000/nueva_cita'
datos = {'autor': 'Solo',
 'cita': 'Sólo sé que no sé Python',
 'etiquetas': 'realidad vacío',
        }

requests.post(url, data = datos)

# Esto es código para confirmar que se ha intrudocido la frase correctamente
frases = requests.get(url_citas + 'Solo').json()
frases
```
[Output]:

```
[{'cita': 'Sólo sé que no sé Python'}]
```


<br/>


### ELIMINAR UNA CITA
Esta función permite al usuario eliminar una cita en la base de datos, para ello tendrá que ofrecer el id.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/eliminar_cita'

_id = (Tiene que ser un int y el indice tiene que existir en la base de datos)

#### Un ejemplo de request sería:

```
url_borrar = "http://localhost:5000/eliminar_cita"
datos = {'_id' : 2964}
requests.post(url_borrar, data =datos)
```


<br/>


### MODIFICAR UNA CITA
Esta función permite al usuario modificar una cita en la base de datos, para ello se tiene que ofrecer el la cita que se quiere modificar y la nueva frase ya modificada.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/modificar_cita'

antigua = (Tiene que coincidir con una frase que se encuentre en la base de datos)

buena = (La frase por la que se quiere sustituir la cita seleccionada

#### Un ejemplo de request sería:

```
url_modificar = "http://localhost:5000/modificar_cita"
datos = {'antigua' : 'Sólo sé que no sé Python', 'buena' : 'mimimimimimimim imimimim '}
requests.post(url_modificar, data =datos)
```

<br/>


### MODIFICAR EL AUTOR DE UNA CITA
Esta función permite al usuario modificar el autor de una cita que se encuentre en la base de datos, para ello se tiene que ofrecer la cita de dicho autor y el nuevo autor.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/modificar_autor_de_cita'

cita = (Tiene que coincidir con una cita que se encuentre en la base de datos)

autor = (El autor la cita seleccionada)

#### Un ejemplo de request sería:

```
url_modificar = "http://localhost:5000/modificar_autor_de_cita"
datos = {'cita' : 'Sólo sé que no sé Python', 'autor' : 'Anónimo'}
requests.post(url_modificar, data =datos)
```

<br/>


### MODIFICAR EL AUTOR POR EL ÍNDICE
Esta función permite al usuario modificar el autor de una cita mediante el índice, para ello se tiene que ofrecer el índice de la cita y el nuevo autor.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/modificar_autor_por_indice'

index = (Tiene que ser un integer y debe de existir en la base de datos)

autor = (Nombre del nuevo autor)

#### Un ejemplo de request sería:

```
url_modificar_a = "http://localhost:5000/modificar_autor_por_indice"
datos = {'index' : 2964, 'autor' : 'Solo'}
requests.post(url_modificar_a, data =datos)
```

<br/>


### MODIFICAR UNA CITA POR EL ÍNDICE
Esta función permite al usuario modificar una cita mediante el índice, para ello se tiene que ofrecer el índice de la cita y la nueva cita.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/modificar_autor_por_indice'

index = (Tiene que ser un integer y debe de existir en la base de datos)

cita = (Cita modificada)

#### Un ejemplo de request sería:

```
url_modificar_c = "http://localhost:5000/modificar_cita_por_indice"
datos = {'index' : 2964, 'cita' : 'Solo sé que no sé Java'}
requests.post(url_modificar_c, data =datos)
```

<br/>


### BORRAR LA COLECCIÓN
Esta función permite al usuario borrar toda la colección de documentos que hay en la base de datos.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/borrar_coleccion'

#### Un ejemplo de request sería:

```
url_borrar = "http://localhost:5000/borrar_coleccion"
requests.post(url_borrar)
```

<br/>


### RESTAURAR COLECCIÓN
Esta función permite al usuario restaurar toda la colección de documentos que había en la base de datos, o bien con los valores por defecto o bien con los camnbios y las implementaciones que se hicieron hasta el momento de borrarla.
#### Los parámetros y argumentos a tener en cuenta son:
URL : 'http://localhost:5000/borrar_coleccion'

original = (Tiene que ser un string, cualquier valor que no sea 'original' restaurará la base de datos con todos los valores añadidos y modificados, si el valor es'original, restaurará la base de datos a sus valores por defecto)

#### Un ejemplo de request sería:

```
url_rest = "http://localhost:5000/restaurar_coleccion"
datos = {'original' : 'original'}
requests.post(url_rest, data =datos)
```
