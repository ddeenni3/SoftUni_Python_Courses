starting_interval = input()
ending_interval = input()
interval_except = input()
counter = 0

for char1 in range(ord(starting_interval), ord(ending_interval) + 1):
    if chr(char1) == interval_except:
        continue
    for char2 in range(ord(starting_interval), ord(ending_interval) + 1):
        if chr(char2) == interval_except:
            continue
        for char3 in range(ord(starting_interval), ord(ending_interval) + 1):
            if chr(char3) == interval_except:
                continue
            else:
                counter += 1
                print(f'{chr(char1)}{chr(char2)}{chr(char3)}', end=' ')
print(f'{counter}')

