import pyjokes

joke = pyjokes.get_joke('en', 'neutral')

print(joke)

# some useful python modules
from collections import Counter, defaultdict, OrderedDict

li = [1, 2,3,4,5,6,7,8]
sentence = " I love python bla bla blah bhal"
# counter creates a counter object that keeps track of how many times an iterable has occured
print(Counter(li))
print(Counter(sentence))


dictionary = defaultdict(lambda: "does not exist", {'a' : 1, 'b': 2})
print(dictionary['a'])
print(dictionary['c'])

# an ordereddictionary retais the order that you insert into the dict
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1


print(d2 == d)