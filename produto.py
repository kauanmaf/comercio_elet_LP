<<<<<<< HEAD
from exception import Erro_sem_estoque
=======
>>>>>>> 1772f924144b6f90f185f9c5147c31f81da13c0c

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

