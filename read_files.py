file_path = './auth.log'

with open(file_path, 'r') as file:
    for each in file:
        print(each.strip())