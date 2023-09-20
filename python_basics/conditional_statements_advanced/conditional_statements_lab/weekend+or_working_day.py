day_of_week = input()

work_or_free = 'Error'

if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    work_or_free = 'Working day'
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    work_or_free = 'Weekend'

print(work_or_free)

