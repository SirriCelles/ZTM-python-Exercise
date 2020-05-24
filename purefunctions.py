# functional programming ... pure function
# some useful functions in python
from functools import reduce

my_list = [1, 2, 3]


# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list

# Using the map function
def multiply_by2(item):
    return item * 2


map_result = list(map(multiply_by2, my_list))
print(map_result, '\n')

# using lambda expression to produce the same result
map_result2 = list(map(lambda item: item * 2, my_list))
print(map_result2, '\n')



# the filter function
def check_odd(item):
    return item % 2 != 0


filter_result = list(filter(check_odd, my_list))
print(filter_result, '\n')

# using lamda expression
filter_result2 = list(filter(lambda item: item % 2 != 0, my_list))
print(filter_result2, '\n')

# using the zip() function

your_list = [10, 20, 30, 40, 50]
zip_result = list(zip(my_list, your_list))
print(zip_result)


# using reduce()
def accumulator(acc, item):
    print(acc, item)
    return acc + item


reduce_result = reduce(accumulator, my_list, 0)
print(reduce_result, '\n')
# lambda Expressions
reduce_result2 = reduce(lambda acc, item: acc + item, my_list, 0)
print(reduce_result2)


# lambda param: action(param)
# implementing lambda expressions on the above functions
