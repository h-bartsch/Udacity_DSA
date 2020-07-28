"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
maxLen = 0 #max call time
maxNum = "" #callers number
for i in calls:
    if int(i[3]) > maxLen: #if the indexed call time is greater than the previous max, update the values
        maxLen = int(i[3])
        maxNum = i[0]

print("%s spent the longest time, %i seconds, on the phone during September 2016." % (maxNum, maxLen))       

"""
Runtime: 0.03989005088806152 seconds
Runtime Analysis: O(n)
"""