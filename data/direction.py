import random


def random_direction():
    direction = random.randint(1, 4)
    if direction == 1:
        return "up"
    elif direction == 2:
        return "down"
    elif direction == 3:
        return "right"
    elif direction == 4:
        return "left"


def find_case(player_rect, enemy_rect):
    if player_rect[1] > enemy_rect[1]:
        if player_rect[0] > enemy_rect[0]:
            return "down & right"
        else:
            return "down & left"
    else:
        if player_rect[0] > enemy_rect[0]:
            return "up & right"
        else:
            return "up & left"


def find_direction(player_rect, enemy_rect):
    case = find_case(player_rect, enemy_rect)
    if case == "up & right":
        if player_rect[0] - enemy_rect[0] > - (player_rect[1] - enemy_rect[1]):
            return "right"
        else:
            return "down"
    elif case == "up & left":
        if enemy_rect[0] - player_rect[0] > - (player_rect[1] - enemy_rect[1]):
            return "left"
        else:
            return "down"
    elif case == "down & right":
        if player_rect[0] - enemy_rect[0] > - (enemy_rect[1] - player_rect[1]):
            return "right"
        else:
            return "up"
    elif case == "down & left":
        if enemy_rect[0] - player_rect[0] > player_rect[1] - enemy_rect[1]:
            return "left"
        else:
            return "up"
