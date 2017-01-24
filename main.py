import string
import csv
import re
import sys

infile = "input.txt"
lexfile = "lexicon.csv"

if len(sys.argv)>1: infile = sys.argv[1]
if len(sys.argv)>2: lexfile = sys.argv[2]
f = open(infile,"r")
s = f.read()

# Splits the input string by spaces and punctuation and creates a list
#containing each individual word.
wordsplit = s.translate(string.maketrans("",""), string.punctuation)
wordsplit = wordsplit.split()

wordlist = []
polarity = []

#Adds the first value of each row of the csv to a list
with open(lexfile, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] in wordlist:
            wordlist.append(row[0])
            polarity.append(row[1])

#Sorts the csv list by descending length
#wordlist.sort(key=lambda x:len(x[0]), reverse=True)

poswords = 0.0
negwords = 0.0
for i in range (len(wordsplit)):
    if wordsplit[i] in wordlist:
        print "Found: "+wordsplit[i]+"!"
        print polarity[wordlist.index(wordsplit[i])]
        if polarity[wordlist.index(wordsplit[i])] == "positive":
            poswords += 1
        elif polarity[wordlist.index(wordsplit[i])] == "negative":
            negwords += 1

print "POSITIVE WORDS: "+str(poswords)
print "NEGATIVE WORDS: "+str(negwords)
