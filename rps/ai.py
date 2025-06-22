import random

def choose_easy():
    return random.choice(['камень', 'ножницы', 'бумага'])

def choose_medium(history):
    if not history:
        return choose_easy()
    last_move = history[-1]
    counter = {'камень': 'бумага', 'бумага': 'ножницы', 'ножницы': 'камень'}
    return counter[last_move]

def choose_hard(history):
    if not history:
        return choose_easy()
    freq = {'камень': 0, 'ножницы': 0, 'бумага': 0}
    for move in history:
        freq[move] += 1
    most_common = max(freq, key=freq.get)
    counter = {'камень': 'бумага', 'бумага': 'ножницы', 'ножницы': 'камень'}
    return counter[most_common]

