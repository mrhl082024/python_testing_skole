set_1 = {"apple", "banana", "cherry"}
print(set_1)
print(len(set_1))

list1 = ["bmw", "volvo", "audi"]
set1 = set(list1)
print(type(set1))

set2 = {"enda", "flere", "ord"}
for x in set2:
    print(x)
print("enda" in set2)

set3 = {"volvo", "bmw", "audi"}
set3.add("volkswagon")
print(set3)

set3.update(set2)
print(set3)

set3.remove("volvo")
print(set3)
set3.remove("enda")
set3.remove("flere")
set3.remove("ord")
set3.add("volvo")
print(set3)

set3.discard("apple")
print(set3)

set4 = {"eivind", "kjell", "john"}
set4.pop()
print(set4)
set4.clear()
print(set4)
del set4


set5 = {1, 2, 3}
set6 = {"a", "b", "c"}
set7 = {"bmw", "volvo", "audi"}
set8 = set5 | set6 | set7
print(set8)