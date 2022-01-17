#!/usr/bin/env python3
import datetime
from datetime import datetime
import paho.mqtt.client as mqtt
from constants import *
import sqlite3
import serverscreen

# The MQTT client.
client = mqtt.Client()


def process_message(client, userdata, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(".")

    # Used for Deleting all blank spaces from recieved MESSAGE
    for index in range(len(message_decoded)):
        message_decoded[index] = message_decoded[index].strip()

    connection = sqlite3.connect("SERVER_DB.db")
    cursor = connection.cursor()

    # DEBUG STUFF GETTING USER
    user = cursor.execute(f'SELECT * FROM users WHERE IdK = "{message_decoded[0].strip()}"').fetchall()
    print(user)

    # INSERTING NEW LOG TO LOG DATA-BASE
    cursor.execute("INSERT INTO logs (RfidCard, Activity, RegisterTime, TerminalId) VALUES (?,?,?,?)",
                   (message_decoded[0], message_decoded[1], message_decoded[2], message_decoded[3]))
    connection.commit()

    # ACTIVITY ESCAPE MEANS THAT THE USER HAS JUST LEFT THE SPORT CENTER
    if message_decoded[1].strip() == "ESCAPE":
        # GETTING USER FEE TO PAY
        balance = cursor.execute(f"SELECT Balance FROM users WHERE IdK LIKE '{message_decoded[0]}'").fetchall()[0][0]

        # 2 LAST LOGS THAT USER HAD MADE (IN AND OUT)
        timeLogs = cursor.execute(
            f"SELECT * FROM (SELECT * FROM logs WHERE RfidCard LIKE '{message_decoded[0]}' ORDER BY idL DESC LIMIT 2) ORDER BY idL ASC").fetchall()

        entryTime = datetime.strptime(timeLogs[0][3], '%d/%m/%Y %H:%M:%S')
        exitTime = datetime.strptime(timeLogs[1][3], '%d/%m/%Y %H:%M:%S')
        timeDifference = (exitTime - entryTime).total_seconds()

        print(f"Opłata za usługę: {timeLogs[0][2]} wynosi: {Activities.get(timeLogs[0][2])}")
        print(f" Kara: {apply_fee(timeDifference)} minęło: {timeDifference}")

        balance += Activities.get(timeLogs[0][2]) + apply_fee(timeDifference)
        cursor.execute(f'UPDATE users SET Balance = {balance} WHERE IdK = "{message_decoded[0].strip()}"')
        cursor.execute(f'UPDATE users SET Entries = 0 WHERE IdK = "{message_decoded[0].strip()}"')

    else:
        cursor.execute(f'UPDATE users SET Entries = 1 WHERE IdK = "{message_decoded[0].strip()}"')
    connection.commit()
    connection.close()


def apply_fee(time_difference):
    if time_difference < 30.0:
        return 0.0
    elif 30.0 <= time_difference < 50.0:
        return PENALTY_1
    elif 50.0 <= time_difference < 70:
        return PENALTY_2
    elif 70.0 <= time_difference < 100:
        return PENALTY_3
    else:
        return PENALTY_4


def connect_to_broker():
    # Connect to the broker.
    client.connect(BROKER)
    # Send message about conenction.
    client.on_message = process_message
    # Starts client and subscribe.
    client.loop_start()
    client.subscribe(SUBSCRIBE)


def disconnect_from_broker():
    # Disconnet the client.
    client.loop_stop()
    client.disconnect()


def run_receiver():
    connect_to_broker()
    serverscreen.main()
    # Start to display window (It will stay here until window is displayed)
    disconnect_from_broker()


if __name__ == "__main__":
    run_receiver()
