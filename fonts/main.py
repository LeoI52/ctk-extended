"""
@author : Léo IMBERT
@created : 16/11/2024
@updated : 23/12/2025
"""

import customtkinter as ctk
import tkinter.font as tkFont

class App(ctk.CTk):

    def __init__(self):
        super().__init__("#212121")
        self.title("CTkinter Fonts Viewer")
        self.geometry("1270x650+75+50")

        self.frame = ctk.CTkScrollableFrame(self)
        self.frame.place(relx=0.5, y=0, anchor="n", relheight=1, relwidth=0.6)

        fonts = sorted(tkFont.families())

        for font in fonts:
            ctk.CTkLabel(self.frame, text=font, font=(font, 30)).pack()

        self.bind("<Escape>", lambda _: self.quit())
        self.mainloop()

if __name__ == "__main__":
    App()