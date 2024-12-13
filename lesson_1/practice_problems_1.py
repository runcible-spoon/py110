# Given the tuple:

fruits = ("apple", "banana", "cherry", "date", "banana")

# How would you count the number of occurrences of "banana" in the tuple?

for fruit in fruits:
    banana_counter = 0
    if fruit == 'banana':
        banana_counter += 1

print(banana_counter)
