from math import ceil

budget = float(input())
students_amount = int(input())
price_flour_per_pack = float(input())
price_eggs = float(input())
price_apron = float(input())

free_package = students_amount // 5
total_flour = (students_amount - free_package) * price_flour_per_pack
total_eggs = students_amount * (price_eggs * 10)
students_extra = ceil(students_amount + students_amount * 0.2)
total_apron = students_extra * price_apron
total_spent = total_flour + total_eggs + total_apron


if total_spent > budget:
    print(f"{abs(total_spent - budget):.2f}$ more needed.")
else:
    print(f'Items purchased for {total_spent:.2f}$.')
    