from produto import Produto
from exception_comercio import erro_sem_estoque, erro_sem_produto

class Inventario:
    carro = 20
    moto = 20
    bicicleta = 20

    def __init__(self):
        pass

    def qtd_carros(self, qtd):
        Inventario.carro += int(qtd)

    def qtd_motos(self, qtd):
        Inventario.moto += int(qtd)

    def qtd_bicicletas(self, qtd):
        Inventario.bicicleta += int(qtd)
        
    def mostrar_inventario(self):
        print(f"Carros: {Inventario.carro}\nMotos: {Inventario.moto}\nBicicletas: {Inventario.bicicleta}")


class Vendas(Inventario):
    def __init__(self, qtd_carros, qtd_motos, qtd_bicicletas):
        super().__init()
        self.qtd_carros(qtd_carros)
        self.qtd_motos(qtd_motos)
        self.qtd_bicicletas(qtd_bicicletas)

   
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
                    Inventario.qtd_carros(Vendas, -int(qtd))
                else:
                    raise erro_sem_estoque()
            elif self.tipo == "bicicleta":
                if Inventario.bicicleta - int(qtd) >= 0:
                    Inventario.qtd_carros(Vendas, -int(qtd))
                else:
                    raise erro_sem_estoque()
                
        except erro_sem_produto as erro:
            return f"{erro_sem_produto.message}"
        except erro_sem_estoque as erro:
            return f"{erro_sem_estoque.message}"
   
    def retorno(self, tipo, qtd, quebrado):
        try:
            self.tipo = tipo.lower()
        except erro_sem_produto as erro:
            return f"{erro_sem_produto.message}"
           
        if quebrado:
            pass
        else:
            Vendas.reposicao(self, tipo, qtd)
           
    def reposicao(self, tipo, qtd):
        qtd = int(qtd)

        if tipo == "carro":
            self.qtd_carros(qtd)
        elif tipo == "moto":
            self.qtd_motos(qtd)
        elif tipo == "bicicleta":
            self.qtd_bicicletas(qtd)
            
        try:
            self.tipo = tipo.lower()
        except erro_sem_produto as erro:
            return f"{erro_sem_produto.message}"