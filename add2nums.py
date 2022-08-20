# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example: 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
intlist = []
num1 = ''
num2 = ''
ans = []

rdigits = (input("Please enter a number as its digits in reversed order seperated by a space (e.g. if your number is 415, enter 5 1 4): "))
rdigits2 = (input("Please enter a second number as its digits in reversed order seperated by a space (e.g. if your number is 415, enter 5 1 4): "))

rdigitslist = rdigits.split()
rdigitslist2 = rdigits2.split()

for i in rdigitslist:
    intlist.insert(0, i)

for n in intlist:
    num1 += n
num = int(num1)

intlist2 = []
for i in rdigitslist2:
    intlist2.insert(0, i)

for n in intlist2:
    num2 += n
secondnum = int(num2)
sum = num + secondnum
sumlist = [int(d) for d in str(sum)]

for j in sumlist:
    ans.insert(0, j)
print(ans)