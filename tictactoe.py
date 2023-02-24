print("Добро пожаловать, уважаемые игроки!")
print("Давайте же сразимся в чудесном интерактивном баттле!")
print("Ниже вы увидите игровое поле, в котором можно поочередно выбирать ячейку")
print("Кто первым сформирует 'линию', тот молодец!")
print()
# объявляем зону игрового поля
zone = [
      1, 2, 3,
      4, 5, 6,
      7, 8, 9
]
# фиксируем победные комбинации
victory = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [2, 4, 7],
      [0, 4, 8]
]
# создаем функицю вывода игрового поля
def print_zone():
      print(zone[0], zone[1], zone[2])
      print(zone[3], zone[4], zone[5])
      print(zone[6], zone[7], zone[8])

# создаем функцию выбора ячейки для хода
def step_in_zone(step,symbol):
    ind = zone.index(step)
    zone[ind] = symbol

# Функция вывода текущего результата игры
def get_result():
      win = ""
      for i in victory:
            if zone[i[0]] == "X" and zone[i[1]] == "X" and zone[i[2]] == "X":
                  win = "X"
            if zone[i[0]] == "O" and zone[i[1]] == "O" and zone[i[2]] == "O":
                  win = "O"
      return win


# Механика игры
game_over = False
player1 = True

while game_over == False:

      # Показываем игровое поле
      print_zone()

      # Предлагаем сделать ход
      if player1 == True:
            symbol = "X"
            step = int(input("Игрок №1, ваш ход: "))
      else:
            symbol = "O"
            step = int(input("Игрок №2, ваш ход: "))

      step_in_zone(step, symbol)  # делаем ход в указанную ячейку
      win = get_result()  # определим победителя
      if win != "":
            game_over = True
      else:
            game_over = False

      player1 = not (player1)

# Игра завершена - объявляем победителя, показав игровое поле
print_zone()
print("Ура! подедил игрок с символом", win)