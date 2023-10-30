from produto import Produto
import exception_comercio


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
    def __init__(self):
        super().__init__()
   
    def venda(self, tipo, qtd):
        try:
            self.tipo = tipo.lower()
            if self.tipo == "carro":
                if int(qtd) <= Inventario.carro:
                    Inventario.qtd_carros(-int(qtd))
                else:
                    raise exception_comercio.erro_sem_estoque()
            elif self.tipo == "moto":
                Inventario.qtd_motos(-int(qtd))
            elif self.tipo == "bicicleta":
                Inventario.qtd_bicicletas(-int(qtd))
            else:
                raise exception_comercio.erro_sem_produto()


        except exception_comercio.erro_sem_produto as erro:
            return f"{exception_comercio.erro_sem_produto.message}"
        except erro_sem_estoque as erro:
            return f"{exception_comercio.erro_sem_estoqu.message}"
   
    def retorno(self, tipo, qtd, quebrado):
        try:
            self.tipo = tipo.lower()
        except:
            print("Não temos esse tipo de produto por aqui.\n Escolha entre carro, moto ou bicicleta!")
           
        if quebrado:
            pass
        else:
            Vendas.reposicao(self, tipo, qtd)
           
    def reposicao(self, tipo, qtd):
        try:
            self.tipo = tipo.lower()
        except:
            print("Não temos esse tipo de produto por aqui.\n Escolha entre carro, moto ou bicicleta")
           
        if self.tipo == "carro":
            Inventario.qtd_carros(qtd)
        elif self.tipo == "moto":
            Inventario.qtd_motos(qtd)
        elif self.tipo == "bicicleta":
            Inventario.qtd_bicicletas(qtd)
