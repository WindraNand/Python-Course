value = 1
# while value <= 10:
#   print(value)
#   if value == 5: 
#     break
#   value += 1
  
# while value <= 10:
#   value += 1
#   if value == 5:
#     continue # skip 5
#   print(value)
# else:
#   print("Value is now equal to " + str(value))

names = ['Daves', 'Sara', 'John']
# for x in names:
#   print(x)
  
# for x in "Mississipi":
#   print(x)

# for x in names:
#   if x == "Sara":
#     break
#   print(x)

# for x in names:
#   if x == "Sara":
#     continue # Skip "Sara"
#   print(x)
  
# for x in range(4):
#   print(x)

# for x in range(2, 4):
#   print(x)

for x in range(0, 101, 5): # format-->(starting num, ending num, increments)
  print(x)
else:
  print("Glad that's over!")
  
names = ["Daves", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for x in names:
#   for y in actions:
#     print(x + " " + y + ".")

for action in actions:
  for name in names:
    print(action + " " + name + ".")
