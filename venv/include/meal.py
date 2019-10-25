from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlite3
import configparser
import datetime

config = configparser.ConfigParser()
config.read('config.ini')
db_address = config.get('global','DB_ADDRESS')
chat_id = config.get('global','CHAT_ID')

def meal_alert(context):
    now = datetime.datetime.now()
    hour = now.hour
    month = now.month
    day = now.day
    if 10 <= hour < 15 or 16 <= hour < 24 or 0 <= hour < 9:
        return 
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    if 9 <= hour < 10:
        message = "It's time to sign in for today's LUNCH!\n/Im_in\n/Im_out"
        cursor.execute('INSERT INTO meal(date, type, members) VALUES (?,?,?)', [str(month) + "." + str(day), "lunch", ""])
    elif 15 <= hour < 16:
        message = "It's time to sign in for today's DINNER!\n/Im_in\n/Im_out"
        cursor.execute('INSERT INTO meal(date, type, members) VALUES (?,?,?)',
                       [str(month) + "." + str(day), "dinner", ""])
        
    connection.commit()
    connection.close()
    context.bot.send_message(chat_id=chat_id, text=message)

def check_in(update, context):
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    cursor.execute("SELECT members FROM meal WHERE id = (SELECT max(id) FROM meal)")
    members = str(cursor.fetchone()[0])
    new_member = str(update.effective_user.id)
    if members is "":
        members = new_member
    elif new_member in members:
        pass
    else:
        members += " " + new_member
    number = members.count(" ") + 1
    cursor.execute("UPDATE meal set members=? WHERE id = (SELECT max(id) FROM meal)", [members])
    connection.commit()
    message = "Good! Currently " + str(number) + " people checked in."
    connection.close()
    context.bot.send_message(chat_id=chat_id, text=message)
    
def check_out(update, context):
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    cursor.execute("SELECT members FROM meal WHERE id = (SELECT max(id) FROM meal)")
    members = str(cursor.fetchone()[0]).replace(str(update.effective_user.id), "").replace("  ", " ") .rstrip().lstrip()
    if members is "":
        number = 0
    else:
        number = members.count(" ") + 1
    cursor.execute("UPDATE meal set members=? WHERE id = (SELECT max(id) FROM meal)", [members])
    connection.commit()
    message = "Pity! Currently " + str(number) + " people checked in."
    connection.close()
    context.bot.send_message(chat_id=chat_id, text=message)

