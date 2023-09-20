period_days = int(input())

doctors = 7

cured_patient = 0
uncured_patient = 0

for i in range(1, period_days + 1):
    patients = int(input())
    if i % 3 == 0:
        if uncured_patient > cured_patient:
            doctors += 1
    if patients > doctors:
        uncured_patient += patients - doctors
        cured_patient += doctors
    else:
        cured_patient += patients


print(f'Treated patients: {cured_patient}.')
print(f'Untreated patients: {uncured_patient}.')

