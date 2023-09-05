
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 400
MAIN_ROWS = 7
MAIN_COLS = 4

FONT_SIZE = 40
OUTPUT_FONT_SIZE = 60
FONT_STYLE = 'Georgia'

STYLING = {
    'gap' : 0.5,
    'corner-radius' : 0
}

NUMBER_POSITION = {
    ',' : {'col' : 2, 'row' : 6},
    1 : {'col' : 0, 'row' : 5},
    2 : {'col' : 1, 'row' : 5},
    3 : {'col' : 2, 'row' : 5},
    4 : {'col' : 0, 'row' : 4},
    5 : {'col' : 1, 'row' : 4},
    6 : {'col' : 2, 'row' : 4},
    7 : {'col' : 0, 'row' : 3},
    8 : {'col' : 1, 'row' : 3},
    9 : {'col' : 2, 'row' : 3},
    0 : {'col' : 1, 'row' : 6},

}

SYMBOLS_POSITION = {
    '=' : {'col' : 3, 'row' : 6, 'character' : '=', 'operator' : '='},
    '+' : {'col' : 3, 'row' : 5, 'character' : '+', 'operator' : '+'},
    '-' : {'col' : 3, 'row' : 4, 'character' : '-', 'operator' : '-'},
    '*' : {'col' : 3, 'row' : 3, 'character' : 'x', 'operator' : '*'},
    '/' : {'col' : 3, 'row' : 2, 'character' : '/', 'operator' : '/'}

}

OPERATIONS_POSITION = {
    'clear' : {'col' : 0, 'row' : 2, 'text' : 'AC'},
    'pow2' : {'col' : 1, 'row' : 2, 'text' : 'x²'},
    'sqrt2' : {'col' : 2, 'row' : 2, 'text' : '√x'},
    'inverse' : {'col' : 0, 'row' : 6, 'text' : '-/+'},

}

COLORS = {
    'light-gray' : {'fg' : ('#505050', '#D4D4D2'), 'hover': ('#686868', '#EFEFED'), 'text' : ('white', 'black')},
    'dark-gray' : {'fg' : ('#D4D4D2', '#505050'), 'hover': ('#EFEFED', '#686868'), 'text' : ('black', 'white')},
    'orange' : {'fg' : '#FF9500', 'hover': '#FFB143', 'text' : ('black', 'white')},
    'orange-hover' : {'fg' : 'white', 'hover': 'white', 'text' : ('black', '#FF9500')},

}

TITLE_BAR_COLORS_HEX = {
    'dark' : 0x00000000,
    'light' : 0x00EEEEEE
}

BLACK = '#000000'
WHITE = '#EEEEEE'


