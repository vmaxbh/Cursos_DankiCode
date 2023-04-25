"""Este módulo refere-se ao código responsável por chamar as funções e gerar o grafo."""

from .functions import Graphical

class Grafico(Graphical):

    def __init__(self):
        pass

    def generate_chart(self, datas_x, datas_y, type_chart='plot', view=True, label_x=None, label_y=None, title=None):
        """Método para gerar o gráfico.
        Parâmetros obrigatórios: datas x, datas y.
        Para alterar o formato do gráfico, em type_chart digite:
        enredo, dispersão ou barra.
        Digite False in view= para que o gráfico não seja exibido, mas salvo."""

        Graphical.chech_regularity(datas_x, datas_y)
        datas = [datas_x, datas_y, type_chart, view, label_x, label_y, title]
        self.criar(datas)
        
    def criar(self, datas):
        Graphical.create_chart(datas)