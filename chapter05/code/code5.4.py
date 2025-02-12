# code5.4.py - Leap years
#
# Write a program that calculates which years are leap years for 
# the year starting 1990 and ending in 2023.
# The rules for a leap year are, if all the following conditions
# are true, then the year is a leap year. 
#
# You will need to use the modulo operator (%) which returns the remainder
# when using integer division
#
# year % 4 == 0
# year % 100 != 0
# year % 400 == 0
# (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
# You are required to use the range() function for the years 1990 - 2023
# And you must loop through the years to test each one.
#
# You will also need to use boolean operators
#
# Print out only the leap years.

start_year = 1990
end_year = 2023

# your code here
for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year!")
