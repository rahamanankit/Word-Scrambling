import random
fh = open("MyFile.txt")
fh1 = open("MyFileScrambled.txt","w")
def shuffles(word):
    # get your word as a list
    word = list(word)

    # perform the shuffle operation
    random.shuffle(word)
    # return the list as a string
    word = ''.join(word)

    return word
for line in fh:
    line = line.split()
    for word in line:
        if len(word) > 3:
            if word.endswith('.') or word.endswith(',') or word.endswith('!') or word.endswith(';') or word.endswith('?'):
                fh1.write(word[0] + '' + shuffles(word[1:-2]) + '' + word[-2] + '' + word[-1] + ' ')
            else:
                fh1.write(word[0] + '' + shuffles(word[1:-1]) + '' + word[-1] + ' ')
        else:
                fh1.write(word + ' ')