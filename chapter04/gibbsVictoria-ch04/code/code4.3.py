# code4.3 - Adding to 10
# In this exercise you are required to use the range function to create 
# an odd-numbered list from 1 to 9, then creates an even-numbered list 
# from 2 to 10. Finally, join the two lists (Hint: you can use the + operator!)
# Then sort the new list so it displays the numbers from 1 to 10
#
# Using the range function, create an odd-numbered list from 1 to 9
odd_numbers = list(range(1, 10, 2))

# Using the range function, create an even-numbered list from 2 to 10
even_numbers = list(range(2, 11, 2))

# Join the two lists
combined_list = odd_numbers + even_numbers
print(combined_list)

# Sort the combined list
sorted_list = sorted(combined_list)

# Display all three lists
print("Odd-Numbered List (1 to 9):")
print(odd_numbers)

print("\nEven-Numbered List (2 to 10):")
print(even_numbers)

print("\nCombined and Sorted List (1 to 10):")
print(sorted_list)
