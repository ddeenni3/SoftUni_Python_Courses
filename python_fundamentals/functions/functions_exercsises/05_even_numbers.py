def is_even(x): return x % 2 == 0


numbers = list(map(int, input().split()))

filtered = list(filter(is_even, numbers))

print(filtered)