"""
As tuplas são imutaveis não alteraveis , mas se convertermos uma tupla para lista e depois convertermos essa lista para tupla conseguimos atualizar alterações nas mesmas.
Lembrando que as listas são criadas dentro de [], e as tuplas sao criadas como padrão dentro de (), mas o que define a tupla é a virguila ex: "Pai",
"""
tupla = ("Pai", "Filho", "Mae")
print(tupla)
listatup = list(tupla)
print(listatup)
listatup.append("sobrinho")
print(listatup)
tupla = tuple(listatup)
print(tupla)
