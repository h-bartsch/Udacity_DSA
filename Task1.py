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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def addNums(nums,numList): #function to take TX & RX phone numbers
    for i in numList:
        nums.add(i[0]) #TX
        nums.add(i[1]) #RX

nums = set() #empty set for all numbers
addNums(nums,calls)
addNums(nums,texts)

print("There are %d different telephone numbers in the records." % (len(nums)))

"""
Runtime: 0.04076957702636719 seconds
Runtime Analysis: O(2*n) ~= O(n)
"""