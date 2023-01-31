from itertools import permutations
s = []
for k in permutations('МИМИКРИЯ'):
   s+=[''.join(k)]
print(len(set(s)))
