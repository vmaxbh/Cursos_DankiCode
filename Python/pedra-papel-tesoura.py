from random import choice

jogador_vitorias = 0
maq_vitorias = 0
empate = 0


def Opcao_Jogador():
    esc_jogador = input("Escolha pedra, papel ou tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    else:
        print("Opção invalida, tente novamente")
        Opcao_Jogador()


def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:

    print("-"*30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print("-"*30)

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura")\
        or (esc_jogador == "papel") and (esc_maquina == "pedra")\
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        print(f" jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}        -Resultado: Voce Ganhou!")
        jogador_vitorias += 1

    elif esc_jogador == esc_maquina:
        print(f" jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} -Resultado: Empate!")
        empate += 1

    else:
        print(f" jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}-Resultado: Voce Perdeu!")
        maq_vitorias += 1

    print("-"*30)
    print("-"*30)
    print(f"Vitorias do jogador: {jogador_vitorias}")
    print(f"Vitorias da maquina: {maq_vitorias}")
    print(f"Empate: {empate}")
    print("-"*30)
    print("-"*30)

    esc_jogador = input("Voce quer jogar novamente? ")
    if esc_jogador in ["SIM", "Sim", "sim", "S", "s"]:
        pass
    elif esc_jogador in ["NAO", "Nao", "nao", "n", "N"]:
        break
    else:
        break
