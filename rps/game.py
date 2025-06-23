from .player import Human, Computer

# Универсальная функция проверки ввода
def get_valid_input(prompt, valid_options):
    """
    Запрашивает ввод у пользователя и проверяет его наличие в допустимых значениях.
    Повторяет запрос до тех пор, пока не будет введено корректное значение.
    """
    value = input(prompt).strip().lower()
    while value not in valid_options:
        print("Неверный выбор. Повторите:")
        value = input(prompt).strip().lower()
    return value

# Определение победителя раунда
def determine_winner(p1, p2):
    if p1 == p2:
        return 'Ничья'
    elif (p1 == 'камень' and p2 == 'ножницы') or \
         (p1 == 'ножницы' and p2 == 'бумага') or \
         (p1 == 'бумага' and p2 == 'камень'):
        return 'Игрок 1 победил'
    else:
        return 'Игрок 2 победил'

# Основной игровой процесс
def play_game():
    print("Добро пожаловать в игру Камень-Ножницы-Бумага!")

    # Выбор режима игры с защитой
    mode = get_valid_input("Выберите режим (1 - PvP, 2 - PvE): ", ['1', '2'])

    # Запрос количества раундов
    while True:
        try:
            rounds = int(input("Сколько раундов сыграть? "))
            if rounds > 0:
                break
            else:
                print("Введите положительное число.")
        except ValueError:
            print("Введите число.")

    p1 = Human()
    history = []

    # Настройка второго игрока
    if mode == '1':
        p2 = Human()
    else:
        difficulty = get_valid_input("Выберите сложность (легкий/средний/сложный): ",
                                     ['легкий', 'средний', 'сложный'])
        p2 = Computer(difficulty)

    score = {"Игрок 1": 0, "Игрок 2": 0, "Ничья": 0}

    for i in range(rounds):
        print(f"\nРаунд {i + 1}:")
        move1 = p1.make_move(history)
        move2 = p2.make_move(history)
        history.append(move1)

        print(f"Игрок 1: {move1}, Игрок 2: {move2}")
        result = determine_winner(move1, move2)
        print(result)

        if result == "Игрок 1 победил":
            score["Игрок 1"] += 1
        elif result == "Игрок 2 победил":
            score["Игрок 2"] += 1
        else:
            score["Ничья"] += 1

    print("\nИтоговый счёт:")
    for player, points in score.items():
        print(f"{player}: {points}")
