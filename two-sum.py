#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

numbers = (input("Please enter a list of numbers seperated by a space (e.g. 4 1 5 8 10 32 15): "))
numslist = numbers.split()
target = int(input("Please enter the sum of any two numbers from your list: "))
newlist = []

for i in numslist:
    newlist.append(int(i))

secondnum = newlist.copy()
firstindex = 0
secondindex = 0

for i in newlist:
    secondnum.remove(i)
    secondindex = 1 + firstindex
    for n in secondnum:
        sum = i+n
        if sum == target:
            print("The numbers", i, "&", n, "add to", target, "\nThese had index numbers", firstindex, "&", secondindex)
            break
        else:
            secondindex += 1
    firstindex += 1