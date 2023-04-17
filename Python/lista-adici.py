lista = ["carro", "barco", "aviao", "moto", "onibus", "carroca", "van", "iate"]
print(lista)
for x in range(len(lista)):
    print(x, lista[x])

# Aqui estamos adicionando dois itens a nossa lista funcao 'append'
lista.append("submnarino")
lista.append("navio")
print(lista)
for x in range(len(lista)):
    print(x, lista[x])
