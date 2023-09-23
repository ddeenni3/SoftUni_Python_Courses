number_of_people = int(input())
elevator_capacity = int(input())
counter = 0

while number_of_people > 0:
    counter += 1
    number_of_people -= elevator_capacity

print(counter)
