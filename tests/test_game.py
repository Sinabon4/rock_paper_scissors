import pytest
from rps.game import determine_winner

def test_draw():
    assert determine_winner('камень', 'камень') == 'Ничья'

def test_player1_wins():
    assert determine_winner('камень', 'ножницы') == 'Игрок 1 победил'

def test_player2_wins():
    assert determine_winner('бумага', 'ножницы') == 'Игрок 2 победил'
