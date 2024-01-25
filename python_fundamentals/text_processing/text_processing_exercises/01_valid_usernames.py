def symbols(some_username):
    for char in some_username:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def length(some_username):
    if 3 <= len(some_username) <= 16:
        return True
    return False


def username_is_valid(some_username):
    if length(some_username) and symbols(some_username):
        return True
    return False


usernames = input().split(", ")

for username in usernames:
    if username_is_valid(username):
        print(username)
