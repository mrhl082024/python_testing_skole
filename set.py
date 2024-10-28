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