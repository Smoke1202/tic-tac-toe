def Greeting():
    board = input("Привет, это игра крестики нолики \n"
                    "-----------------\n"
                    "Нужно вводить два числа через пробел:\n"
                    " - первое число сторока,\n"
                    " - второе столбик. \n" 
                    "Чтобы начать нажми Enter! \n"
                    "-----------------\n" 
                    "Приятной игры >.<")
    if board == "":
        print()

Greeting()

def nachalo(vopros):
    otvet = None
    while otvet not in ('да','нет'):
        otvet = input(vopros).lower()
    return otvet

def fishki():
    perviy_hod=nachalo("Вы хотите быть первым, кто сделает ход? ('да', 'нет')  ")
    if perviy_hod == 'да':
        print('Хорошо, вы ходите первый!')
        player_1 = "X"
        player_2 = "O"
    else:
        print('Хорошо, вы ходите после первого игрока!')
        player_1 = "O"
        player_2 = "X"
    return player_2, player_1

def main():
    human1, human2 = fishki()

main()

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def player():
    counter = 0
    while True:
        counter += 1
        show()


def ask():
    while True:                                                 #цикл
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:                                     #если введенных чисел не 2 , то выводим сообщение
            print("Введите две координаты! ")
            continue                                            #Позволяет пропустить текущий блок и начать его заново

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):                #Если мы ввели числа то функция isdigit вернет True
            print(" Введите числа! ")
            continue

        x, y = map(int,cords)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print("Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break

