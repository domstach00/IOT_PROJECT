from constants import *
import tkinter
import sqlite3


class ServerScreen:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry(SCREEN_GEOMETRY)
        self.window.title(SCREEN_TITLE)

    def create_main_window(self):
        self.label = tkinter.Label(self.window, text="Listening to the MQTT")
        self.exit_button = tkinter.Button(self.window, text="Stop", command=lambda: self.window.quit())
        self.print_log_button = tkinter.Button(self.window, text="Print logs", command=lambda: self.show_logs())
        self.print_users = tkinter.Button(self.window, text="Print users", command=lambda: self.show_users())

        self.label.pack()
        self.exit_button.pack(side="right")
        self.print_log_button.pack(side="right")
        self.print_users.pack(side="right")

    def show_logs(self):
        self.window_logs = tkinter.Tk()
        self.connection = sqlite3.connect(SERVER_DB)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM logs")
        self.log_entrys = self.cursor.fetchall()
        self.labels_log_entry = []

        for log_entry in self.log_entrys:
            self.labels_log_entry.append(tkinter.Label(self.window_logs, text=(
                f"RFIDCard: {log_entry[1]} Activity: {log_entry[2]} RegisterTime: {log_entry[3]} TerminalId: {log_entry[4]} "
            )))

        for label in self.labels_log_entry:
            label.pack(side="top")

        self.connection.commit()
        self.connection.close()
        # Display this window.
        self.window_logs.mainloop()

    def show_users(self):
        self.window_users = tkinter.Tk()
        self.connection_2 = sqlite3.connect(SERVER_DB)
        self.cursor_2 = self.connection_2.cursor()
        self.cursor_2.execute("SELECT * FROM users")
        self.user_entrys = self.cursor_2.fetchall()
        self.labels_user_entry = []

        for user_entry in self.user_entrys:
            self.labels_user_entry.append(tkinter.Label(self.window_users, text=(
                f"IdK: {user_entry[0]} Imie: {user_entry[1]} Nazwisko: {user_entry[2]} Entries: {user_entry[3]} Balance: {user_entry[4]} zł")))

        for label in self.labels_user_entry:
            label.pack(side="top")

        self.connection_2.commit()
        self.connection_2.close()
        # Display this window.
        self.window_users.mainloop()


def main():
    server_screen = ServerScreen()
    server_screen.create_main_window()
    server_screen.window.mainloop()


if __name__ == '__main__':
    main()
