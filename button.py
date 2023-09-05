import tkinter
from typing import Callable, Optional, Tuple, Union
from customtkinter import CTkButton
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
from settings import *

class Button(CTkButton):
    def __init__(self, parent, row, column, funct, text, font, color):
        super().__init__(
            master = parent, 
            text = text,
            command = funct,
            corner_radius=STYLING['corner-radius'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text'])
        self.grid(column = column, row = row, sticky = 'NSEW', padx = STYLING['gap'], pady = STYLING['gap'])