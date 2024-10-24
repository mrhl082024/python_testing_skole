sorting_list=[2,4,3,6,8,7,9,1,5]
sorting_list.sort()
print(sorting_list)
sorting_list.sort(reverse=True)
print(sorting_list)


adding_list=["volvo", "audi"]
adding_list.append("bmw")
print(adding_list)
adding_list.pop(0)
print(adding_list)


#tuple
mytuple=("apple", "banana", "pear", "apple")
print(len(mytuple))
print(type(mytuple))
print(mytuple[1])
print(mytuple[-1])
print(mytuple[1:3])
if "pear" in mytuple:
    print("there is a pear in this tuple")


x = ("bmw", "audi", "volvo")
y = list(x)
y[1] = "mercedes"
x = tuple(y)
print(x)

y = list(x)
y.append("alfa romeo")
x = tuple(y)
print(x)

y = list(x)
y.remove("alfa romeo")
x = tuple(y)
print(x)

tuple_fruits = ("apple", "kiwi", "orange")
(red, green, yellow) = tuple_fruits
print(green)
print(red)
print(yellow)
