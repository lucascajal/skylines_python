from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ParseMode
from Antlr import Antlr

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    lang.clean()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Wassup my friend. Type /help for a list of commands")

def author(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Skyliner 2020!\nCreated by Lucas Cajal\nlucas.cajal@est.fib.upc.edu\nlucascajal.com")

def lst(update, context):
    keys = lang.lst()
    message = 'List of skylines and their area:'
    for element in keys:
        message += '\n   · ' + element + ' | area = ' + str(lang.getArea(element))
    if len(keys) == 0:
        message = 'There are currently no skylines defined'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message)

def clean(update, context):
    lang.clean()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="All identifiers erased!")

def save(update, context):
    lang.save(context.args[0])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Data saved!")

def load(update, context):
    lang.load(context.args[0])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Data loaded!")

def help(update, context):
    keyboard = [[InlineKeyboardButton("List commands", callback_data='List commands')],
                [InlineKeyboardButton("Language description", callback_data='Language description')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('What do you need help with?', reply_markup=reply_markup)

def printHelp(update, context):
    query = update.callback_query
    query.answer()
    info = ""
    if "{}".format(query.data) == "List commands":
        info = """*Avaliable commands:*

/start : Starts the session
/help : Display help
/author : Information about the author
/lst : List session skylines
/clean : Clear all skylines from session
/save : Save current session
/load : Load saved session"""
    else:
        info = """*Skyline management language*

*Skyline creation*
  · Single: \(xmin, h, xmax\)
xmin and xmax specify the initial and final position, and h the height of the buidling\. Example: \(1, 2, 3\)

  · Multiple: _NOT IMPLEMENTED YET_ \[\(xmin, h, xmax\), \(xmin, h, xmax\)\.\.\.\] 
Allows creating multiple buildings from a list of simple buildings\. Example: \[\(1, 2, 3\), \(3, 4, 6\)\]

  · Random: \{n, h, w, xmin, xmax\}
Creates n buildings, each one of them with a random height between 0 and h, a random width between 1 and w, and random initial and final positions between xmin and xmax\.

*Skyline operators*
  · skl \+ skl: union
  · skl \* skl: intersection
  · skl \* N: replication, N times
  · skl \+ N: move N positions to the right
  · skl \- N: move N positions to the left
  · \- skl: reflection

*Order of operators \(descending\)*
  · \( \)	parenthesis
  ·  \-	reflection
  ·  \*	intersection and replication
  · \+ \-	union and displacement
"""
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=info, 
        parse_mode='MarkdownV2')

def command(update, context):
    """Reads a code line and replies with the resulting skyline"""
    a, h = lang.send(update.message.text)
    if not a:
        update.message.reply_text("Wrong command")
    else:
        context.bot.send_photo(
            chat_id=update.effective_chat.id, 
            photo=open('/home/lucas/upc/LP/Python/bot/fig.png', 'rb'))
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="area: " + str(a) + "\nalçada: " + str(h))

lang = Antlr()

TOKEN = open('/home/lucas/upc/LP/Python/bot/token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

updater.dispatcher.add_handler(CallbackQueryHandler(printHelp)) # per respondre a click de help al inline keyboard

dispatcher.add_handler(CommandHandler('start', start)) # inicia la conversa amb el Bot
dispatcher.add_handler(CommandHandler('author', author)) # el Bot ha d’escriure el nom complet de l’autor del projecte i seu correu electrònic oficial de la facultat
dispatcher.add_handler(CommandHandler('help', help)) # el Bot ha de contestar amb una llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús

dispatcher.add_handler(CommandHandler('lst', lst)) # mostra els identificadors definits i la seva corresponent àrea
dispatcher.add_handler(CommandHandler('clean', clean)) # esborra tots els identificadors definits
dispatcher.add_handler(CommandHandler('save', save)) # ha de guardar un skyline definit amb el nom id.sky
dispatcher.add_handler(CommandHandler('load', load)) # ha de carregar un skyline de l’arxiu id.sky

dispatcher.add_handler(MessageHandler(Filters.text, command))

updater.start_polling()