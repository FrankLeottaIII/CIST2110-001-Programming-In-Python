# In python we have the ability to work with dates and times
# First we need to import the datetime module
import datetime as dt

# We can get the current date and time using the now() method
now = dt.datetime.now()

print(now)

# notice how the date and time is formatted
# we can format the date and time using the strftime() method
# strftime() takes in an argument called a format code

# Example 1
# format the date and time
print(now.strftime("%Y-%m-%d %H:%M:%S")) # -> 2021-03-10 16:11:06
# Just print date and hour minute
print(now.strftime("%Y-%m-%d %H:%M")) # -> 2021-03-10 16:11
# Make the date look like were used to seeing it
print(now.strftime("%m-%d-%Y %H:%M")) # -> 03-10-2021 16:11
# Make the time in 12hr format
print(now.strftime("%m-%d-%Y %I:%M %p")) # -> 03-10-2021 04:11 PM

# Where datetime starts to get really useful is when we start to compare dates and times

# Example 1
# Create a variable to hold a date
date_1 = dt.datetime(2021, 3, 10) # 3/10/2021
# Compare it to the current date
print(date_1 > now) # -> False
print(date_1 < now) # -> True

# how far away in days is date_1 from now
print((date_1 - now).days) # -> # This will be negative because date_1 is in the past

date_2 = dt.datetime(2024, 3, 10) # 3/20/2021
print((date_2 - now).days) # -> # This will be positive because date_2 is in the future

def how_many_days_until_end_of_year():
    # Get the current date
    now = dt.datetime.now()
    # Create a variable to hold the end of year date
    end_of_year = dt.datetime(now.year, 12, 31)
    # Return the difference in days
    return (end_of_year - now).days

print(how_many_days_until_end_of_year())