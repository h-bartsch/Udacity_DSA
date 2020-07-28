"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
numSet = set() #empty set of non telemarketers
teleSet = set() #empty set of telemarketers
for i in calls: #iterate through calls, adding RX calls to numSet
    numSet.add(i[1])

for j in texts: #iterate through texts, adding all texts to numSet
    numSet.add(i[0])
    numSet.add(i[1])

for k in calls: #iterate through calls again, checking against numSet
    if k[0] not in numSet:
        teleSet.add(k[0])

teleList = sorted(list(teleSet)) #convert set to list so we can sort
print("These numbers could be telemarketers: ")
for m in teleList: #printing each number on new line
  print(m)

"""
Runtime: 0.07879018783569336 seconds
Runtime Analysis: O(n log n)
"""