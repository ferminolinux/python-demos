# using a simple for
def read_n_lines(path: str, lines: int) -> str:
    message = ""
    contador = 0

    with open(path) as content:
        for l in content:
            if contador == lines:
                break
            message += l
            contador += 1

    return message




filePath = input('Send file path: ')
linesToRead = int(input('How many lines should be read? '))

print(read_n_lines(filePath, linesToRead))