# code5.3.py
#
# In this exercise you are provided two lists. 
# 1. A list of the 7 highest peaks in the Smoky Mountains
# 2. A list containing additional peaks in the Smoky Mountains.
# The additional list also contains two peaks that are in the 7
# highest list.
# Write a short program that uses a for loop and an if...else
# conditional statement that looks for a match between the two lists.
# If there is a match then display one of the two print statements provided
# for you in the code.
# 


# List of the 7 highest peaks in the Great Smoky Mountains National Park
highest_peaks = [
    "Clingmans Dome",
    "Mount Guyot",
    "Mount Le Conte",
    "Mount Buckley",
    "Mount Love",
    "Mount Collins",
    "Old Black"
]

# List of additional peaks
additional_peaks = [
    "Mount Cammerer",
    "Mount Sterling",
    "Clingmans Dome",
    "Mount Sequoyah",
    "Mount Le Conte"
]

# Check for matches between the two lists and print the result
print("Matching Peaks (7 Highest Peaks in Smoky Mountains):")
for peak in additional_peaks:
    if peak in highest_peaks:
        print(f"{peak} is one of the 7 highest peaks in the Smoky Mountains.")
    else:
        print(f"{peak} is not in the list of the 7 highest peaks.")
