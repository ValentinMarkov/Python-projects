from random import randint
from dice_visual_parts import dice_visual_point


def dice_number():
    num = randint(0, 5)
    print('Dice result:')
    print(dice_visual_point[num])
