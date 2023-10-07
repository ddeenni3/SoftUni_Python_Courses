def data_reader(some_data, some_data_type):
    if some_data_type == 'int':
        return int(some_data) * 2
    elif some_data_type == 'real':
        return f'{float(some_data) * 1.5:.2f}'
    elif some_data_type == 'string':
        return f'${some_data}$'


data_type = input()
data = input()

print(data_reader(data, data_type))
