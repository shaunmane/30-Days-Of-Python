# ─────────────────────────────────────────────
## 💻 Exercises: Day 15
# ─────────────────────────────────────────────

# --- SyntaxError --- #
numbers = [1, 2, 4, 5, 7                      # SyntaxError: '[' was never closed

# --- NameError --- #
print(f"My name is: {name}")                  # NameError: name 'name' is not defined

# --- IndexError --- #
numbers = [1, 2, 4, 5, 3, 7]
print(numbers[7])                            # IndexError: list index out of range

# --- ModuleNotFoundError --- #
import bash                                  # ModuleNotFoundError: No module named 'bash'

# --- AttributeError --- #
numbers.sorted()                             # AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?

# --- KeyError --- #
country = {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    }
print(country["capitol"])                    # KeyError: 'capitol'

# --- TypeError --- #
print(4 + "3")                               # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# --- ImportError --- #
from random import numb                      # ImportError: cannot import name 'numb' from 'random'
print(numb(numbers))

# --- ValueError --- # 
two = "two"     
print(int(two))                              # ValueError: invalid literal for int() with base 10: 'two'

# --- ZeroDivisionError --- #
print(10 / 0)                                # ZeroDivisionError: division by zero