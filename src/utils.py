"""
Вспомогательные функции.
"""
import data
from configparser import ConfigParser


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


def write_players() -> None:
    """Записывает в файл данных игроков информацию из соответствующей глобальной структуры данных."""
    config = ConfigParser()
    config.read_dict(data.players_db)
    # ИСПРАВИТЬ: функция read_players() читает в словарь data.players_db всё содержимое файла, затем здесь вы читаете в конфиг-объект весь словарь data.players_db — следовательно вам надо файл перезаписывать, а не дозаписывать
    with open(data.PLAYERS_PATH, 'a', encoding='utf-8') as file:
        config.write(file)


