# ─────────────────────────────────────────────
## 💻 Exercises: Day 14
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 2
# ─────────────────────────────────────────────
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Use map to create a new list by changing each country to uppercase in the countries list
upper = lambda x: x.upper()
countries_upper = map(upper, countries)
print(f"Uppercase countries: {list(countries_upper)}")

# 2. Use map to create a new list by changing each number to its square in the numbers list
square = lambda i: i ** 2
print(f"Square numbers: {list(map(square, numbers))}")

# 3. Use map to change each name to uppercase in the names list
print(f"Uppercase names: {list(map(upper, names))}")

# 4. Use filter to filter out countries containing 'land'.
without_land = lambda x: "land" not in x
print(f"Countries without 'land' in them: {list(filter(without_land, countries))}") 

# 5. Use filter to filter out countries having exactly six characters.
six_char = lambda x: len(x) != 6
print(f"Countries that are not 6 characters long: {list(filter(six_char, countries))}")

# 6. Use filter to filter out countries containing six letters and more in the country list.
six_or_more = lambda x: len(x) >= 6
print(f"Countries that are 6 or more characters long: {list(filter(six_or_more, countries))}")

# 7. Use filter to filter out countries starting with an 'E'
starts_with = lambda x: x[0] == "E"
print(f"Countries that start with an 'E': {list(filter(starts_with, countries))}")

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print(f"Countries that are uppercase and do not have 'land' in them: {list(map(upper, filter(without_land, countries)))}")

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
get_string = lambda x: str(x)
get_string_list = map(get_string, numbers)
print(f"List containing only strings: {list(get_string_list)}")

# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce
sum_two = lambda a, b: a + b
sum_list = reduce(sum_two, numbers)
print(f"Total of the sum of numbers in {numbers} is: {sum_list}")

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concat = lambda a, b: f"{a}, {b}" if b != countries[-1] else f"{a}, and {b}"
concat_final = reduce(concat, countries)
print(f"{concat_final} are north European countries.")

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.