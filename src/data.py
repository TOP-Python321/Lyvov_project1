"""
Глобальные переменные и константы.
"""

# стандартная библиотека
from pathlib import Path
from re import compile



PLAYERS_PATH = Path(r'..\data\players.ini')
SAVES_PATH = Path(r'..\data\saves.txt')
HELP_PATH = Path(r'..\data\help.txt')

TITLE = 'КРЕСТИКИ-НОЛИКИ'
HELP_TITLE = 'ПОМОЩЬ'


DEBUG = True
debug_data = {}

PROMPT = ' > '

MESSAGES = {
    'ввод имени': 'введите имя игрока',
    'некорректное имя': 'имя игрока должно начинаться с буквы, содержать только буквы, цифры и символ подчёркивания',
    'ввод размерности':'введите новый размер поля',
    'некорректная размерность': 'размер поля должен находится в диапозоне от 3 до 20'
    # '': '',
}

COMMANDS = {
    'начать новую партию': ('new', 'n', 'начать', 'н'),
    'загрузить существующую партию': ('load', 'l', 'загрузка', 'з'),
    'отобразить раздел помощи': ('help', 'h', 'помощь', 'п'),
    'создать или переключиться на игрока': ('player', 'p', 'игрок', 'и'),
    'отобразить таблицу результатов': ('table', 't', 'таблица', 'т'),
    'изменить размер поля': ('dim', 'd', 'размер', 'р'),
    'выйти': ('quit', 'q', 'выход', 'в'),
}


NAME_PATTERN = compile(r'[A-Za-zА-ЯЁа-яё][A-Za-zА-ЯЁа-яё\d_]+')
DIM_PATTERN = compile(r'[3-9]|(?:1[0-9]|20)')


players_db: dict[str, dict[str, int]] = {}
saves_db: dict[tuple[str, str], dict] = {}


dim: int = 3
dim_range = range(dim)
all_cells: int = dim**2

authorized: str


TOKENS = ('X', 'O')
WEIGHT_OWN = 1.5
WEIGHT_FOE = 1.0
START_MATRICES = ()


players: list[str] = []

board: dict[int, str] = dict.fromkeys(range(1, all_cells+1), ' ')
turns: dict[int, str] = {}


field: str = ''

