import tkinter as tk
import customtkinter as ctk
import os
import sys
import animelist

COLOUR = '#3d7000'
HCOLOUR = '#2d5202'


class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.geometry('500x300')
        self.title('Shikimori parser')
        self.resizable(False, False)
        self.iconbitmap(self.resource_path("icon.ico"))

        self.main_frame = ctk.CTkFrame(master=self)
        self.main_frame.place(relheight=1, relwidth=1)

        self.iv_button = ctk.CTkButton(master=self.main_frame, text='Pars ivanko4456', font=('Arial', 20),
                                       command=lambda: animelist.main('ivanko4456', self.newtable.get()),
                                       fg_color=COLOUR, hover_color=HCOLOUR)
        self.iv_button.place(x=50, y=50)

        self.ah_button = ctk.CTkButton(master=self.main_frame, text='Pars AHMED2007RUS', font=('Arial', 20),
                                       command=lambda: animelist.main('AHMED2007RUS', self.newtable.get()),
                                       fg_color=COLOUR, hover_color=HCOLOUR)
        self.ah_button.place(x=220, y=50)

        self.nick_entry = ctk.CTkEntry(master=self.main_frame, font=('TimesNewRoman', 20),
                                       width=200, placeholder_text='enter username', border_color=COLOUR)
        self.nick_entry.place(x=150, y=150)

        self.pars_user_btn = ctk.CTkButton(master=self.main_frame, text='Pars user', font=('Arial', 20),
                                           command=lambda: animelist.main(self.nick_entry.get(), self.newtable.get()),
                                           width=200, fg_color=COLOUR, hover_color=HCOLOUR)
        self.pars_user_btn.place(x=150, y=200)

        self.newtable = tk.BooleanVar()
        self.new_table = ctk.CTkCheckBox(master=self.main_frame, text='Создавать новые таблицы', variable=self.newtable,
                                         onvalue=True, offvalue=False, border_color=COLOUR, fg_color=COLOUR,
                                         hover_color=HCOLOUR).place(x=150, y=235)

    @staticmethod
    def resource_path(relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


app = App()
app.mainloop()
