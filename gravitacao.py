m1 = input('digite a massa do primeiro objeto em KG:')
m2 = input('digite a massa do segundo objeto em KG:')
d = input("digite a distancia entre os objeto em metros:")
G = 6.674 *(10**-11)

F = G * (float(m1)*float(m2))/(float(d)**2)
print(f'A força gravitacional entre os corpos é de:" {F}N')
