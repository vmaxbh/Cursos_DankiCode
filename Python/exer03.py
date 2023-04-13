idade = input("Qual a idade do nadador? ")
result = int(idade)
if result >= int(5) and result <= int(7):
    print("Nadador da categoria Infantil A")
if result >= int(8) and result <= int(10):
    print("Nadador da categoria Infantil B")
if result >= int(11) and result <= int(13):
    print("Nadador da categoria Juvenil A")
if result >= int(14) and result <= int(17):
    print("Nadador da categoria Juvenil B")
elif result >= int(18):
    print("Nadador da categoria PROFISSIONAL")
