from nim_engine import put_stones, get_bunches, is_gameover, take_from_bunch, enter_sizes
from termcolor import cprint, colored

max_bunches = int(input(colored("Введите количество кучек предметов: ", color='green')))
max_bunche_size = int(input(colored("Введите макстмальный размер кучки предметов: ", color='green')))

enter_sizes(bunches=max_bunches, bunche_size=max_bunche_size)
put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'cyan'
    cprint('Ход игрока {}'.format(user_number), color=user_color)
    pos = input(colored('С какой кучки берем? ', color=user_color))
    qua = input(colored('Сколько предметов берем? ', color=user_color))
    step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        if is_gameover():
            break
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход!', color='red', attrs=['bold'])
    # if is_gameover():
    #     break

cprint('Выиграл игрок номер {}'.format(user_number), color='red', attrs=['bold'])