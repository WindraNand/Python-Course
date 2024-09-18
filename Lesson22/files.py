import os

#   R = Read
#   A = Append
#   W = Write
#   X = Create / Delete

## Read - error if it doesn't exist

f = open("./Lesson22/names.txt")
# print(f.read())

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)
    
f.close()

try:
    f = open("./Lesson22/names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()
    
## Append - creates the file if it doesn't exist

f = open("./Lesson22/names.txt", "a")
f.write("\nNeil")
f.close()

f = open("./Lesson22/names.txt")
print(f.read())
f.close()

## Write (overwrite)
f = open("./Lesson22/context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("./Lesson22/context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it doesn't exist


f = open("./Lesson22/name_list.txt", "w")
f.close()

# Creates the specified file but returns an error if the file exist
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()
    
# Delete a file

# Avoid an Error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete doesn't exist")

with open("./Lesson22/more_names.txt") as f:
    content = f.read()
    
with open("./Lesson22/names.txt", "w") as f:
    f.write(content)