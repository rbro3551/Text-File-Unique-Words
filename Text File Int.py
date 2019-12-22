from __future__ import with_statement
import csv
import string
count = 0
passf = {}                     #Import what is needed and create dictionaries and lists for unique words
wcount = 0
uniqewrds = set()
wlist = []
from collections import Counter
c = {}

while True:
    try:
        file = input('Enter the file to read from:')
        with open(file, 'r') as passfile:
            break                                   #Check if valid file
    except FileNotFoundError:
        print('File not found')
        continue
with open(file, 'r') as passfile:
    reader = csv.reader(passfile, delimiter = ' ')
    for row in reader:
        for word in row:                                #Open file as csv
            word = word.lower()
            nword = word.translate(str.maketrans('', '', string.punctuation))
            if len(word) > 3:
                if nword not in passf:
                    passf[nword] = 1                #Append words of length greater than 3 to dictionary
                    count += 1
                    wcount += 1
                else:
                    passf[nword] += 1
                    count += 1
                    wcount += 1
            qword = word.translate(str.maketrans('', '', string.punctuation))
            if len(word) > 3:
                uniqewrds.add(qword)                        #Add unique words to list
    sorted_d = sorted(passf.items(), reverse=True, key=lambda x: x[1])
print('{}{:>20}{:>20}'.format('#', 'Word', 'Freq'))                    #Output the dictionary in readable terms
print('=' * 50)
finaldict = dict(sorted_d)
dcount = 0
num = 1
for key, value in finaldict.items():                #Append words that occur only once to list
    if value == 1:
        wlist.append(value)
for key, value in finaldict.items():
    if dcount >= 10:
        break
    print('{}{:>20}{:>20}'.format(num, key, value))
    dcount += 1
    num += 1
print()
print('There are %d words that occur only once.' % (len(wlist)))
print('There are %d unique words in the document.' %(len(uniqewrds)))