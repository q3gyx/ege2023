for x in range(1,4000):
   t = 4**2015+2**x -2**2015 + 15
   s = bin(t)[2:]
   if s.count('1')==500:
      print(x)
