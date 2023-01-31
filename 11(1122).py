for x in range(1,100):
   t = 36**17-6**x+71
   s = []
   while t>0:
      s=[t%6]+s
      t//=6
   if sum(s)==61:
      print(x)
