import random


with open('/Users/yichengxia/Desktop/Programs/Python/Algo-rhythm/src/text_data/hot_takes', 'r') as f:
    hot_takes = f.readlines()

with open('/Users/yichengxia/Desktop/Programs/Python/Algo-rhythm/src/text_data/ice_breaker_questions', 'r') as f:
    ice_breakers = f.readlines()




def get_random_hot_take():
    return random.Random().choice(hot_takes)


def get_random_ice_breaker():
    return random.Random().choice(ice_breakers)
