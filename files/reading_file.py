# the primary fucntion in python that allows us to manipulate files is the open() function
# r for writing
f = open("dummy_file.txt", "rt")
print(f.read(5))
print('\n')
f.close()

f = open("dummy_file.txt", "rt")
print(f.readline())
print('\n')
f.close()

f = open("dummy_file.txt", "rt")
print(f.readlines()) #returns a lis that contains the entire file content
print('\n')
f.close()

f = open("dummy_file.txt", "rt")
for x in f:
    print(x)
f.close()


f = open("dummy_file.txt", "rt")
# reading the whole file. Pythin uses the idea of a cursor to read a file
print(f.read())
print('\n')
f.seek(0)

print(f.read())
print('\n')
f.seek(0)


print(f.read())
print('\n')
f.seek(0)
f.close()

# to avoid using the f.close() statement use the with / as keywords

with open("dummy_file.txt") as f:
    print(f.readlines())
