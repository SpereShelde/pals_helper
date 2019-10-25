from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import sqlite3
import logging
import datetime
from meal import *
from stock import *
from bill import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
db_address = config.get('global','DB_ADDRESS')
chat_id = config.get('global','CHAT_ID')

# def hello(update, context):
#     # context.bot.send_message(chat_id=update.effective_chat.id, text='Hello {}'.format(update.message.from_user.first_name))
#     update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

def check_mention(message):
    if message.rstrip().lstrip().startswith("@PalsHelperBot "):
        return True
    else:
        return False

def housekeeper(update, context):

    menu = "Hi, i'm here.\nWhat can I do for you?\n/menu View main menu\n/stock Query food stock\n/add_stock Update food stock\n/check_bill Check my bill"
    context.bot.send_message(chat_id=chat_id,
                             text=menu)

def housekeeper_chat(update, context):
    # print(update.effective_chat.id)
    if update.message.text.rstrip().lstrip() == "@PalsHelperBot":
        context.bot.send_message(chat_id=chat_id, text="WTF are you saying???")
    if update.message.text.rstrip().lstrip().startswith("@PalsHelperBot "):
        context.bot.send_message(chat_id=chat_id,
                                 text=update.message.text.replace("@PalsHelperBot ", " "))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.ERROR)

updater = Updater('', use_context=True)

# job = updater.job_queue
# job_minute = job.run_repeating(meal_alert, interval=3600, first=0)

updater.job_queue.run_repeating(meal_alert, interval=3600, first=1)

updater.dispatcher.add_handler(CommandHandler('menu', housekeeper))
# updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('stock', stock))
updater.dispatcher.add_handler(CommandHandler('add_stock', add_stock))
updater.dispatcher.add_handler(CommandHandler('chicken_wings', chicken_wings))
updater.dispatcher.add_handler(CommandHandler('chicken_thigh', chicken_thigh))
updater.dispatcher.add_handler(CommandHandler('chicken_breast', chicken_breast))
updater.dispatcher.add_handler(CommandHandler('pork_belly_strip', pork_belly_strip))
updater.dispatcher.add_handler(CommandHandler('pork_belly_slices', pork_belly_slices))
updater.dispatcher.add_handler(CommandHandler('pork_loin', pork_loin))
updater.dispatcher.add_handler(CommandHandler('pork_ribs', pork_ribs))
updater.dispatcher.add_handler(CommandHandler('lamp_chops', lamp_chops))
updater.dispatcher.add_handler(CommandHandler('beef_tenderloin', beef_tenderloin))
updater.dispatcher.add_handler(CommandHandler('beef', beef))
updater.dispatcher.add_handler(CommandHandler('add_chicken_wings', add_chicken_wings))
updater.dispatcher.add_handler(CommandHandler('add_chicken_thigh', add_chicken_thigh))
updater.dispatcher.add_handler(CommandHandler('add_chicken_breast', add_chicken_breast))
updater.dispatcher.add_handler(CommandHandler('add_pork_belly_strip', add_pork_belly_strip))
updater.dispatcher.add_handler(CommandHandler('add_pork_belly_slices', add_pork_belly_slices))
updater.dispatcher.add_handler(CommandHandler('add_pork_loin', add_pork_loin))
updater.dispatcher.add_handler(CommandHandler('add_pork_ribs', add_pork_ribs))
updater.dispatcher.add_handler(CommandHandler('add_lamp_chops', add_lamp_chops))
updater.dispatcher.add_handler(CommandHandler('add_beef_tenderloin', add_beef_tenderloin))
updater.dispatcher.add_handler(CommandHandler('add_beef', add_beef))
updater.dispatcher.add_handler(CommandHandler('redu_chicken_wings', redu_chicken_wings))
updater.dispatcher.add_handler(CommandHandler('redu_chicken_thigh', redu_chicken_thigh))
updater.dispatcher.add_handler(CommandHandler('redu_chicken_breast', redu_chicken_breast))
updater.dispatcher.add_handler(CommandHandler('redu_pork_belly_strip', redu_pork_belly_strip))
updater.dispatcher.add_handler(CommandHandler('redu_pork_belly_slices', redu_pork_belly_slices))
updater.dispatcher.add_handler(CommandHandler('redu_pork_loin', redu_pork_loin))
updater.dispatcher.add_handler(CommandHandler('redu_pork_ribs', redu_pork_ribs))
updater.dispatcher.add_handler(CommandHandler('redu_lamp_chops', redu_lamp_chops))
updater.dispatcher.add_handler(CommandHandler('redu_beef_tenderloin', redu_beef_tenderloin))
updater.dispatcher.add_handler(CommandHandler('redu_beef', redu_beef))
updater.dispatcher.add_handler(CommandHandler('Im_in', check_in))
updater.dispatcher.add_handler(CommandHandler('Im_out', check_out))
updater.dispatcher.add_handler(CommandHandler('bill', bill))
updater.dispatcher.add_handler(CommandHandler('check_bill', check_bill))
updater.dispatcher.add_handler(MessageHandler(Filters.text, housekeeper_chat))

updater.start_polling()
updater.idle()
