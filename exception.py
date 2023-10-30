# Se não tiver estoque
# pegar 

class Erro_sem_estoque(Exception):
    def __init__(self, message = "Deu Ruim, Mané!"):
        self.message = message
        super().__init__(self.message)
try:
    raise Erro_sem_estoque()
except Erro_sem_estoque as erro:
    print(erro.message)