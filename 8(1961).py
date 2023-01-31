from itertools import product
i = 0
for k in product('ЕЛМРУ',repeat=4):
   i = i + 1
   if k[0]=='Л':
      print(i, ''.join(k) )
      break
