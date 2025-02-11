# fix5.3.py
#
# What's wrong here?
# We have a list of error levels and all of them are being displayed on
# the screen. Alter the program so that _only_ the Notice displays. 
# Do not modify the error_1, 2, or 3 variables.

error_levels = ['Notice', 'Warning', 'Fatal']
error_1 = 'Notice'
error_2 = 'Warning'
error_3 = 'Fatal'

if(error_levels[0] == error_1):
    print(f"Error level: {error_levels[0]}")
if(error_levels[1] == error_2):
    print(f"Error level: {error_levels[1]}")
if(error_levels[2] == error_3):
    print(f"Error level: {error_levels[2]}")
    