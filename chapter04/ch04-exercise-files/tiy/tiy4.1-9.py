print("4.1")

pizzas = ['supreme', 'meat lovers', 'greek']
for pizza in pizzas:
  print(f"I like {pizza} pizza!")

print("I really like pizza!")

print("\n4.2")

animals = ['cow', 'pig', 'chicken']
for food  in animals:
  print(f"A {food} can be cute but also delicious!")

print("All these animals are cute and delicious! Nomnomnom")
print("I already did this one before realizing you didn't have it on the list for us to do!")

print("\n4.3")

numbers = list(range(1, 21))
print(numbers)

print("\n4.5")

million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

print("\n4.6")

odd_numbers = list(range(1, 21, 2))
for odd in odd_numbers:
  print(odd)

print("\n4.7")

threes = list(range(3, 31, 3))
for number in threes:
  print(number)

print("\n4.8")

cubes = []
for value in range(1, 11):
  cube = value**3
  print(cube)

print("\n4.9")

cubes = [value**3 for value in range(1, 11)]
print(cubes)
