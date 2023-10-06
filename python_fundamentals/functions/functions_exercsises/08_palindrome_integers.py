def palindrome_check(number: str):
    return number == number[::-1]


input_numbers = input().split(', ')


for num in input_numbers:
    print(palindrome_check(num))
