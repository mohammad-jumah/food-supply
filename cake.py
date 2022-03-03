cake = input("Please enter the number of cake slices available:\n")
people = input("Please enter the number of people available:\n")
cake = int(cake)
people = int(people)
print(f'there are {cake} pieces of cakes')
print(f'there are {people} people')

if cake > people:
  print("You have enough cake")
elif cake == people:
  print("You have just enough cake")
elif cake < people:
  print("Make more cake")
else:
  print("error")
