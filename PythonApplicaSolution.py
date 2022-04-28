
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

#There are four collection data types in the Python programming language: list,tuple,set and dictionary

myList=["apple",'banana','cherry']
print(len(myList))
print(type(myList))

list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "blackcurrant" in thislist:
    print("Yes")
else:
    thislist[1] = "blackcurrant"
    print(thislist)

thislis = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislis[1:3] = ["blackcurrant", "watermelon"]
print(thislis)

thislistt = ["apple", "banana", "cherry"]
thislistt[1:2] = ["blackcurrant", "watermelon"]
print(thislistt)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

for x in thislist:
    print(x)

a=["apple","orange","Mango"]
for i in range(len(a)):
    print(i)

