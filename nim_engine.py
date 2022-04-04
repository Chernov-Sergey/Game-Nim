from random import randint
from termcolor import colored
# from main import max_bunches, max_bunche_size

MAX_BUNCHES = 0
MAX_BUNCHE_SIZE = 0

_holder = {}
_sorted_keys = None

def enter_sizes():
    global MAX_BUNCHES, MAX_BUNCHE_SIZE
    MAX_BUNCHES = int(input(colored("Введите количество кучек предметов: ", color='green')))
    MAX_BUNCHE_SIZE = int(input(colored("Введите макстмальный размер кучки предметов: ", color='green')))


def put_stones():
    """ расположить камни на игровой поверхности """
    global _holder, _sorted_keys
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHE_SIZE)
    _sorted_keys = sorted(_holder.keys())


def take_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def get_bunches():
    res = []
    for key in _sorted_keys:
        res.append(_holder[key])
    return res


def is_gameover():
    return sum(_holder.values()) == 0