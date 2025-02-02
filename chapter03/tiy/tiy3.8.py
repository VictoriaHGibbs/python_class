places = ['catacombs of paris', 'alcatraz', 'bermuda triangle', 'area 51', 'aokigahara']

print("Here's the original list:")
print(places)
print("----------------------------------------------------------------")

print("Here's the sorted list:")
print(sorted(places))
print("----------------------------------------------------------------")

print("Here's the original list again:")
print(places)
print("----------------------------------------------------------------")

print("Here's the reverse alphabetical sorted list:")
print(sorted(places, reverse=True))
print("----------------------------------------------------------------")

print("Here's the original list again:")
print(places)
print("----------------------------------------------------------------")

print("Here's the reversed sorted list:")
places.reverse()
print(places)
print("----------------------------------------------------------------")

print("Here's the reversed-reversed sorted list:")
places.reverse()
print(places)
print("----------------------------------------------------------------")

print("Here's the permanently sorted list:")
places.sort()
print(places)
print("----------------------------------------------------------------")

print("Here's the reverse-alphabetical permanently sorted list:")
places.sort(reverse=True)
print(places)
print("----------------------------------------------------------------")
