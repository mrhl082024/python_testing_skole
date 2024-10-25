

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


mytuple = ("Volvo", "BMW", "Audi", "Mercedez")
for x in mytuple:
    print(x)

for i in range(len(mytuple)):
    print(mytuple[i])

fruit_tuple = ("apple", "banana", "mango")
y = 0
while y < len(fruit_tuple):
    print(fruit_tuple[y])
    y = y + 1

