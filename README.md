# Pràctica de Python: Skyline bot

Bot de Telegram programat en python per poder crear i gestionar skylines.

## Utilització

### Prerequisits

Les llibreries necessàries per executar el bot es troben llistades dins el fitxer ```requirements.txt```, i es poden instalar utilitzant ```pip``` executant la comanda
```bash
> pip3 install -r requirements.txt
```

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
