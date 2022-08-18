from collections import Counter, defaultdict, OrderedDict
from array import array
import datetime
import time

#user Counter to get a dict with key as the element and val as the counter of the key inside an iterable
li = [1,2,3,4,5,5,5,2,2,7,7,9]
print(Counter(li))

sentence = 'good morning'
print(Counter(sentence))

#use defaultdict to call a callable function when the key is not found in the dict
mydict = defaultdict(lambda : 'This key not exist', {'a':1, 'b':2})
print(mydict['c'])

#ordered dict can preserve the ordering of insertion of key val pair
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3

d2 = OrderedDict()
d2['a'] = 1
d2['c'] = 2
d2['b'] = 3

print(d1==d2)

# datetime module
print(datetime.time(6,45,28))
print(datetime.date.today)

# array is more efficient in terms of memory than built in list
arr = array('i', [1,2,3])
print(arr)
print(arr[1])