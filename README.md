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
  - Save inside a `token.txt` file the received *access token*, which will look something like `U10201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`. This file must be saved inside the same directory where the program `bot.py`is located.

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
- `/lst`: Lists all declared variables in current session
- `/clean`: Clears all variables of current session
- `/save [skyline1, skyline2, ...]`: Saves the variables specified as parameters. If no variable names are given, the bot lists all declared variables so the user can select which ones will be saved.
- `/load [skyline1, skyline2, ...]`: Loads the variables specified as parameters. If no variable names are given, the bot lists all saved variables so the user can select which ones will be loaded.

### Skyline management language

The language allows us to perform the following operations:
- Building creation:
  - Simple: `(xmin, height, xmax)` where `xmin` i `xmax` specify the starting and ending position of the building, and `height` the height of the buidling. Example: `(1, 2, 3)`.
  - Multiple: `[(xmin, height, xmax), ...]` allows to create multiple buidlings using a list of simple buildings. Example: `[(1, 2, 3), (3, 4, 6)]` or `[(1, 1, 2), (1000000000000, 1, 1000000000001)]`.
  - Random: `{n, h, w, xmin, xmax}` creates `n` buildings, each one of them with a random height between 0 and `h`, a random width between 1 and `w`, and random starting and ending positions between `xmin` and `xmax`.

- Skyline operators:
  - `skyline + skyline`: union
  - `skyline * skyline`: intersection
  - `skyline * N`: replication (`N` times)
  - `skyline + N`: displacement to the right by `N` positions
  - `skyline - N`: displacement to the left by `N` positions
  - `- skyline`: reflection

The following table shows the operator priority, from greater to smaller:

_**Operator**_ | _**Description**_
------------ | -------------
`( )` | Parenthesis
`-` | Reflection
`*` | Intersection and replication
`+` `-` | Union and displacement

- Variables:

The language allows the declaration of variables, which can be declared with the `:=` operator. Example: `a := (1, 2, 3)`. These variables can be permanently saved and later retreived, otherwise they will only last in memory during the program's execution.

## Original problem statement

https://gebakx.github.io/SkylineBot/ (In catalan)

## Author

**Lucas Cajal**

[contact@lucascajal.com](mailto:contact@lucascajal.com)

www.lucascajal.com
