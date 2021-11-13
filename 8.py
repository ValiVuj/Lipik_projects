import random
n = random.randint(0,86400)
print(n)
h = n / 3600
m = n % 3600 / 60
s = n % 60
print("Broj sati je", h, "minuta", m, "sekundi",s)