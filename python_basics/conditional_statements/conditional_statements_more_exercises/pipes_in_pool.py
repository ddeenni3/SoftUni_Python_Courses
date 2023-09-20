pool_volume_in_litres = int(input())
first_pipe_debit_per_hour = int(input())
second_pipe_debit_per_hour = int(input())
hours_worker_absent = float(input())

first_pipe_fill = first_pipe_debit_per_hour * hours_worker_absent
second_pipe_fill = second_pipe_debit_per_hour * hours_worker_absent
both_pipes_combined = first_pipe_fill + second_pipe_fill

fill_percentage_total = both_pipes_combined / pool_volume_in_litres

first_pipe_percentage = first_pipe_fill / both_pipes_combined
second_pipe_percentage = second_pipe_fill / both_pipes_combined

fill_percentage_total *= 100
first_pipe_percentage *= 100
second_pipe_percentage *= 100

diff = both_pipes_combined - pool_volume_in_litres

if both_pipes_combined <= pool_volume_in_litres:
    print(f"The pool is {fill_percentage_total:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. "
          f"Pipe 2: {second_pipe_percentage:.2f}%.")
else:
    print(f'For {hours_worker_absent} hours the pool overflows with {diff} liters.')

