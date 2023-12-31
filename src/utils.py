# стандартная библиотека
from configparser import ConfigParser
from shutil import get_terminal_size
# проект
import data
import help



def read_players() -> bool:
    """Читает файл данных игроков, сохраняет информацию в соответствующую глобальную структуру данных. Возвращает True, если в файле данных игроков есть хотя бы одна запись, иначе False."""
    config = ConfigParser()
    config.read(data.PLAYERS_PATH)
    config = {
        player_name: {
            key: int(value)
            for key, value in config[player_name].items()
        }
        for player_name in config.sections()
    }
    data.players_db = config
    return bool(config)


def read_saves() -> None:
    """"""
    saves = data.SAVES_PATH.read_text(encoding='utf-8').split('\n')
    for save in saves:
        players, turns, dim = save.split('!')
        data.saves_db |= {
            tuple(players.split(',')): {
                'dim': int(dim),
                'turns': {
                    int(turn): data.TOKENS[i%2]
                    for i, turn in enumerate(turns.split(','))
                },
            }
        }

def write_players() -> None:
    """Записывает в файл данных игроков информацию из соответствующей глобальной структуры данных."""
    config = ConfigParser()
    config.read_dict(data.players_db)
    # ИСПРАВИТЬ: функция read_players() читает в словарь data.players_db всё содержимое файла, затем здесь вы читаете в конфиг-объект весь словарь data.players_db — следовательно вам надо файл перезаписывать, а не дозаписывать
    with open(data.PLAYERS_PATH, 'w', encoding='utf-8') as file:
        config.write(file)


def write_saves() -> None:
    """ """


def dim_input() -> int:
    while True:
        dim = input(f' {data.MESSAGES["ввод размерности"]}{data.PROMPT}')
        if data.DIM_PATTERN.fullmatch(dim):
            return int(dim)
        print(f' {data.MESSAGES["некорректная размерность"]} ')


def change_dim(new_dim: int) -> None:
    """"""
    data.dim = new_dim
    data.dim_range = range(new_dim)
    data.all_cells = new_dim**2
    data.board = dict.fromkeys(range(1, data.all_cells+1), ' ')


def field_template(data_width: int = None) -> str:
    """"""
    if data_width is None:
        field_width = data.dim*(3 + max(len(t) for t in data.TOKENS)) - 1
    else:
        field_width = data.dim*(3 + data_width) - 1
    v_sep, h_sep = '|', '—'
    v_sep = v_sep.join([' {} ']*data.dim)
    h_sep = f'\n{h_sep*field_width}\n'
    return h_sep.join([v_sep]*data.dim)


def show_title() -> None:
    """Выводит на экран заголовок игры при запуске программы"""
    width = get_terminal_size().columns - 1
    line1 = f"{'#' * width}"
    line2 = f"\n#{' ' * (width-2)}#\n"
    text_line = f"#{'Игра КРЕСТИКИ-X НОЛИКИ-O'.center(width - 2)}#"
    print(line1+line2+text_line+line2+line1)


def concatenate_rows(
        matrix1: str,
        matrix2: str,
        *matrices: str,
        padding: int = 8
) -> str:
    """"""
    matrices = matrix1, matrix2, *matrices
    matrices = [m.split('\n') for m in matrices]
    padding = ' '*padding
    return '\n'.join(
        padding.join(row)
        for row in zip(*matrices)
    )
