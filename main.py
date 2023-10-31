from inventario import Vendas, Inventario

compras = True

# Criando a estrutura de compras
while compras:
    # Colocando opções para o cliente
    cliente = input("\nBem vindo à nossa loja!\n\nQue ação você quer realizar?\n\n-Comprar (para comprar um produto)\n-Devolver (para devolver um produto)\n-Repor (para adicionar produtos no estoque)\n-Inventario (para mostrar os produtos disponíveis) \n\nDigite:")

    # Mostrando o inventário
    if cliente.lower() == "inventario":
        print(f"\n{Inventario()}")

    # Repondo os produtos
    elif cliente.lower() == "repor":
        
        # Pedindo para especificar o tipo e quantidade
        tipo = input("\nQue tipo de produto? ").lower()
        quantidade = input("\nQuantas unidades? ").lower()
        
        # Chamando o método para adicionar
        Vendas.reposicao(Vendas, tipo, quantidade)
    
    # Método para comprar
    elif cliente.lower() == "comprar":
        # Pedindo para especificar o tipo e quantidade
        tipo = input("\nQue tipo de produto? ").lower()
        quantidade = input("\nQuantas unidades? ").lower()

        # Chamando o método para comprar
        Vendas.venda(Vendas, tipo, quantidade)
    
    # Método para devolver um produto
    elif cliente.lower() == "devolver":
        # O cliente diz se o produto está quebrado ou não
        quebrado = input("\nO produto está quebrado? Se sim, digite 's'. Caso contrário digite 'n'.")

        # Pegunta o tipo e quantidade
        tipo = input("\nQue tipo de produto? ").lower()
        quantidade = input("\nQuantas unidades? ").lower()

        # Realiza os métodos necessários
        if quebrado.lower() == "s":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=True)
        elif quebrado.lower() == "n":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=False)
    
    # Se não digitar nenhuma das opções
    else:
        print("\nNão entendi, por favor digite uma das opções ")
    
    # Dando opções para o usuário
    continuar = input("Deseja fazer algo mais? Se sim, digite 's'. Caso contrário digite 'n'. ")

    if continuar.lower() == "n":
        compras = False

# Finalizando as transações
print("Foi um prazer te ter conosco!\n Volte sempre que precisar de um carro, de uma moto ou de uma bicicleta :3")   