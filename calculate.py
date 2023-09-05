from typing import Optional, Tuple, Union
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
from settings import *
import customtkinter as ctk
import darkdetect

class Calculator(ctk.CTk):

    def __init__(self, is_dark) -> None:

        # main window setup
        super().__init__(fg_color = (WHITE, BLACK))
        ctk.set_appearance_mode(f"{'dark' if is_dark else 'light'}")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.title('')
        self.iconbitmap('calc-icon.ico')
        
        # grid layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLS)), weight=1, uniform='a')

        # widgets
        self.createWidgets()

        self.mainloop()

    def createWidgets(self):
        OutputLabel(self, 0)
        OutputLabel(self, 1)

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row):
        super().__init__(master = parent, text='123')
        self.grid(column = 0, columnspan = 4, row = row)

if __name__ == '__main__':

    Calculator(darkdetect.isDark())