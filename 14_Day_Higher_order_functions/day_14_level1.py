# ─────────────────────────────────────────────
## 💻 Exercises: Day 14
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 1
# ─────────────────────────────────────────────
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Explain the difference between map, filter, and reduce.
# map - built-in function that takes a function and iterable as parameters.
# filter - calls the specified function which returns *boolean* for each item of the specified iterable (list).
# reduce - takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value.

# 2. Explain the difference between higher order function, closure and decorator
# higher order function - a function calling another function.
# closure - a function defined within another function.
# decorator - allows a user to add new functionality to an existing object without modifying its structure.

# 3. Define a call function before map, filter or reduce, see examples.
def square_root(x):
    return x ** 0.5
numbers_squared = map(square_root, numbers)
print(f"Square root of each number in {numbers} is: {list(numbers_squared)}")

def is_prime(number):
    if not isinstance(number, int):
        return False
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True  
prime = filter(is_prime, numbers)    
print(f"Prime numbers in {numbers} are: {list(prime)}")

def multiply_two_nums(x, y):
    return int(x) * int(y)
total = reduce(multiply_two_nums, numbers)
print(f"The total of multiplying numbers in {numbers} is: {total}")

# 4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)