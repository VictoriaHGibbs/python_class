# fix3.3.py
# This is a list containing 5 of the original six hockey teams in the NHL.
# This list is missing the Toronto Maple Leafs
# Fix this program so it inserts the Toronto Maple Leafs after the Chicago Black Hawks, then
# print out the list of the 6 original teams.
# 

original_six = ['Detroit Red Wings', 'Chicago Black Hawks', 'Montreal Canadians', 'Boston Bruins', 'New York Rangers']
missing_team = 'Toronto Maple Leafs'
original_six.insert(2, missing_team)
print(original_six)





