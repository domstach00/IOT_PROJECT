from constants import *
import tkinter
from sender import *
from supporting_methods import *


class TerminalScreen:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry(SCREEN_GEOMETRY)
        self.window.title(SCREEN_TITLE)

    def create_entry_window(self):
        self.enter_btn = tkinter.Button(self.window, text="Enter",
                                        command=lambda: self.enter())
        self.escape_btn = tkinter.Button(self.window, text="Escape",
                                         command=lambda: self.escape())
        self.intro_label = tkinter.Label(self.window, text="Use card")
        self.intro_label.grid(row=0, columnspan=5)
        self.enter_btn.grid(row=1, column=0)
        self.escape_btn.grid(row=2, column=0)
        self.window.mainloop()

    def enter(self):
        self.id_card = read_rfid()
        self.create_chose_activity_window()

    def escape(self):
        self.enter_btn.destroy()
        self.escape_btn.destroy()
        send_log(self.id_card, "ESCAPE")
        self.id_card = find_used_card()
        self.create_end_window()

    def create_chose_activity_window(self):
        self.enter_btn.destroy()
        self.escape_btn.destroy()
        self.intro_label.destroy()

        self.intro_label = tkinter.Label(self.window, text="Chose activity")
        self.intro_label.grid(row=0, columnspan=5)
        self.activity_1_btn = tkinter.Button(self.window, text="Pool",
                                             command=lambda: self.action_after_activity("Pool"))
        self.activity_2_btn = tkinter.Button(self.window, text="Gym",
                                             command=lambda: self.action_after_activity("Gym"))
        self.activity_3_btn = tkinter.Button(self.window, text="Squash",
                                             command=lambda: self.action_after_activity("Squash"))
        self.activity_4_btn = tkinter.Button(self.window, text="Badminton",
                                             command=lambda: self.action_after_activity("Badminton"))
        self.activity_5_btn = tkinter.Button(self.window, text="Climbing",
                                             command=lambda: self.action_after_activity("Climbing"))
        self.activity_1_btn.grid(row=1, column=4)
        self.activity_2_btn.grid(row=2, column=4)
        self.activity_3_btn.grid(row=3, column=4)
        self.activity_4_btn.grid(row=4, column=4)
        self.activity_5_btn.grid(row=5, column=4)

    def action_after_activity(self, activity: str):
        send_log(card=self.id_card, activity=activity)
        self.create_end_window()

    def create_end_window(self):
        self.activity_1_btn.destroy()
        self.activity_2_btn.destroy()
        self.activity_3_btn.destroy()
        self.activity_4_btn.destroy()
        self.activity_5_btn.destroy()
        self.intro_label.destroy()
        self.intro_label = tkinter.Label(self.window, text="Have a nice day")
        self.intro_label.grid(row=0, columnspan=5)
        self.back_btn = tkinter.Button(self.window, text="Back to main window",
                                       command=lambda: self.end_function())
        self.back_btn.grid(row=1, column=4)

    def end_function(self):
        self.back_btn.destroy()
        self.intro_label.destroy()
        self.create_entry_window()


def main():
    view = TerminalScreen()
    view.create_entry_window()
    view.window.mainloop()
