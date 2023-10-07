from math import floor


def closest_to_center(first_x, first_y, second_x, second_y):
    if (abs(first_x)) + (abs(first_y)) < (abs(second_x)) + (abs(second_y)):
        return f'({floor(first_x)}, {floor(first_y)})'
    return f'({floor(second_x)}, {floor(second_y)})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_to_center(x1, y1, x2, y2))
