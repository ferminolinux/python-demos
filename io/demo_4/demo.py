def wordcount(inline: str, separator=' '):
    temp = inline.split(separator)
    trash = temp.count('') + temp.count('\n')
    return len(temp) - trash




wc = 0
filePath = './sample2.txt'

with open(filePath, 'r') as file:
    for l in file:
        wc += wordcount(l)


print('Total of words:', wc)