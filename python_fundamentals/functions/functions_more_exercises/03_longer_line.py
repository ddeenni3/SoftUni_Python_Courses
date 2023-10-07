from math import floor


def longer_line(first_x, first_y, second_x, second_y, third_x, third_y, fourth_x, fourth_y):
    first_line = floor(abs(first_x) + abs(first_y)) + floor(abs(second_x) + abs(second_y))
    second_line = floor(abs(third_x) + abs(third_y)) + floor(abs(fourth_x) + abs(fourth_y))

    if first_line > second_line:
        if (abs(first_x)) + (abs(first_y)) <= (abs(second_x)) + (abs(second_y)):
            return f'({floor(first_x)}, {floor(first_y)})({floor(second_x)}, {floor(second_y)})'
        else:
            return f'({floor(second_x)}, {floor(second_y)})({floor(first_x)}, {floor(first_y)})'
    elif second_line > first_line:
        if (abs(third_x)) + (abs(third_y)) <= (abs(fourth_x)) + (abs(fourth_y)):
            return f'({floor(third_x)}, {floor(third_y)})({floor(fourth_x)}, {floor(fourth_y)})'
        else:
            return f'({floor(fourth_x)}, {floor(fourth_y)})({floor(third_x)}, {floor(third_y)})'
    else:
        if (abs(third_x)) + (abs(third_y)) < (abs(fourth_x)) + (abs(fourth_y)):
            return f'({floor(third_x)}, {floor(third_y)})({floor(fourth_x)}, {floor(fourth_y)})'
        else:
            return f'({floor(fourth_x)}, {floor(fourth_y)})({floor(third_x)}, {floor(third_y)})'


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))
x3 = floor(float(input()))
y3 = floor(float(input()))
x4 = floor(float(input()))
y4 = floor(float(input()))


print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
