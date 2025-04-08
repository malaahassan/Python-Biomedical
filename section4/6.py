d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3}
all_dicts = [d1, d2, d3]
fin_di = {}

for d in all_dicts:
    fin_di.update(d)

print(fin_di)