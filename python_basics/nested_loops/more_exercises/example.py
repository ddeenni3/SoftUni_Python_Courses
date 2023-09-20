one_lev_coins = int(input())
two_lev_coins = int(input())
five_lev_note = int(input())
total_sum = int(input())

break_flag = False

while total_sum > 0:
    one_counter = 0
    two_counter = 0
    five_counter = 0
    while five_lev_note > 0:
        five_counter += 1
        five_lev_note -= 1
        total_sum -= 5
        while two_lev_coins > 0:
            two_counter += 1
            two_lev_coins -= 1
            total_sum -= 2
            while one_lev_coins > 0:
                total_sum -= 1
                one_lev_coins -= 1
                one_counter += 1
                print(f'{one_counter} * 1 lv. + {two_counter} * 2 lv. + {five_counter} * 5 lv.')
                if total_sum <= 0:
                    break_flag = True
                    break
            if break_flag:
                break
        if break_flag:
            break
    print(f'{one_counter} * 1 lv. + {two_counter} * 2 lv. + {five_counter} * 5 lv.')
    if break_flag:
        break
