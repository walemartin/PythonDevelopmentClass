
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
