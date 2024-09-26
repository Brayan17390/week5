#collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add?Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "kiwi", "watermelon"]

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple" #I can reassign values using this
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()

print(fruits[0])
for fruit in fruits:
   print(fruit)