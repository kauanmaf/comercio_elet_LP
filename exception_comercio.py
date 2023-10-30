# Se não tiver estoque
# pegar 

class erro_sem_produto(Exception):
    def __init__(self, message = "Não temos esse tipo de produto por aqui.\n Escolha entre carro, moto ou bicicleta"):
        self.message = message
        super().__init__(self.message)

class erro_sem_estoque(Exception):
    def __init__(self, message = "Infelizmente não temos o estoque disponível no momento"):
        self.message = message
        super().__init__(self.message)