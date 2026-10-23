# Homework for the lesson
# Write a script that creates a list containing the first 100 terms (at least) of the Fibonacci sequence
# The list should look like this:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55… all the way to really really large numbers
# https://www.w3schools.com/python/trypython.asp?filename=demo_compiler

# Here is a script that gives the first 100 positive even numbers
# You may use this as a starting template
numbers = [0, 1]
for i in range(1, 1000):
    print(numbers[0])
    bell = numbers.pop(0)
    bell = bell + numbers[0]
    numbers.append(bell)









