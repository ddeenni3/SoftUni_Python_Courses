def tribonacci_sequence(some_number: int):
    result = [1, 0, 0]
    for num in range(some_number):
        next_num = sum(result)
        print(next_num, end=' ')
        result.append(next_num)
        result.pop(0)


number = int(input())
tribonacci_sequence(number)
