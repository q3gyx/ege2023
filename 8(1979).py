from itertools import product
s='кресло'
i = 0
for k in product(s,repeat=4):
   if (k[0] == 'к' or   \
       k[0] == 'р' or   \
       k[0] == 'с' or   \
       k[0] == 'л') and \
      (k[3] == 'е' or   \
       k[3] == 'о'):
      i+=1
print(i)
   
