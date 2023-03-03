
previous = 0

for number in range(10):
    print(f'Current:{number}', f'Previous:{previous}', f'Sum:{number + previous}')
    previous = number