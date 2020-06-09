# Telegram bot: Skylines

Telegram bot implemented in python, made to create and manage city skylines.

## Usage

### Prerequisites
The necessary libraries to execute the bot are listed inside `requirements.txt`. They can be installed using
```bash
> pip3 install -r requirements.txt
```
You will also need to set up a telegram bot and get an *Access token*, which is a unique identifier given by Telegram to identify bots. In order to get it:
  - Access [@BotFather](https://telegram.me/botfather)
  - Use the `/newbot` command and fill all required information (full name and bot username, which must end with `'bot'`).
  - Save inside a `token.txt` file the received *access token*, which looks something like `U10201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`. This file must be saved inside the same directory where the program `bot.py`is located.

The full instructions on how to set up a Telegram bot can be found at https://core.telegram.org/bots#6-botfather.

### Execution

To run the program, simply run
```bash
> python3 bot.py
```
### Bot commands
The bot has several commands:
- `/start`: Starts the conversation with the bot (Note: it is not required to run this command in order to use the bot)
- `/help`: Displays help, which can be either the description of the commands or the explanation on the language's syntax.
- `/author`: The bot displays information about the author.
- `/lst`: Llista tots els identificadors definits i l'àrea de l'skyline que hi ha a cadascun.
- `/clean`: Esborra tots els identificadors definits.
- `/save [skyline1, skyline2, ...]`: Guarda els skylines indicats per l'usuari. Si no s'indica cap skyline per guardar, el bot ens demana que seleccionem els que volem guardar mostrant-nos una llista de tots els disponibles.
- `/load [skyline1, skyline2, ...]`: Carrega els skylines indicats per l'usuari. Si no s'indica cap skyline per guardar, el bot ens demana que seleccionem els que volem carregar mostrant-nos una llista de tots els disponibles.

### Llenguatge per gestionar skylines

El llenguatge permet els tipus d’operacions següents:
- Creació d’edificis:
  - Simple: `(xmin, alçada, xmax)` on `xmin` i `xmax` especifiquen la posició d’inici i final a la coordenada horizontal i `alçada` l’alçada de l’edifici. Ex: `(1, 2, 3)`.
  - Compostos: `[(xmin, alçada, xmax), ...]` permet definir diversos edificis mitjançant una llista d’edificis simples. Ex: `[(1, 2, 3), (3, 4, 6)]` o `[(1, 1, 2), (1000000000000, 1, 1000000000001)]`.
  - Aleatoris: `{n, h, w, xmin, xmax}` construeix `n` edificis, cadascun d’ells amb una alçada aleatòria entre 0 i `h`, amb una amplada aleatòria entre 1 i `w`, i una posició d’inici i de final aleatòria entre `xmin` i `xmax`.

- Operadors d’skylines:
  - `skyline + skyline`: unió
  - `skyline * skyline`: intersecció
  - `skyline * N`: replicació N vegades de l’skyline
  - `skyline + N`: desplaçament a la dreta de l’skyline N posicions
  - `skyline - N`: desplaçament a l’esquerra de l’skyline N posicions
  - `- skyline`: retorna l’skyline reflectit.

La taula següent mostra la prioritat d’operadors de més gran a més petita:

_**Operador**_ | _**Descripció**_
------------ | -------------
`( )` | Parèntesis
`-` | Mirall
`*` | Intersecció i replicació
`+` `-` | Unió i desplaçaments

- Identificadors:

El llenguatge admet l'ús d'*identificadors* i d'*assignacions* mitjançant l'operador `:=`. Els identificadors han de ser una lletra seguida de zero o més lletres o dígits. Ex: `a := (1, 2, 3)`.

## Estructura del codi

El codi del nostre bot es pot dividir en 4 parts:
- `bot.py`: S'encarrega de gestionar la interacció amb l'usuari a través de telegram
- `Antlr.py`: Fa de pont entre el bot i la gramàtica. Sencarrega de gestionar les comandes rebudes des del bot i enviar a `EvalVisitor` les operacions de gestió d'skylines rebudes des del bot. També gestiona les excepcions generades durant l'execució.
- `EvalVisitor.py` i gramàtica: S'encarreguen de parsejar les operacions rebudes i generar i modificar els skylines resultant d'aquestes operacions.
- `Skyline.py`: Defineix la classe skyline i les operacions que s'hi poden fer.

### La classe Skyline

Per implementar la classe `Skyline`, hem decidit utilitzar un diccionari. Aquest guarda l'alçada de cada posició dins de l'*skyline*, sempre i quan aquesta alçada sigui superior a zero. Per tant, les claus del diccionari són nombres enters que indiquen la posició, i el seu valor un altre enter que ens indica l'alçada de l'*skyline* a aquella posició. Això significa que, per a guardar un edifici, tindrem tantes entrades com l'amplada d'aquest edifici. Per exemple, l'edifici `(1,2,4)` quedarà guardat al diccionari de l'*skyline* com a `{1:2, 2:2, 3:2}`. 

És fàcil veure que guardar les dades d'aquesta forma ocuparà més espai que si utilitzéssim una estructura més *naive*, com ara una llista d'edificis, on per cada edifici guardem les mateixes dades que ens proporciona l'usuari (`xmin`, `h`, `xmax`). Però l'utilització del diccionari ens permetrà fer operacions sobre l'*skyline* molt més ràpides, com veurem a continuació. Tenint en compte que actualment els computadors es veuen molt més limitats per la capacitat de processament que per la seva memòria, hem decidit que aquest mètode era el més adeqüat. Una altra avantatge d'utilitzar aquesta estructura és la simplicitat d'implementació de les operacions, que fa el codi molt més fàcil de mantenir.

A continuació explicarem com s'han implementat les diferents operacions sobre *skylines*, i analitzarem la seva complexitat. 

#### Unió
Aquesta operació realitza la unió de dos skylines. Per exemple, si executem `a := b + c`, l'*skyline* `a` serà la unió de `b` i `c`.

Per fer aquesta operació, primer fem una copia del primer *skyline* de l'operació, per tal d'evitar modificar aquest durant l'execució. Llavors, per a cada element dins el diccionari del segon skyline, si a la copia ja existeix una entrada amb la mateixa clau, li assignem com a valor el màxim entre el valor actual i el valor al segon skyline. Si no existeix l'entrada, afegim aquest element a la nostra copia. Un cop acabat, retornarem el nou skyline.

Degut a que el cost de consultar o modificar una entrada al diccionari és `O(1)`, i fem aquest procés per a cada element del segon diccionari, el cost serà `O(m)`, on `m` és el nombre d'elements del segon diccionari. Si sumem la complexitat de la copia obligatòria del primer diccionari, el cost total d'aquesta operació és `O(n) + O(m) = O(n+m)`.

Si comparem el cost amb el que s'hauria obtingut en cas d'utilitzar una llista d'edificis com a estructura de dades, podem veure que hauríem mantingut el cost de la copia `O(n)`, i per fer la unió hauríem d'implementar una búsqueda binària, de cost `O(log n)`, i per a cada inserció dins la llista pagar un cost `O(n)`, ja que com cal mantenir la llista ordenada, no podem inserir l'element al final d'aquesta, ho hem de fer a la posició corresponent. Per tant, el cost de l'operació seria `O(n) + O(n log n) = O(n log n)`.

#### Intersecció
Aquesta operació realitza la intersecció de dos skylines. Per exemple, si executem `a := b + c`, l'*skyline* `a` serà la intersecció de `b` i `c`.

Gràcies a la nostra implementació de *skyline* amb un diccionari, aquesta operació és pràcticament igual que la unió, on només fem 2 petits canvis. En comptes de fer una copia del diccionari del primer skyline, en crearem un buit. Llavors, iterarem per tots els elements del skyline més petit, i per a cada un d'aquests elements mirarem si també es present a l'altre skyline. En cas afirmatiu, afegirem al nou diccionari que hem creat una entrada amb la clau de l'element i amb el valor mínim entre els dos skylines. Un cop acabat, retornarem el nou skyline.

En aquest cas, com no hem de fer copia d'un skyline, no hem de pagar el cost d'aquesta. I com iterem per l'skyline amb el menor nombre d'entrades, i consultar un valor a un diccionari té cost `O(1)`, el cost de la intersecció serà `O( min(n, m) )`, on `n` i `m` són el nombre d'entrades de cada skyline.

En el cas d'haver utilitzat llistes, el cost seria igual que el de la unió, `O(n log n)`.

#### Replicació
Per implementar la replicació, simplement cal afegir a l'skyline una còpia d'ell mateix desplaçada, i fer-ho `m` vegades, on `m` indica el nombre de replicacions. Per fer una copia tenim un cost de `O(n)`, per a un skyline de `n` elements, i per fer el desplaçament només cal sumar l'amplada de l'*skyline* a les claus. Per tant, el cost de l'operació és `O(n*m)`.

En el cas d'haver utilitzat llistes, el cost seria exactament el mateix, degut a que hem de fer les copies i desplaçaments igual.

#### Desplaçament
Per fer un desplaçament de l'skyline, només cal sumar o restar a cada clau el valor que es vol desplaçar. Com això s'ha de fer per a cada entrada del diccionari, el cost és `O(n)`, on `n` és el nombre d'elements del diccionari.

El cost en cas d'utilitzar una llista seria el mateix, ja que cal iterar per tots els elements per sumar el desplaçament.

#### Mirall
L'operació de mirall gira el nostre skyline d'esquerra a dreta. A efectes pràctics, es fa un desplaçament de cada entrada del diccionari. Aquest desplaçament és diferent per a cada element, però es pot calcular amb una simple operació de cost `O(1)`, i per tant el cost total de l'operació mirall és de `O(n)`.

En cas d'haver utilitzat una llista, el cost seria el mateix, ja que cal iterar per tots els elements presents a aquesta.

#### Càlcul de l'àrea i alçada de l'*skyline*
Degut a que cada vegada que l'usuari fa una operació hem de retornar l'àrea i alçada màxima de l'*skyline*, s'ha decidit que aquests valors seràn valors materialitzats en comptes de derivats, i per tant cada vegada que modifiquem un skyline augmentarem o disminuirem els seus valors de forma corresponent.

#### Compressió de l'*skyline*
Com hem dit, la utilització d'un diccionari per representar l'skyline augmenta l'eficiència del programa, però també l'espai que ocupa. Quan volem guardar un skyline, no farem operacions sobre l'arxiu guardat, i per tant ens interessa més tenir-lo representat amb una estructura de dades més eficient en espai. És per això que s'ha implementat el métode `getCompressedSkyline()`, que transforma la nostra estructura de diccionari en una llista d'edificis, on per a cada edifici guardem només la seva posició inicial, posició final i alçada. El mètode `uncompressSkyline()` fa la transformació oposada: converteix un skyline comprimit en una llista a un skyline representat amb un diccionari, i serà el mètode que utilitzarem al carregar skylines guardats.

## Enunciat

https://gebakx.github.io/SkylineBot/

## Autor

**Lucas Cajal**
[contact@lucascajal.com](mailto:contact@lucascajal.com)
www.lucascajal.com
