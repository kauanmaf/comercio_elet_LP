from inventario import Vendas, Inventario

compras = True

while compras:
    cliente = input("Bem vindo à nossa loja!\n Que ação você quer realizar? (escolha entre 'repor', 'devolver' ou 'comprar').")

    tipo = input("Que tipo de produto?").lower()
    quantidade = input("Quantas unidades?").lower()

    if cliente.lower() == "repor":
        Vendas.reposicao(Vendas, tipo, quantidade)
    elif cliente.lower() == "comprar":
        Vendas.venda(Vendas, tipo, quantidade)
    elif cliente.lower() == "devolver":
        quebrado = input("O produto está quebrado? Se sim, digite 's'. Caso contrário digite 'n'.")
        if quebrado.lower() == "s":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=True)
        elif quebrado.lower() == "n":
            Vendas.retorno(Vendas, tipo=tipo, qtd=quantidade, quebrado=False)
        
    continuar = input("Deseja fazer algo mais? Se sim, digite 's'. Caso contrário digite 'n'.")

    if continuar.lower() == "n":
        compras = False

print("Foi um prazer te ter conosco!\n Volte sempre que precisar de um carro, de uma moto ou de uma bicicleta :3")   
