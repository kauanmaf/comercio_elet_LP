from produto import Produto
from exception_comercio import erro_sem_estoque, erro_sem_produto

# Classe elaborada para armazenar e disponibilizar informações referentes ao estoque de produtos.
class Inventario:
    # Disponibilidade de cada produto.
    carro = 20
    moto = 20
    bicicleta = 20

    def __init__(self):
        pass

    # Aumenta a quantidade de carros no inventário.
    def qtd_carros(self, qtd):
        Inventario.carro += int(qtd)
 
    # Aumenta o total de motos no inventário.
    def qtd_motos(self, qtd):
        Inventario.moto += int(qtd)
 
    # Aumenta o número de motos no inventário.
    def qtd_bicicletas(self, qtd):
        Inventario.bicicleta += int(qtd)
   
   # Retorna a quantidade disponível de cada produto.
    def __str__(self):
        return f"Carros: {Inventario.carro}\nMotos: {Inventario.moto}\nBicicletas: {Inventario.bicicleta}"

# Classe construída para realizar processos relacionados às vendas de produtos.
class Vendas(Inventario):
    def __init__(self, qtd_carros, qtd_motos, qtd_bicicletas):
        super().__init()
        self.qtd_carros(qtd_carros)
        self.qtd_motos(qtd_motos)
        self.qtd_bicicletas(qtd_bicicletas)

    # Verifica a disponibilidade da quantidade de um determinado produto no estoque.
    def venda(self, tipo, qtd):
        try:
            self.tipo = tipo.lower()
            if self.tipo == "carro":
                if Inventario.carro - int(qtd) >= 0:
                    Inventario.qtd_carros(Vendas, -int(qtd))
                else:
                    raise erro_sem_estoque()
            elif self.tipo == "moto":
                if Inventario.moto - int(qtd) >= 0:
                    Inventario.qtd_motos(Vendas, -int(qtd))
                else:
                    raise erro_sem_estoque()
            elif self.tipo == "bicicleta":
                if Inventario.bicicleta - int(qtd) >= 0:
                    Inventario.qtd_bicicletas(Vendas, -int(qtd))
                else:
                    raise erro_sem_estoque()
            else:
                raise erro_sem_produto()
        except erro_sem_produto as erro:
            return f"{erro_sem_produto.message}"
        except erro_sem_estoque as erro:
            return f"{erro_sem_estoque.message}"
    
    # Averigua a possibilidade de retorno do produto.
    def retorno(self, tipo, qtd, quebrado):
        try:
            self.tipo = tipo.lower()
        except erro_sem_produto as erro:
            return f"{erro_sem_produto.message}"

        # Se o veículo estiver quebrado, o produto não retorna ao estoque.   
        if quebrado:
            pass
        # Caso contrário, o produto volta ao estoque.
        else:
            Vendas.reposicao(self, tipo, qtd)

    # Realiza a reposição do produto.      
    def reposicao(self, tipo, qtd):
        qtd = int(qtd)

        # Reposição de carro. 
        if tipo == "carro":
            self.qtd_carros(qtd)
        # Reposição de moto.    
        elif tipo == "moto":
            self.qtd_motos(qtd)
        # Reposição de bicicleta    
        elif tipo == "bicicleta":
            self.qtd_bicicletas(qtd)
            
        try:
            self.tipo = tipo.lower()
        # Se o produto não possuir nenhum dos tipos anteriores, o veículo não será inserido no estoque.   
        except erro_sem_produto as erro:
            return f"{erro_sem_produto.message}"
