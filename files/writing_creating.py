# Open file and append content


with open("dummy_file2.txt", "a") as f:
    f.write("This is new content just added to file number 2")

f = open("dummy_file2.txt", "r")
print(f.read())
print('\n')
f.close()

# open file and overwrite content
f = open("dummy_file2.txt", 'w')
f.write(" THis content has overwritten the old one")
f.close()

f = open("dummy_file2.txt", "r")
print(f.read())
print('\n')
f.close()

# inoder to read and write
with open("dummy_file2.txt", "r+") as f:
    f.write("newest")
    print(f.readlines())

try:
    with open('some_file.txt') as f:
        print(f.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err