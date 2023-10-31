from produto import Produto
from exception_comercio import *
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
            print(f"{erro.message}")
        except erro_sem_estoque as erro:
            print(f"{erro.message}")
    
    # Averigua o pedido de retorno do produto.
    def retorno(self, tipo, qtd, quebrado):
        try:
            self.tipo = tipo.lower()
        except erro_sem_produto as erro:
            print( f"{erro.message}")
        # Se o veículo estiver quebrado, o produto não retorna ao inventário.
        if quebrado:
            pass
        # Caso contrário, o produto volta ao inventário.
        else:
            Vendas.reposicao(self, tipo, qtd)

    # Realiza a reposição do produto.      
    def reposicao(self, tipo, qtd):
        
        try:
            # Checando se é inteiro
            if isinstance(qtd, int):
                qtd = int(qtd)
            else:
                raise erro_nao_inteiro
            
            # Colocando como lower
            self.tipo = tipo.lower()

            # Chcando se é negativo
            if qtd < 0:
                raise erro_repor_negativo()
            
            
            # Reposição de carro. 
            if tipo == "carro":
                self.qtd_carros(Vendas, qtd)
            # Reposição de moto.    
            elif tipo == "moto":
                self.qtd_motos(Vendas, qtd)
            # Reposição de bicicleta    
            elif tipo == "bicicleta":
                self.qtd_bicicletas(Vendas, qtd)
            else:
                raise erro_sem_produto()
        # Se o produto não possuir nenhum dos tipos anteriores, o veículo não será inserido no estoque.   
        except erro_sem_produto as erro:
            print(f"{erro.message}")
        except erro_repor_negativo as erro:
            print(f"{erro.message}")
        except erro_nao_inteiro as erro:
            print(f"{erro.message}")