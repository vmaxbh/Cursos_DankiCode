"""
COmo descobrir um numero par ou impar
"""
print(100 * "_")
numero = int(input("Insira um numero que te digo se ele é par ou impar: "))
if (numero % 2) == 0:
    print(f"{numero} é um numero par!")
else:
    print(f"{numero} é um numero impar!")
print(100 * "_")
