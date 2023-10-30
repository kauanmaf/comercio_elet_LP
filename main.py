from inventario import Vendas, Inventario

compras = True

# Criando a estrutura de compras
while compras:
    # Colocando opções para o cliente
    cliente = input("Bem vindo à nossa loja!\nQue ação você quer realizar?\n-Repor\n-Devolver\n-Comprar\n-Inventario\nDigite:")

    # Mostrando o inventário
    if cliente.lower() == "inventario":
        print(f"\n{Inventario()}")

    # Repondo os produtos
    elif cliente.lower() == "repor":
        
        # Pedindo para especificar o tipo e quantidade
        tipo = input("Que tipo de produto?").lower()
        quantidade = input("Quantas unidades?").lower()
        
        # Chamando o método para adicionar
        Vendas.reposicao(Vendas, tipo, quantidade)
    
    # Método para comprar
    elif cliente.lower() == "comprar":
        # Pedindo para especificar o tipo e quantidade
        tipo = input("Que tipo de produto?").lower()
        quantidade = input("Quantas unidades?").lower()

        # Chamando o método para comprar
        Vendas.venda(Vendas, tipo, quantidade)
    
    # Método para devolver um produto
    elif cliente.lower() == "devolver":
        # O cliente diz se o produto está quebrado ou não
        quebrado = input("O produto está quebrado? Se sim, digite 's'. Caso contrário digite 'n'.")

        # Pegunta o tipo e quantidade
        tipo = input("Que tipo de produto?").lower()
        quantidade = input("Quantas unidades?").lower()

        # Realiza os métodos necessários
        if quebrado.lower() == "s":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=True)
        elif quebrado.lower() == "n":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=False)
    
    # Se não digitar nenhuma das opções
    else:
        print("Não entendi, por favor digite uma das opções")
    
    # Dando opções para o usuário
    continuar = input("Deseja fazer algo mais? Se sim, digite 's'. Caso contrário digite 'n'.")

    if continuar.lower() == "n":
        compras = False

# Finalizando as transações
print("Foi um prazer te ter conosco!\n Volte sempre que precisar de um carro, de uma moto ou de uma bicicleta :3")   