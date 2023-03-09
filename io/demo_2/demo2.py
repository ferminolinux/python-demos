path = input('Send a file path: ')

with open(path, 'r') as f:
    lines = f.readlines()

    if not lines:
        print('Empty file')
    else:
        print(*lines, sep='')
