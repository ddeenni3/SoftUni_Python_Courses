def employee_happiness(employees: list, factor: int):
    employees_new_score = [x * factor for x in employees]
    total_score = sum(employees_new_score)
    average_score = total_score / len(employees)
    happy_employees = [x for x in employees_new_score if x >= average_score]
    if len(happy_employees) >= len(employees) // 2:
        return f'Score: {len(happy_employees)}/{len(employees)}. Employees are happy!'
    else:
        return f'Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!'


employees_score = list(map(int, input().split()))
happiness_factor = int(input())

print(employee_happiness(employees_score, happiness_factor))
