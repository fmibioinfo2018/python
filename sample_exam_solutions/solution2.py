# Да се прочете секвенция от файл [data/sequence_1.seq] и да се запише в обратна последователност в нов файл с име [reverse_sequence_1.seq]

import os

fileToOpenName = '../sample_exam/data/sequence_1.seq'
newFIleName = 'reverse_sequence_1.seq'
currentFolderPath = os.path.dirname(os.path.abspath(__file__))
completePath = os.path.join(currentFolderPath, 'data/')
# darn this stuff :X

with open(fileToOpenName) as fileToOpen:
    content = fileToOpen.read()

with open(os.path.join(completePath, newFIleName), 'w+') as newFile:
    newFile.write(content[::-1])
    newFile.flush()
    newFile.seek(0)
    print(newFile.read())


