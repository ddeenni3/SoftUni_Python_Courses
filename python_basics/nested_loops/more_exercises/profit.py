one_lev_coins = int(input())
two_lev_coins = int(input())
five_lev_note = int(input())
total_sum = int(input())

for one in range(0, one_lev_coins + 1):
    for two in range(0, two_lev_coins + 1):
        for five in range(0, five_lev_note + 1):
            current_sum = one * 1 + two * 2 + five * 5
            if current_sum == total_sum:
                print(f'{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total_sum} lv.')
            current_sum = 0
