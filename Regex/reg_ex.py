import re

string = 'Search inside this string'

print('search' in string)

# using
print(re.search('this', string))
# it returns a string match obeject if string is found in patern
a = re.search('this', string)\

print(a.span())
print(a.start())
print(a.end())
print(a.group()) # very useful when doing multiple search

# regular expressions with patterns
pattern = re.compile('string')
b = pattern.search(string)
print(b, '\n')
c = pattern.fullmatch(string)
d = pattern.match(string)

# common function ia the re module
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


