import string
import csv
import re
import sys

infile = "input.txt"
lexfile = "lexicon.csv"
infiles = []
if len(sys.argv)>1:
    for arg in range(len(sys.argv[1:])): infiles.append(sys.argv[arg+1])
print infiles
f = open(infile,"r")
s = f.read().lower()

# Splits the input string by spaces and punctuation and creates a list
#containing each individual word.
wordsplit = s.translate(string.maketrans("",""), string.punctuation)
wordsplit = wordsplit.split()

"""#wordlist = []
#Adds the first value of each row of the csv to a list
*lexicon = lexfiles[0]
for lex in range(len(lexfiles)):
    lexicon = lexfiles[lex]
    with open(lexicon, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row[0] in wordlist:
                wordlist.append(row[0])
                #polarity.append(row[1])"""


 ### TESTING FOR NEGEMO WORDS ###
wordlist = []
polarity = []
poswords = 0.0
negwords = 0.0

with open("lexicon.csv", 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] in wordlist:
            wordlist.append(row[0])
            polarity.append(row[1])

print "TESTING NEGEMO"
for i in range (len(wordsplit)):
    if wordsplit[i] in wordlist:
        if polarity[wordlist.index(wordsplit[i])] == "positive":
            poswords+=1
        else:
            negwords+=1

negtotal = negwords/len(wordsplit)
negtotal = negtotal*(-0.237)
print negtotal

 ### TESTING FOR EXCLUSIVE WORDS ###
wordlist = []
extotal = 0;

with open("exclusives.csv", 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] in wordlist:
            wordlist.append(row[0])

print "TESTING EXCLUSIVE"
for i in range (len(wordsplit)):
    if wordsplit[i] in wordlist:
        extotal+=1

extotal = extotal/len(wordsplit)
extotal = extotal*(0.54)
print extotal

 ### TESTING FOR FIRST PERSON ###
wordlist = []
fptotal = 0;

with open("firstperson.csv", 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] in wordlist:
            wordlist.append(row[0])

print "TESTING FIRST PERSON"
print wordlist
for i in range (len(wordsplit)):
    if wordsplit[i] in wordlist:
        fptotal+=1

fptotal = fptotal/len(wordsplit)
fptotal = fptotal*(0.36)
print fptotal

 ### RUNNING FINAL CALCULATIONS ###
total = fptotal + extotal + negtotal
print total




"""for i in range (len(wordsplit)):
    if wordsplit[i] in wordlist:
        print "Found: "+wordsplit[i]+"!" """
