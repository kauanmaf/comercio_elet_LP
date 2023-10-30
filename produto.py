from exception import Erro_sem_estoque

class Produto:
    codigo = 0
    
    def __init__(self):
        
        Produto.codigo += 1   

    @staticmethod
    def total_produtos_count():
        return Produto.codigo    
        
class Carro(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "C" + str(Produto.codigo)

class Moto(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "M" + str(Produto.codigo)

class Bicicleta(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "B" + str(Produto.codigo)

