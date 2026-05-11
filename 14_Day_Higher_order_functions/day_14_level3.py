# ─────────────────────────────────────────────
## 💻 Exercises: Day 14
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 3
# ─────────────────────────────────────────────
# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#    - Sort countries by name, by capital, by population
def sort_name(countries):
    return sorted(countries, key=lambda country: country["name"]) 

def sort_capital(countries):
    return sorted(countries, key=lambda country: country["capital"]) 

def sort_population(countries):
    return sorted(countries, key=lambda country: country["population"]) 

#    - Sort out the ten most spoken languages by location.
#    - Sort out the ten most populated countries.