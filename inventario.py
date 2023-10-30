class Inventario:
    def __init__(self):
        self.carro = 20
        self.carro = 20
        self.carro = 20
    
    def qtd_carros(self, qtd):
        self.carro += qtd
        
    def qtd_motos(self, qtd):
        self.moto += qtd
        
    def qtd_bicicletas(self, qtd):
        self.bicicleta += qtd
        
class Vendas(Inventario):
    def __init__(self):
        super().__init__()
    
    def venda(self, tipo, qtd):
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