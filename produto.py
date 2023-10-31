from exception_comercio import erro_sem_estoque

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

class Moto(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "M" + str(Produto.codigo)

class Bicicleta(Produto):
    def __init__(self):
        super().__init__()
        self.codigo = "B" + str(Produto.codigo)