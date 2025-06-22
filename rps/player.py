from abc import ABC, abstractmethod
import random
from . import ai

class Player(ABC):
    @abstractmethod
    def make_move(self, history):
        pass

class Human(Player):
    def make_move(self, history):
        move = input("Выберите (камень, ножницы, бумага): ").lower()
        while move not in ['камень', 'ножницы', 'бумага']:
            move = input("Неверный выбор. Повторите: ").lower()
        return move

class Computer(Player):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.history = []

    def make_move(self, history):
        if self.difficulty == 'легкий':
            return ai.choose_easy()
        elif self.difficulty == 'средний':
            return ai.choose_medium(history)
        elif self.difficulty == 'сложный':
            return ai.choose_hard(history)
        return ai.choose_easy()
