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
#### los dos parámetros a tener en cuenta son:
URL : 'http://localhost:5000/mensaje_autor'

nombre_autor

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

valor_minimo_de_positividad = (puede ser int o float y determina qué valor debe tener el sentiment como mínimo para que la frase sea mostrada)

numero_de_frases = *(debe ser un int y determina el número de citas a mostrar)

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

valor_minimo_de_negatividad = (puede ser int o float y determina qué valor debe tener el sentiment como mínimo para que la frase sea mostrada)

numero_de_frases = *(debe ser un int y determina el número de citas a mostrar)

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

valor_maximo_de_compound_negativo = (puede ser int o float y determina qué valor debe tener el compound como máximo para que la frase sea mostrada)

numero_de_frases = *(debe ser un int y determina el número de citas a mostrar)

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

valor_minimo_de_compound_positivo = (puede ser int o float y determina qué valor debe tener el compound como mínimo para que la frase sea mostrada)

numero_de_frases = *(debe ser un int y determina el número de citas a mostrar)

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
