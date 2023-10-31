from exception_comercio import erro_sem_estoque
from random import choice

marcas_bicicleta = ["Caloi", "Focus", "Giant"]
marcas_carro = ["Ford", "Fiat", "Toyota", "Volkswagen"]
marcas_moto = ["Honda", "Yamaha", "Suzuki"]

# Classe criada para realizar a contagem de produtos em estoque
class Produto:
    codigo = 0
    
    def __init__(self):
        
        Produto.codigo += 1   

    @staticmethod
    def total_produtos_count():
        return Produto.codigo    

# Elaborando os códigos de identificação dos produtos        
class Carro(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "C" + str(Produto.codigo)
        self.marca = choice(marcas_carro)

class Moto(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "M" + str(Produto.codigo)
        self.marca = choice(marcas_moto)

class Bicicleta(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "B" + str(Produto.codigo)
        self.marca = choice(marcas_bicicleta)
