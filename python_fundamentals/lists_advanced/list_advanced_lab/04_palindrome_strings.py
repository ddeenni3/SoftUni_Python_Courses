def palindrome_strings():

    palindromes = [x for x in input().split() if x == x[::-1]]
    palindrome = input()
    count = palindromes.count(palindrome)

    return palindromes, count


list_of_palindromes, count_of_palindrome = palindrome_strings()

print(f'{list_of_palindromes}\nFound palindrome {count_of_palindrome} times')
