# Optimización:
getSkyline: no hacer copia siempre, devolver referencia. Hacer copia de la referencia sólo cuando sea necesario.

interseccion: iterar por el skyline más corto, no skyline2.
# Pràctica de Python: Skyline bot

Bot de Telegram programat en python per poder crear i gestionar skylines.

## Utilització

### Prerequisits

Les llibreries necessàries per executar el bot es troben llistades dins el fitxer ```requirements.txt```, i es poden instalar utilitzant ```pip``` executant la comanda
```bash
> pip3 install -r requirements.txt
```
També cal tenir un *Acces token*, que és un identificador que Telegram dona per identificar cada bot. Per obtenir-lo:
  - Entrem a [@BotFather](https://telegram.me/botfather)
  - Utilitzem la `comanda newbot` i donem la informació demanada (nom complet i nom d'usuari del bot, que ha d'acabar amb `bot`).
  - Desem a un fitxer `token.txt` el nostre *access token*, que té un aspecte com ara `U10201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`. Aquest fitxer s'ha de guardar al mateix directori on es troba el nostre programa ```bot.py```.

Les instruccions completes per crear bots són a https://core.telegram.org/bots#6-botfather.


### Execució

Per executar el programa, només cal utilitzar la comanda
```bash
> python3 bot.py
```
### Comandes del bot

El nostre bot disposa de diverses comandes:
- `/start`: Inicia la conversa amb el bot
- `/help`: El bot ens demanarà amb què necessitem ajuda, i segons la nostra resposta ens contestarà amb l'explicacio de les comandes o el llenguatge per gestionar skylines.
- `/author`: El bot respon amb l'informació sobre el seu autor.
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

__(Borrar y poner solo en las op que sea necesario??) Cal notar que degut a la naturalesa del llenguatge, cada vegada que realitzem una operacio a un skyline no volem modificar aquest, si no que volem generar-ne un de nou. Per tant, a totes les operacions hem de crear una copia de l'*skyline* original sobre el que després farem modificacions. Aquesta copia té un cost de `O(n)`, on `n` és el nombre d'entrades dins del diccionari que representa l'*skyline*, i serà el *bottleneck* de les nostres operacions.__

estructura diccionari: 
  ocupa més en memoria de programa, però execució molt més ràpida
compressió i descompressió per guardar/carregar/imprimir: 
  matplotlib no peta, transforma estructura per optimitzar espai, ja que no s'han de fer càlculs -> menys memòria persistent

#### Unió
Aquesta operació realitza la unió de dos skylines. Per exemple, si executem `a := b + c`, l'*skyline* `a` serà la unió de `b` i `c`.

Per fer aquesta operació, primer fem una copia del primer *skyline* de l'operació, per tal d'evitar modificar aquest durant l'execució. Llavors, per a cada element dins el diccionari del segon skyline, si a la copia ja existeix una entrada amb la mateixa clau, li assignem com a valor el màxim entre el valor actual i el valor al segon skyline. Si no existeix l'entrada, afegim aquest element a la nostra copia. 

Degut a que el cost de consultar o modificar una entrada al diccionari és `O(1)`, i fem aquest procés per a cada element del segon diccionari, el cost serà `O(m)`, on `m` és el nombre d'elements del segon diccionari. Si sumem la complexitat de la copia obligatòria del primer diccionari, el cost total d'aquesta operació és `O(n) + O(m) = O(n+m)`.

Si comparem el cost amb el que s'hauria obtingut en cas d'utilitzar una llista d'edificis com a estructura de dades, podem veure que hauríem mantingut el cost de la copia `O(n)`, i per fer la unió hauríem d'implementar una búsqueda binària, de cost `O(log n)`, i per a cada inserció dins la llista pagar un cost `O(n)`, ja que com cal mantenir la llista ordenada, no podem inserir l'element al final d'aquesta, ho hem de fer a la posició corresponent. Per tant, el cost de l'operació seria `O(n) + O(n log n) = O(n log n)`.

#### Intersecció
Aquesta operació realitza la intersecció de dos skylines. Per exemple, si executem `a := b + c`, l'*skyline* `a` serà la intersecció de `b` i `c`.

Gràcies a la nostra implementació de *skyline* amb un diccionari, aquesta operació és pràcticament igual que la unió, on només fem 2 petits canvis. En comptes de fer una copia 

#### Replicació
metodologia
cost

#### Desplaçament
metodologia
cost

#### Mirall
metodologia
cost

#### Càlcul de l'àrea i alçada de l'*skyline*

#### Compressió de l'*skyline*

## Referències

https://wiki.python.org/moin/TimeComplexity

## Enunciat

https://gebakx.github.io/SkylineBot/

## Autor

**Lucas Cajal**

www.lucascajal.com
