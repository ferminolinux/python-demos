# Count words without using string split method
def wordcount(inline: str, separator=' '):

    def wordsplit(string: str):
        edge = 0
        temp = []

        for index, character in enumerate(string):
            if character == separator:
                temp.append(string[edge:index])
                edge = index + 1
            continue
        else:
            temp.append(string[edge:index + 1])

        return temp
    



    words = wordsplit(inline)
    trash = words.count('') + words.count('\n')

    return len(words) - trash


    

    
filePath = './sample2.txt'
wc = 0
with open(filePath, 'r') as file:
    for l in file:
        wc += wordcount(l)


print('Total of words:', wc)
