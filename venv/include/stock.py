from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlite3
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
db_address = config.get('global','DB_ADDRESS')
chat_id = config.get('global','CHAT_ID')

def stock(update, context):
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM storage')
    storage = cursor.fetchall()
    message = "Here is the list of stock."
    for food in storage:
        # print(food)
        message += "\n/"+str(food[1]).replace(" ", "_")+":\t"+str(food[3])+" left"
    connection.close()
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def update_stock_database(name, operation):
    #operation = -1 or 1
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    cursor.execute("UPDATE storage set stock=stock+? WHERE name=?", [operation, name])
    connection.commit()
    cursor.execute("SELECT stock FROM storage WHERE name=?", [name])
    stock = cursor.fetchone()[0]
    connection.close()

    return str(stock)

def chicken_wings(update, context):
    message = "Need edit stock?\n/add_chicken_wings: add 1\n/redu_chicken_wings: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_chicken_wings(update, context):
    stock = update_stock_database("chicken wings", 1)
    message = "Success!\nChicken wings: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)
def redu_chicken_wings(update, context):
    stock = update_stock_database("chicken wings", -1)
    message = "Success!\nChicken wings: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def chicken_thigh(update, context):
    message = "Need edit stock?\n/add_chicken_thigh: add 1\n/redu_chicken_thigh: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_chicken_thigh(update, context):
    stock = update_stock_database("chicken thigh", 1)
    message = "Success!\nChicken thigh: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_chicken_thigh(update, context):
    stock = update_stock_database("chicken thigh", -1)
    message = "Success!\nChicken thigh: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def chicken_breast(update, context):
    message = "Need edit stock?\n/add_chicken_breast: add 1\n/redu_chicken_breast: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_chicken_breast(update, context):
    stock = update_stock_database("chicken breast", 1)
    message = "Success!\nChicken breast: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_chicken_breast(update, context):
    stock = update_stock_database("chicken breast", -1)
    message = "Success!\nChicken breast: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def pork_belly_strip(update, context):
    message = "Need edit stock?\n/add_pork_belly_strip: add 1\n/redu_pork_belly_strip: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_pork_belly_strip(update, context):
    stock = update_stock_database("pork belly strip", 1)
    message = "Success!\nPork belly strip: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_pork_belly_strip(update, context):
    stock = update_stock_database("pork belly strip", -1)
    message = "Success!\nPork belly strip: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def pork_belly_slices(update, context):
    message = "Need edit stock?\n/add_pork_belly_slices: add 1\n/redu_pork_belly_slices: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_pork_belly_slices(update, context):
    stock = update_stock_database("pork belly slices", 1)
    message = "Success!\nPork belly slices: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_pork_belly_slices(update, context):
    stock = update_stock_database("pork belly slices", -1)
    message = "Success!\nPork belly slices: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def pork_loin(update, context):
    message = "Need edit stock?\n/add_pork_loin: add 1\n/redu_pork_loin: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_pork_loin(update, context):
    stock = update_stock_database("pork loin", 1)
    message = "Success!\nPork loin: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_pork_loin(update, context):
    stock = update_stock_database("pork loin", -11)
    message = "Success!\nPork loin: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def pork_ribs(update, context):
    message = "Need edit stock?\n/add_pork_ribs: add 1\n/redu_pork_ribs: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_pork_ribs(update, context):
    stock = update_stock_database("pork ribs", 1)
    message = "Success!\nPork ribs: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_pork_ribs(update, context):
    stock = update_stock_database("pork ribs", - 1)
    message = "Success!\nPork ribs: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def lamp_chops(update, context):
    message = "Need edit stock?\n/add_lamp_chops: add 1\n/redu_lamp_chops: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_lamp_chops(update, context):
    stock = update_stock_database("lamp chops", 1)
    message = "Success!\nLamp chops: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_lamp_chops(update, context):
    stock = update_stock_database("lamp chops", -1)
    message = "Success!\nLamp chops: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def lamp(update, context):
    message = "Need edit stock?\n/add_lamp: add 1\n/redu_lamp: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_lamp(update, context):
    stock = update_stock_database("lamp", 1)
    message = "Success!\nLamp: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_lamp(update, context):
    stock = update_stock_database("lamp", -1)
    message = "Success!\nLamp: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def beef_tenderloin(update, context):
    message = "Need edit stock?\n/add_beef_tenderloin: add 1\n/redu_beef_tenderloin: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_beef_tenderloin(update, context):
    stock = update_stock_database("beef tenderloin", 1)
    message = "Success!\nBeef tenderloin: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_beef_tenderloin(update, context):
    stock = update_stock_database("beef tenderloin", -1)
    message = "Success!\nBeef tenderloin: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def beef(update, context):
    message = "Need edit stock?\n/add_beef: add 1\n/redu_beef: reduce 1"
    print(message)
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_beef(update, context):
    stock = update_stock_database("beef", 1)
    message = "Success!\nBeef: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def redu_beef(update, context):
    stock = update_stock_database("beef", -1)
    message = "Success!\nBeef: " + stock + " left"
    context.bot.send_message(chat_id=chat_id,
                             text=message)

def add_stock(update, context):
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM storage')
    storage = cursor.fetchall()
    message = "What kind of food stock need add?"
    for food in storage:
        message +="\n/add_"+str(food[1]).replace(" ","_")+":\t"+str(food[3])+" left"
    connection.close()
    context.bot.send_message(chat_id=chat_id,
                             text=message)