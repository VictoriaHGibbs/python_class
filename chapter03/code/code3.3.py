# code3.3.py
# Use the canadian_provinces list for the following exercises on sorting


# Canadian Provinces list
canadian_provinces = ['Yukon', 'Northwest Territories', 'Nunavut', 'British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec', 'Newfoundland and Labrador', 'New Brunswick', 'Nova Scotia']

# Sort the list in alphabetical order and print
# Create a variable named sorted_provinces_alpha that stores the new
# list so you don't alter the original list.
# Print the sorted list in alphabetical order
#
# Your code here
sorted_provinces_alpha = sorted(canadian_provinces)
print("Provinces in alphabetical order:")
# Your code here
print(sorted_provinces_alpha)

# Sort the list in reverse alphabetical order and print
# Create a variable named sorted_provinces_reverse that stores the new
# list so you don't alter the original list
# Print the sorted list in reverse alphabetical order
#
#  Your code here
sorted_provinces_reverse = sorted(canadian_provinces, reverse=True)
print("Provinces in reverse alphabetical order:")
# Your code here
print(sorted_provinces_reverse)
print()
# Delete the list and print the deleted list
# Create a variable named deleted_provinces that stores a deleted list
# so you don't alter the original list
# Print the list of provinces to be deleted
deleted_provinces = canadian_provinces.copy()
canadian_provinces.clear()
# Your code here
print("Deleted list of Canadian Provinces:")
# Your code here
print(deleted_provinces)
print()


# Print the empty list (after deletion)
print("Current list after deletion:")
# Your code here
print(canadian_provinces)
