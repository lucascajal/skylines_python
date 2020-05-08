from telegram.ext import Updater, CommandHandler


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Wassup my friend. Type /help for a list of commands")

def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Avaliable commands: /start, /help and /random.")


def random(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, 
        photo='https://lh6.googleusercontent.com/-Jt_ZGBdd3vc/TxmmvpAG1TI/AAAAAAAABNI/mpDhvs85XCc/w130-h170-n-k/P1040327.JPG')


TOKEN = open('bot/token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('random', random))

updater.start_polling()