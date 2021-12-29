import re, fnmatch, os

path = 'templates/template_2.txt'
pattern = r'{[A-z]*[0-9]*}'

def print_vars(path):
    with open(path, 'r') as f:
        data = f.read()
        found = re.findall(pattern, data)
        print('Przed: '+data)
        print('-------------------')
        for i in found:
            data = data.replace(i, '________')
            print(f'{i}  ->  {i[1:-1]}')
        print('-------------------')
    print('Po: '+data)
print_vars(path)