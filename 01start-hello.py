from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters


def start(update, context):
    update.message.reply_text('Привет!')


def main():
    updater = Updater("5101987677:AAHm9vcl71p0-h_ZdIX6Clcfb3hbcdhTec8")
    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()