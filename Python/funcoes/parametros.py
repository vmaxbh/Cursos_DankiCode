
def imprime_nome(nome=None, sobrenome=None, idade=None, profissao=None):
    if imprime_nome != None:
        print("-"*50)
        print("-"*50)
        print(f"Olá {nome} {sobrenome}")
        print(f"Sua idade é: {idade}")
        print(f"Voce trabalha como: {profissao}")
        print("-"*50)
        print("-"*50)
    else:
        print("Inicie seu cadastro novamente")
        print("Bom dia de trabalho!")


nome = input("Qual o seu nome? ")
sobrenome = input("Qual o seu sobrenome? ")
idade = input("Qual a sua idade? ")
profissao = input("Qual a sua profissão? ")
print(imprime_nome(nome, sobrenome, idade, profissao))
