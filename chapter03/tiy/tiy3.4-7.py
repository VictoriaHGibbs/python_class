guest = ['grandma ann', 'becca', 'damiana']
print(f"{guest[0].title()} would you like to come to dinner?")
print(f"{guest[1].title()} would you like to come to dinner?")
print(f"{guest[2].title()} would you like to come to dinner?")
print("----------------------------------------------------------------")

popped_guest = guest.pop()
print(f"Unfortunately {popped_guest.title()} can't make it.")
print("----------------------------------------------------------------")


guest.append('zach')
print(f"{guest[0].title()} would you like to come to dinner?")
print(f"{guest[1].title()} would you like to come to dinner?")
print(f"{guest[2].title()} would you like to come to dinner?")
print("----------------------------------------------------------------")


print(f"Hey {guest[0].title()}, I found a bigger table!")
print(f"Hey {guest[1].title()}, I found a bigger table!")
print(f"Hey {guest[2].title()}, I found a bigger table!")
print("----------------------------------------------------------------")

guest.insert(0, 'cynde')
guest.insert(1, 'debra')
guest.append('david')
print("----------------------------------------------------------------")

print(f"{guest[0].title()} would you like to come to dinner?")
print(f"{guest[1].title()} would you like to come to dinner?")
print(f"{guest[2].title()} would you like to come to dinner?")
print(f"{guest[3].title()} would you like to come to dinner?")
print(f"{guest[4].title()} would you like to come to dinner?")
print(f"{guest[5].title()} would you like to come to dinner?")
print("----------------------------------------------------------------")

print("My bad, only 2 of ya'll can come to dinner.")
print("----------------------------------------------------------------")

popped_guest = guest.pop()
print(f"{popped_guest.title()} sorry, you're out.")
popped_guest = guest.pop()
print(f"{popped_guest.title()} sorry, you're out.")
popped_guest = guest.pop()
print(f"{popped_guest.title()} sorry, you're out.")
popped_guest = guest.pop()
print(f"{popped_guest.title()} sorry, you're out.")
print("----------------------------------------------------------------")

print(f"{guest[0].title()} lucky you! You still get to come eat!")
print(f"{guest[1].title()} lucky you! You still get to come eat!")
print("----------------------------------------------------------------")

del guest[0]
del guest[0]
print(guest)
