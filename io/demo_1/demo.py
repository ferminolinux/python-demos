
originalPath = input('Send original file path: ')
copyPath = input('Send a copy file path: ')
line = 0


with open(originalPath, 'r') as fileReader:

    writer = open(copyPath, 'w')

    for lineNumber, r in enumerate(fileReader):
        if lineNumber == 4:
            continue

        writer.write(r)

