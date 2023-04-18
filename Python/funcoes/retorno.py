def par_impar():
    numero = 5
    if (numero % 2) == 0:
        return "Esse numero é Par"
    return "Esse numero é Impar"


def calc_idade():
    ano_atual = 2023
    ano_nasc = 1989
    idade = ano_atual - ano_nasc
    return "A sua idade é: ", idade


print(par_impar())
print(calc_idade())
              