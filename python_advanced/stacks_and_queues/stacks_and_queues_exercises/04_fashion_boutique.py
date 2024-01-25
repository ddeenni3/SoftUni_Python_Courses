delivery = [int(x) for x in input().split()]

rack_capacity = int(input())

number_of_racks = 0
current_sum = 0

while delivery:
    current_wear = delivery.pop()
    current_sum += current_wear
    if current_sum == rack_capacity:
        number_of_racks += 1
        current_sum = 0
    elif current_sum > rack_capacity:
        delivery.append(current_wear)
        number_of_racks += 1
        current_sum = 0

if current_sum > 0:
    number_of_racks += 1

print(number_of_racks)

# smarter solution:

# clothes = [int(x) for x in input().split()]
# rack_space = int(input())
#
# racks_count = 1
# current_rack_space = rack_space
#
# while clothes:
#     cloth = clothes.pop()
#
#     if current_rack_space >= cloth:
#         current_rack_space -= cloth
#     else:
#         racks_count += 1
#         current_rack_space = rack_space - cloth
#
# print(racks_count)