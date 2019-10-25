from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlite3
import configparser
import datetime

config = configparser.ConfigParser()
config.read('config.ini')
db_address = config.get('global','DB_ADDRESS')
chat_id = config.get('global','CHAT_ID')

def bill(update, context):
    if len(context.args) == 0:
        update.message.reply_text("empty")
        return
    else:
        now = datetime.datetime.now()
        hour = now.hour
        month = now.month
        day = now.day
        connection = sqlite3.connect(db_address)
        cursor = connection.cursor()
        payers = context.args[1:-1]
        remark = context.args[-1]
        balance = float(context.args[0]) / (len(payers) + 1)
        for payer in payers:
            cursor.execute('SELECT user_id FROM user WHERE code = ?', payer.upper())
            user_id = cursor.fetchone()[0]
            if user_id is None:
                message = "Contain invalid payer code. Please rewrite."
                context.bot.send_message(chat_id=chat_id,
                                         text=message)
                connection.close()
                return
            else:
                cursor.execute('INSERT INTO bill(payee_id, payer_id, balance, time, done, remark) VALUES (?, ?, ?, ?, ?, ?)', (update.effective_user.id, user_id, balance, ".".join([str(month), str(day), str(hour)]), 0, remark))
                connection.commit()
        message = "Bill recorded!\n/check_bill check bill"
        context.bot.send_message(chat_id=chat_id,
                                     text=message)
        connection.close()

def check_bill(update, context):
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    cursor.execute('SELECT user_id, name FROM user WHERE user_id != ?', (update.effective_user.id,))
    users = cursor.fetchall()
    balances = {}
    for user in users:
        cursor.execute('SELECT sum(balance) FROM bill WHERE payee_id = ? and payer_id = ? and done = 0', (update.effective_user.id, user[0]))
        result = cursor.fetchone()
        if result[0] is not None:
            balance = float(result[0])
        else:
            balance = 0
        cursor.execute('SELECT sum(balance) FROM bill WHERE payee_id = ? and payer_id = ? and done = 0',
                       (user[0], update.effective_user.id))
        result = cursor.fetchone()
        if result[0] is not None:
            balances[user[1]] = balance - float(result[0])
        else:
            balances[user[1]] = balance - 0
        connection.commit()
    connection.close()
    message = update.effective_user.username + ", here is the list of balance."
    for (key,value) in balances.items():
        if value > 0:
            message += "\n" + key + " owe you $" + str(round(value, 2))
        elif value == 0 :
            message += "\nyou and " + key + " are good."
        else:
            message += "\nyou owe " + key + " $" + str(round(value, 2))
    # message += "\n/pay_your_bill"
    context.bot.send_message(chat_id=chat_id, text=message)

# def ay_your_bill(update, context):
#     pass