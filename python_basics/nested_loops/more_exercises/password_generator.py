n = int(input())
L = int(input())

for s1 in range(1, n + 1):
    for s2 in range(1, n + 1):
        for l1 in range(97, (96 + L) + 1):
            for l2 in range(97, (96 + L) + 1):
                for s3 in range(1, n + 1):
                    if s3 > s1 and s3 > s2:
                        print(f'{s1}{s2}{chr(l1)}{chr(l2)}{s3}', end=' ')

