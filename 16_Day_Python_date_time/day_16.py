# ─────────────────────────────────────────────
## 💻 Exercises: Day 16
# ─────────────────────────────────────────────

from datetime import datetime

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now         = datetime.now()
day         = datetime.now().day
month       = datetime.now().month
year        = datetime.now().year
hour        = datetime.now()
minute      = datetime.now().minute
timestamp   = datetime.now().timestamp

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(f'Current date: {day}/{month}/{year}, {hour}:{minute}')
print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

# 3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print(datetime.strptime(date_string, "%d %B, %Y"))

# 4. Calculate the time difference between now and new year.
new_year = datetime(year = 2027, month = 1, day = 1)
time_diff =  new_year - now
print(time_diff)

# 5. Calculate the time difference between 1 January 1970 and now.
# 6. Think, what can you use the datetime module for? Examples:
#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog 