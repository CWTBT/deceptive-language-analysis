import string
import csv
import sys

negwords = []

with open("lexicon.csv","rb") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == "negative" and not row[0] in negwords:
                    negwords.append(row[0])

target = open("negwords.txt","r+b")

count = 0
for i in negwords:
    target.write(negwords[count]+"\n")
    count+=1
