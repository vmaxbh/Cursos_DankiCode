"""Este módulo refere-se ao código para ajudar main.py"""

import matplotlib.pyplot as plt

class Graphical(Exception):

    def __init__(self):
        pass

    def create_chart(datas):
        """Método para criar a imagem gráfica.
        O método espera apenas 1 parâmetro do tipo lista.
        \nEsta é a sequência de dados dentro da lista:
        \ndates[dates_x, date_y, type_chart, view, label_x, label_y, title]
        \nEsta string não pode ser alterada."""

        try:
            plt.xlabel(datas[4]) if datas[4]!=None else ""
            plt.ylabel(datas[5]) if datas[5]!=None else ""
            plt.title(datas[6]) if datas[6]!=None else ""

            if datas[2]=='scatter':
                plt.scatter(datas[0], datas[1])
            if datas[2]=='bar':
                plt.bar(datas[0], datas[1])
            if datas[2]=='plot':
                plt.plot(datas[0], datas[1])

            plt.show() if datas[3] else plt.savefig("Grafico.png")
        except:
            raise Graphical("Error: failed to creat chart image.")


    def chech_regularity(datas_x, datas_y):
        """Função para verificar as regularidades dos parâmetros.
        \nIsso não retorna nada. Se algo der errado, o programa receberá uma exceção."""
        
        if type(datas_x)==type(datas_y)==list:
            if len(datas_x)!=len(datas_y):
                raise Graphical("Lists must be the same size.")
        else:
            raise Graphical("Expected to receive list as parameter.")