my_list = []

for char in "HEllo":
    my_list.append(char)

print(my_list)

# this can be done easily with list comprehension
# list/set/dict = [param for param in iterable]
your_list = [char for char in 'hello']
print(your_list)

your_list2 = [num for num in range(0, 100, 2)] #list
your_list3 = (num * 2 for num in range(0, 100)) #set
your_list4 = {num ** 2 for num in range(0, 100) if num % 2 == 0} #set
print(your_list4)

# dictionary comprehensions
simple_dict = {
    'a': 1,
    'b':2
}
my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)


