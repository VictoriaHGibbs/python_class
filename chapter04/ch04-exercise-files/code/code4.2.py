# code4.2 - Original six plus six
# 
# Back to hockey! 
# You have already been introduced to the original six teams in the previous chapter,
# now we are going to add the next six expansion teams (1967). 
# We are also going to use a new method called extend. The extend method allows you 
# to add a comma separated list instead of using the append() method six times. 
# Hint: all_teams.extend()
#
# There are few ways to solve this problem, but, while we are at it, 
# let's add one more method, copy(). Here is how you could use it
# all_teams = original_six.copy().

# List of Original Six teams
original_six = ["Boston Bruins", "Chicago Blackhawks", "Detroit Red Wings", "Montreal Canadians", "New York Rangers", "Toronto Maple Leafs"]

# List of next six teams added after expansion
next_six_teams = ["Los Angeles Kings", "Minnesota North Stars", "Oakland Seals", "Philadelphia Flyers", "Pittsburgh Penguins", "St. Louis Blues"]

# Extend the Original Six list with the next six teams
# Hint: here is where you can use your all_teams = original_six.copy() and .extents() methods
all_teams = original_six.copy()
all_teams.extend(next_six_teams)
# Alphabetize in reverse order
all_teams_reverse = sorted(all_teams)
all_teams_reverse.reverse()

# Slice the first three teams and the last three teams
first_3_last_3 = all_teams_reverse[0:3]
first_3_last_3.extend(all_teams_reverse[-3:])
# Print out the lists
print("Original Six Teams:")
print(original_six)

print("\nOriginal Six Plus Next Six (Alphabetical Reverse Order):")
print(all_teams_reverse)

print("\nFirst Three Teams and Last Three Teams:")
print(first_3_last_3)
