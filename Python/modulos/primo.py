
def primo(numero):
    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                return "Esse não eh primo"
        else:
            return "Esse numero eh primo"
    else:
        return "Esse numero nao eh primo: numero menor ou iguasl a 1 "
