# Criando uma classe para quando ficar sem produto
class erro_sem_produto(Exception):
    def __init__(self, message = "Não temos esse tipo de produto por aqui.\n Escolha entre carro, moto ou bicicleta"):
        self.message = message
        super().__init__(self.message)

# Criando uma classe para quando estiver sem estoque
class erro_sem_estoque(Exception):
    def __init__(self, message = "Infelizmente não temos o estoque disponível no momento"):
        self.message = message
        super().__init__(self.message)

# Criando erro para quando tentar adicionar um numero negativo
class erro_repor_negativo(Exception):
    def __init__(self, message = "Você não pode adicionar números negativos ao estoque"):
        self.message = message
        super().__init__(self.message)

# Criando erro para quando tentar adicionar um float
class erro_nao_inteiro(Exception):
    def __init__(self, message = "Você não pode adicionar números não inteiros ao estoque"):
        self.message = message
        super().__init__(self.message)