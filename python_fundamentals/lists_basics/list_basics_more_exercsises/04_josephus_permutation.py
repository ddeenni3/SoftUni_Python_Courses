person_numbers_list = input().split()
k = int(input())
killed_sequence = []
sequence_len = len(person_numbers_list)
current_victim = k - 1
victim_index = 0
while sequence_len > 0:
    victim_index = (current_victim + victim_index) % sequence_len
    killed_sequence.append(person_numbers_list.pop(victim_index))
    sequence_len -= 1

print(f"[{','.join(killed_sequence)}]")
