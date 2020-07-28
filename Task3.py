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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

numSet = set()
countFixedBang = 0.
countTotal = 0
for i in calls:
  if i[0][0:5]: #[0] = calling number, [0:5] = (080) index
    countTotal += 1
    if "(" in i[1]: #if receiver is fixed line
      numSet.add(i[1][1:4]) #3 digit area code
      if "(080)" in i[1]:
        countFixedBang += 1
    elif " " in i[1]: #if RX is mobile
      numSet.add(i[1][0:4]) #4 digit area code
    else:
      numSet.add("140") #telemarketer area code

numList = sorted(list(numSet)) #convert set to list so we can sort
print("The numbers called by people in Bangalore have codes:")
for j in numList: #printing each number on new line
  print(j)

percentFixedBang = (countFixedBang/countTotal)*100 #Part B calculations
print("\n%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % (percentFixedBang))

"""
Runtime: 0.06379890441894531 seconds
Runtime Analysis: O(n log n)
    - 1 if statement = O(n)
    - 1 sorted statement = O(n log n)
"""