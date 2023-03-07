# using slicing and unpacking operations

def read_n_lines(path: str, lines: int) -> list:
    with open(path) as content:
       return content.readlines()[0:lines - 1]


filePath = input('Send file path: ')
linesToRead = int(input('How many lines should be read? '))

# unpack
print(*(read_n_lines(filePath, linesToRead)))