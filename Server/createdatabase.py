import sqlite3
import os
from constants import *


def remove_database(db_name: str = SERVER_DB):
    if os.path.exists(db_name):
        os.remove(db_name)
        print("An old database removed.")


def create_database():
    connection = sqlite3.connect(SERVER_DB)
    cursor = connection.cursor()

    cursor.execute(""" CREATE TABLE users (
        IdK text,
        Imie text,
        Nazwisko text,
        Entries int,
        Balance float,
        PRIMARY KEY (IdK)
    )""")

    cursor.execute(""" CREATE TABLE logs (
        idL INTEGER PRIMARY KEY AUTOINCREMENT,
        RfidCard text,
        Activity text,
        RegisterTime date,
        TerminalId text
    )""")

    # connection.commit()
    # connection.close()

    connention = sqlite3.connect(SERVER_DB)
    cursor = connention.cursor()
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0035124", "Krzysztof", "Mazowiecki", 0, 0))
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0135153", "Jan", "Kowalski", 0, 0))
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0235124", "Jerzy", "Malinowski", 0, 0))
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0316234", "Marian", "Wyszałkowski", 0, 0))
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0455321", "Zuzannaa", "Kulik", 0, 0))
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0525211", "Julia", "Gwoździewicz", 0, 0))
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0637451", "Jakub", "Galicki", 0, 0))
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                   ("0712412", "Adrian", "Maciaszek", 0, 0))
    connention.commit()
    connention.close()

    print("The new database created.")


if __name__ == '__main__':
    remove_database()
    create_database()
