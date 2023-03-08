#  using iterator concepts 
def read_n_lines(path: str, lines: int) -> str:
    message = ""

    with open(path) as content:
        for n in range(lines):
            message += next(content)

    return message




filePath = input('Send file path: ')
linesToRead = int(input('How many lines should be read? '))

print(read_n_lines(filePath, linesToRead))