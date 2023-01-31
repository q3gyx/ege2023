from itertools import product
s='сало'
i = 0
for k in product(s,repeat=6):
   h = ''.join(k)
   if 0< h.count('о') <=3:
      i+=1
print(i)

