from itertools import product
s='abc'
i = 0
# wxyz = 4 первые 
# wxyz = 4 последние
# всего 16 вариантов

for k in product(s,repeat=4):
      i+=1
print(i*16)
