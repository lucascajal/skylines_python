from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Antlr import Antlr

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Wassup my friend. Type /help for a list of commands")

def author(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Skyliner 2020!\nCreated by Lucas Cajal\nlucascajal.com")

def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Avaliable commands: /start, /help and /author.")

def echo(update, context):
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

TOKEN = open('bot/token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('help', help))

dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()