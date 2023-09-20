string = input().lower()

words = ["water", "fish", "sun", 'sand']

counter = 0

for item in words:
    if item in string:
        appeared_times = string.count(item)
        counter += appeared_times
print(counter)