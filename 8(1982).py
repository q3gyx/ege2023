from itertools import product
s='лодка'
i = 0
for k in product(s,repeat=4):
   h = ''.join(k)
   if h.count('о')>=2:
      i+=1
#print(i)
x = 3*(4**2)
x += 2*(4**2)
x += 1*(4**2)
print(x+17)
