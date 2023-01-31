# I = k*v*i*t
k = 2
v = 64*1000
i = 16
I = 48*(2**23) # Мб

t = I // (k*v*i)
print(t//60)
