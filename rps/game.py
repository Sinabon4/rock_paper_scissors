from .player import Human, Computer

def determine_winner(p1, p2):
    if p1 == p2:
        return 'Ничья'
    elif (p1 == 'камень' and p2 == 'ножницы') or \
         (p1 == 'ножницы' and p2 == 'бумага') or \
         (p1 == 'бумага' and p2 == 'камень'):
        return 'Игрок 1 победил'
    else:
        return 'Игрок 2 победил'

def play_game():
    mode = input("Выберите режим (1 - PvP, 2 - PvE): ")
    rounds = int(input("Сколько раундов сыграть? "))
    p1 = Human()
    history = []

    if mode == '1':
        p2 = Human()
    else:
        difficulty = input("Выберите сложность (легкий/средний/сложный): ")
        p2 = Computer(difficulty)

    score = {"Игрок 1": 0, "Игрок 2": 0, "Ничья": 0}

    for i in range(rounds):
        print(f"\nРаунд {i+1}:")
        move1 = p1.make_move(history)
        move2 = p2.make_move(history)
        history.append(move1)
        result = determine_winner(move1, move2)
        print(f"Игрок 1: {move1}, Игрок 2: {move2}")
        print(result)
        if result == "Игрок 1 победил":
            score["Игрок 1"] += 1
        elif result == "Игрок 2 победил":
            score["Игрок 2"] += 1
        else:
            score["Ничья"] += 1

    print("\nИтоговый счёт:")
    for k, v in score.items():
        print(f"{k}: {v}")
