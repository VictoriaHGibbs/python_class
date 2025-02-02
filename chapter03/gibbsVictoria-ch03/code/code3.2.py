# 3.2.py
# Use the list of Canadian Provinces to solve this exercise 

# Initial list of Canadian Provinces
canadian_provinces = ['Yukon', 'Northwest Territories', 'Nunavut', 'British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec', 'Newfoundland and Labrador', 'New Brunswick', 'Nova Scotia']

# Display the initial list of provinces
print("Initial list of Canadian Provinces:")
# Your code here
print(canadian_provinces)

# Delete the first province using pop()
# Use a variable named deleted_first_province
deleted_first_province = canadian_provinces.pop(0)
# Print the line using the variable deleted_first_province
# Use the \n character to create a new line
#
# Your output should be
# The first province, Yukon, has been deleted.
#
# Your code here
print(f"The first province, {deleted_first_province}, has been deleted.\n")
print("The new list:\n")
print(canadian_provinces)
# Delete the last province using pop() - hint: you can use a negative number
# Use a variable named deleted_last_province
deleted_last_province = canadian_provinces.pop()
# Print this line using the variable  deleted_last_province
# Use the \n character to create a new line

# Your output should be
# The last province, Nova Scotia, has been deleted.
#
# Your code here
print(f"The last province, {deleted_last_province}, has been deleted.\n ")
# Display the entire list with the two missing provinces
print(f"\nModified list of Canadian Provinces:")
#
# Your code here
print(canadian_provinces)


