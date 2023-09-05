from button import Button, NumberButton, MathButton
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
from settings import *
import math
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

        # data
        self.output_string = ctk.StringVar(value = '0')
        self.formula_string = ctk.StringVar(value = '')
        self.display_chars = []
        self.full_op = []

        # widgets
        self.createWidgets()

        self.mainloop()

    def createWidgets(self):

        main_font = CTkFont(family = FONT_STYLE, size=FONT_SIZE)
        output_font = CTkFont(family = FONT_STYLE, size=OUTPUT_FONT_SIZE)


        OutputLabel(self, 0, 'SE', main_font, self.formula_string) # formula cell
        OutputLabel(self, 1, 'E', output_font, self.output_string) # output cell

        for operation in OPERATIONS_POSITION:
            Button(
                parent = self, 
                funct = eval(f"self.{operation}"),
                row = OPERATIONS_POSITION[operation]['row'], 
                col = OPERATIONS_POSITION[operation]['col'], 
                text = OPERATIONS_POSITION[operation]['text'],
                font = main_font,
                color = 'dark-gray')
            
        for number in NUMBER_POSITION:
            NumberButton(
                parent = self,
                text = number,
                funct = self.NumberPress,
                # funct = eval(f"self.{operation}"),
                row = NUMBER_POSITION[number]['row'], 
                col = NUMBER_POSITION[number]['col'], 
                font = main_font,
                color= 'light-gray')
            
        for symbol in SYMBOLS_POSITION:
            MathButton(
                parent = self,
                funct = self.MathPress,
                row = SYMBOLS_POSITION[symbol]['row'], 
                col = SYMBOLS_POSITION[symbol]['col'], 
                text = SYMBOLS_POSITION[symbol]['character'],
                operator = SYMBOLS_POSITION[symbol]['operator'],
                font = main_font,
                color= 'orange')
        
    def NumberPress(self, value):
        self.display_chars.append(str(value))
        number = ''.join(self.display_chars)
        self.formula_string.set(number)

    def MathPress(self, value):
        current_number = ''.join(self.display_chars)

        if current_number:
            self.full_op.append(current_number)

            if value != '=':
                self.full_op.append(value)
                self.display_chars = []
                self.formula_string.set(''.join(self.full_op))
                
            else:
                self.output_string.set(eval(''.join(self.full_op)))
        
    def clear(self):
        self.formula_string.set('')
        self.output_string.set('0')
        self.display_chars = []
        self.full_op = []

    def pow2(self):
        current_number = ''.join(self.display_chars)

        if current_number:
            self.formula_string.set(f"({current_number})²")
            self.output_string.set(str(int(current_number)**2))

    def sqrt2(self):
        current_number = ''.join(self.display_chars)

        if current_number:
            self.formula_string.set(f"√({current_number})")
            self.output_string.set(str(math.sqrt(int(current_number))))

    def inverse(self):
        print("dupa4")

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, allign, font, string_variable):
        super().__init__(master = parent, font = font, textvariable = string_variable)
        self.grid(column = 0, columnspan = 4, row = row, sticky = allign, padx = 7)

if __name__ == '__main__':

    Calculator(darkdetect.isDark())