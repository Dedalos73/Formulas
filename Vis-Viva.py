import math

M = input('digite a massa do objeto em KG:')
R = input("digite a distancia entre os objeto em metros:")
A = input('Digite o semi eixo maior da orbita em metros:')
G = 6.674 *(10**-11)

V = math.sqrt(float(G)*float(M)*(2/float(R)-1/float(A)))

print(f'A velocidade orbital é de:"{V}m/s²')
