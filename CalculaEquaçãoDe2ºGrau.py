#Código que calcule uma equação de segundo grau

a=float(input('Digite o valor de A -> '))
b=float(input('Digite o valor de B -> '))
c=float(input('Digite o valor de C -> '))
d=float(input('Digite o valor que vem após 0 = -> '))
c=c-d

delta = b**2-4*a*c

raiz_delta = delta**0.5

x1 = (-b+raiz_delta) / (2*a)
x2 = (-b-raiz_delta) / (2*a)

print(f'O delta é igual a {delta}')

if delta >=0:
    print(f'x1 = {x1}\nx2 = {x2}')

else: print('O valor de delta é negativo equação não pode ser finalizada')