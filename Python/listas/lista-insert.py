lista = ["carro", "barco", "aviao", "moto", "onibus", "carroca", "van", "iate"]
print(lista)

lista.insert(2, "Bicicleta")
for x in range(len(lista)):
    print(x, lista[x])
print("Inserindo o item 'bicicleta' na posicao 2 de nossa lista")
# para remover um indice use o .remove("indice") 
# para remover o ultimo indice da lista use .pop()
# para remover uma lista inteira use del lista()
        