from functools import *

def mov(x):
   return x+1, \
          x+2, \
          x+3, \
          x*2


def game(x):
   if x>33: return 'W'
   if any(game(i)=='W' for i in mov(x)):
         return 'P1'

for s in range(1,33):
   if game(s):
      print(s,game(s))
