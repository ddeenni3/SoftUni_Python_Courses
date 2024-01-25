path_to_file = input().split("\\")
file_name, file_extension = path_to_file[-1].split(".")
print(f'File name: {file_name}\nFile extension: {file_extension}')
