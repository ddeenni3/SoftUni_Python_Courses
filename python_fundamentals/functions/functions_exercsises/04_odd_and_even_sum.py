def odd_even_sum(number: str):
    sum_odd = 0
    sum_even = 0
    for num in number:
        current_num = int(num)
        if current_num % 2 == 0:
            sum_even += current_num
        else:
            sum_odd += current_num
    return sum_odd, sum_even


num_as_string = input()

sum_of_odds, sum_of_evans = odd_even_sum(num_as_string)

print(f'Odd sum = {sum_of_odds}, Even sum = {sum_of_evans}')
