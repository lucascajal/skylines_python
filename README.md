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

### La classe Skyline
estructura diccionari: 
  ocupa més en memoria de programa, però execució molt més ràpida
compressió i descompressió per guardar/carregar/imprimir: 
  matplotlib no peta, transforma estructura per optimitzar espai, ja que no s'han de fer càlculs -> menys memòria persistent

#### Unió
metodologia
cost

#### Intersecció
metodologia
cost

#### Replicació
metodologia
cost

#### Desplaçament
metodologia
cost

#### Mirall
metodologia
cost

## Referències

## Enunciat

https://gebakx.github.io/SkylineBot/

## Autor

**Lucas Cajal**

www.lucascajal.com
