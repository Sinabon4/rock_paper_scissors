import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rps.game import determine_winner

# Проверка ничьей
def test_draw():
    assert determine_winner('камень', 'камень') == 'Ничья'
    assert determine_winner('ножницы', 'ножницы') == 'Ничья'
    assert determine_winner('бумага', 'бумага') == 'Ничья'

# Проверка победы игрока 1
def test_player1_wins():
    assert determine_winner('камень', 'ножницы') == 'Игрок 1 победил'
    assert determine_winner('ножницы', 'бумага') == 'Игрок 1 победил'
    assert determine_winner('бумага', 'камень') == 'Игрок 1 победил'

# Проверка победы игрока 2
def test_player2_wins():
    assert determine_winner('камень', 'бумага') == 'Игрок 2 победил'
    assert determine_winner('бумага', 'ножницы') == 'Игрок 2 победил'
    assert determine_winner('ножницы', 'камень') == 'Игрок 2 победил'

# Ручной запуск
if __name__ == "__main__":
    try:
        test_draw()
        test_player1_wins()
        test_player2_wins()
        print("✅ Все ручные тесты пройдены успешно!")
    except AssertionError:
        print("❌ Один из тестов не прошёл.")
        