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
def most_spoken_by_location(countries):
    most_spoken = sorted(countries, key=lambda country: len(country["languages"]), reverse=True)[:10]
    return sorted(most_spoken, key=lambda x: x["name"])
    
#    - Sort out the ten most populated countries.