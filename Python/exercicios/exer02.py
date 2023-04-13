idade = input("qual a sua idade? ")
result = int(idade)
if result < int(16):
    print("Voce é MENOR!")
if result >= int(16) and result < int(18):
    print("Voce é EMANCIPADO!")
if result >= int(18):
    print("Voce é de MAIOR!")
