# fix7.1.py - Cyclone
#
# There are two problmes with this program. 
# 1.    It allows people shorter than 48" to ride -- obviously this could cause
#       an undesireable result
# 2.    Python needs the correct data type when gathering user input.
#
# What can you do to fix the problems?

print("You must be at least 48 inches tall to ride the Cyclone rollercoaster")
height = input("How tall are you?")
if height <= 48:
    print("You are tall enought to ride the Cyclone - Enjoy!")
else:
    print("You are not tall enough to ride the Cyclone. Come back next year!")