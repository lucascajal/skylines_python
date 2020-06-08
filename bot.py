from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ParseMode
from Antlr import Antlr

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import sys

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
    chat_id = str(update.message.chat_id)
    if len(context.args) >= 1:
        for i in range(0, len(context.args)):
            a, h = lang.save(chat_id, context.args[i])
            if not a:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, 
                    text='*ERROR:* Variable "' + str(context.args[i]) + '" not declared\. Type /lst to see a list of declared variables', 
                    parse_mode='MarkdownV2')
            else:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='Variable "' + str(context.args[i]) + '" saved!')

    else:
        keyboard = []
        for key in lang.lst():
            keyboard.append([InlineKeyboardButton(key, callback_data=str(len(chat_id)) + chat_id + "_save_" +key)])

        if len(keyboard) == 0:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="There are no declared variables!")
        else:
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Which variable do you want to save?', reply_markup=reply_markup)

def load(update, context):
    chat_id = str(update.message.chat_id)
    if len(context.args) >= 1:
        for i in range(0, len(context.args)):
            a, h = lang.load(chat_id, context.args[i])
            if not a:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='*ERROR:* Skyline "' + str(context.args[i]) + '" not found\.\nType /load to see a list of avaliable files', 
                    parse_mode='MarkdownV2')
            else:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='Skyline "' + str(context.args[i]) + '" loaded\!',
                    parse_mode='MarkdownV2')
    else :
        keyboard = []
        path = str(os.path.abspath(os.path.dirname(sys.argv[0]))) + "/userData/"
        if os.path.isdir(path + chat_id):
            for file in os.listdir(path + chat_id):
                if file.endswith(".sky"):
                    name = file[:len(file)-4]
                    keyboard.append([InlineKeyboardButton(name, callback_data=str(len(chat_id)) + chat_id + name)])

        if len(keyboard) == 0:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="There are no saved skylines!")
        else:
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Which file do you want to load?', reply_markup=reply_markup)

def help(update, context):
    keyboard = [[InlineKeyboardButton("List commands", callback_data='List commands')],
                [InlineKeyboardButton("Language description", callback_data='Language description')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('What do you need help with?', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    text = ""
    if "{}".format(query.data) == "List commands":
        text = """*Avaliable commands:*

/start : Starts the session
/help : Display help
/author : Information about the author
/lst : List session skylines
/clean : Clear all skylines from session
/save : Save current session
/load : Load saved session"""
    elif "{}".format(query.data) == "Language description":
        text = """*Skyline management language*

*Skyline creation*
  · Single: \(xmin, h, xmax\)
xmin and xmax specify the initial and final position, and h the height of the buidling\. Example: \(1, 2, 3\)

  · Multiple: \[\(xmin, h, xmax\), \(xmin, h, xmax\)\.\.\.\] 
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
    else:
        callback = "{}".format(query.data)
        chat_id = callback[1:int(callback[0])+1]
        callback = callback[int(callback[0])+1:]

        if "_save_" == callback[:6]:
            lang.save(chat_id, callback[6:])
            text = "Variable saved\!"
        else:
            lang.load(chat_id, callback)
            text = "Skyline loaded\!"

    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=text, 
        parse_mode='MarkdownV2')

def command(update, context):
    """Reads a code line and replies with the resulting skyline"""
    chat_id = str(update.message.chat_id)
    a, h = lang.send(update.message.text, chat_id)
    if not a:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='*ERROR:* ' + h,
            parse_mode='MarkdownV2')
    else:
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open('/home/lucas/upc/LP/Python/userData/' + chat_id + '/fig.png', 'rb'))
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="area: " + str(h[0][0]) + "\nalçada: " + str(h[0][1]))

lang = Antlr()

TOKEN = open('/home/lucas/upc/LP/Python/bot/token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CallbackQueryHandler(button)) # per respondre a click de help al inline keyboard

dispatcher.add_handler(CommandHandler('start', start)) # inicia la conversa amb el Bot
dispatcher.add_handler(CommandHandler('author', author)) # el Bot ha d’escriure el nom complet de l’autor del projecte i seu correu electrònic oficial de la facultat
dispatcher.add_handler(CommandHandler('help', help)) # el Bot ha de contestar amb una llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús

dispatcher.add_handler(CommandHandler('lst', lst)) # mostra els identificadors definits i la seva corresponent àrea
dispatcher.add_handler(CommandHandler('clean', clean)) # esborra tots els identificadors definits
dispatcher.add_handler(CommandHandler('save', save)) # ha de guardar un skyline definit amb el nom id.sky
dispatcher.add_handler(CommandHandler('load', load)) # ha de carregar un skyline de l’arxiu id.sky

dispatcher.add_handler(MessageHandler(Filters.text, command))

updater.start_polling()
