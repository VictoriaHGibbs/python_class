# code5.2.py

# In this exercise you are given a list of the 7 highest peaks in the Smoky
# Mountains National park. 
# Create an if...else statement that accepts a value for user. 
# If the value is found in the list print
#   {user_peak} is one of the 7 highest mountain peaks in the Smoky Mountain National Park!
# Else print
#   {user_peak} is not in the list of the 7 highest mountain peaks.")



# This is a list of 7 highest mountain peaks in the Smoky Mountain National Park
smoky_peaks = [
    "Clingmans Dome",
    "Mount Guyot",
    "Mount Le Conte",
    "Mount Buckley",
    "Mount Love",
    "Mount Collins",
    "Old Black"
]

smoky_peaks_lc = [smoky_peak.lower() for smoky_peak in smoky_peaks]

# Get user input for a mountain peak

# user_peak = 'Grandfather Mountain'
user_peak = 'grandfather Mountain'

# user_peak = 'Clingmans Dome'
# user_peak = 'clingmans Dome'


# Create your if...else statement here
if user_peak.lower() in smoky_peaks_lc:
    print(f"{user_peak.title()} is one of the 7 highest mountain peaks in the Smoky Mountain National Park!")
else:
    print(f"{user_peak.title()} is not in the list of the 7 highest mountain peaks.")
