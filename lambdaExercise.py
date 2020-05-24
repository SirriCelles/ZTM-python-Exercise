my_list = [5, 4, 3]

squared_list = list(map(lambda item: item * item, my_list))
print(squared_list)

# List sorting
a = [(0,2), (4,3), (9, 9), (10, -1)]

b = (2, 8, 6, 8,9)
a.sort(key=lambda x: x[1])
print(a)
