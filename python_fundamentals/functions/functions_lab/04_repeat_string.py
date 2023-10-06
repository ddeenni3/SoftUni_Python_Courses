def string_repeat(string: str, n: int) -> str:
    return string * n


user_input = input()
counter = int(input())

print(string_repeat(user_input, counter))
