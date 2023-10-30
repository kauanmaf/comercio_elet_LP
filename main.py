from inventario import Vendas, Inventario

compras = True

while compras:
    cliente = input("Bem vindo à nossa loja!\nQue ação você quer realizar?\n-Repor\n-Devolver\n-Comprar\nInventario\nDigite:")
    if cliente.lower() == "inventario":
        print(Inventario())

    elif cliente.lower() == "repor":
        tipo = input("Que tipo de produto?").lower()
        quantidade = input("Quantas unidades?").lower()
        Vendas.reposicao(Vendas, tipo, quantidade)
    elif cliente.lower() == "comprar":
        tipo = input("Que tipo de produto?").lower()
        quantidade = input("Quantas unidades?").lower()
        Vendas.venda(Vendas, tipo, quantidade)
    elif cliente.lower() == "devolver":
        quebrado = input("O produto está quebrado? Se sim, digite 's'. Caso contrário digite 'n'.")
        tipo = input("Que tipo de produto?").lower()
        quantidade = input("Quantas unidades?").lower()
        if quebrado.lower() == "s":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=True)
        elif quebrado.lower() == "n":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=False)
    
    else:
        print("Não entendi, por favor digite uma das opções")
        
    continuar = input("Deseja fazer algo mais? Se sim, digite 's'. Caso contrário digite 'n'.")

    if continuar.lower() == "n":
        compras = False

print("Foi um prazer te ter conosco!\n Volte sempre que precisar de um carro, de uma moto ou de uma bicicleta :3")   
