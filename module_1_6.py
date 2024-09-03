my_dict={'Masha':1981, 'Ira':1985, 'Dasha':1990, 'Misha':1987}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Yana'))
my_dict.update({'Tom':2005, 'Mark':2015})
a = my_dict.pop('Ira')
print(a)
del my_dict['Dasha']
print(my_dict.get('Misha'))
print(my_dict)

my_set={1, 1, 1, 1, 1, 42.314, 'Яблоко'}
print(my_set)
my_set.add(4)
my_set.add(5)
my_set.discard(1)
print(my_set)

