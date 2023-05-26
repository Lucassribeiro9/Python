import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li': [0 ,1 ,2],
}
d2 = d1.copy() # copia rasa
d3 = copy.deepcopy(d1)
d2['c1'] = 1000
d2['li'][1] = 9999
print(d1)
print(d2) 
print(d3)