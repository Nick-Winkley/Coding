"""
Dictionaries are unordered mappings for storing objects. 
Dictionaries use a key-value pairing
key-value pair allows users to quickly grab objects without needing to know an index location

{'key1';'value1','key2':'value2'}
Dictionaries are unordered and cannot be sorted.

Lists are ordered and can be indexed and sliced.

Keys themselves should always be strings

"""

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
print(my_dict['key1'])

pricesLookup = {'apple':2.99,'oranges':1.99,'milk':5.80}
print(pricesLookup['apple'])

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k3']['insideKey'])

d = {'key1':['a','b','c']}
print(d['key1'][2].upper())


d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
print(d.values())
print(d.items())



