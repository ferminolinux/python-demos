# using a enumerated for
def read_n_lines(path: str, lines: int) -> str:
    message = ""

    with open(path) as content:
        for lineNumber, lineContent in enumerate(content):
            if lineNumber == lines:
                break
            message += lineContent


    return message




filePath = input('Send file path: ')
linesToRead = int(input('How many lines should be read? '))

print(read_n_lines(filePath, linesToRead))