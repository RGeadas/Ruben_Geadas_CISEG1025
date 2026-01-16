# Segundo Teste Final da Ficha dos Loops

def inserir_cliente(ultimo_id):
    nome_cli=input("Escreve o nome do cliente\n")

    while nome_cli.strip() == "":
        nome_cli=input("Escreve o nome do cliente\n")
    morada_cli=input("Escreve a morada do cliente\n")

    while morada_cli.strip() == "":
        morada_cli=input("Escreve a morada do cliente\n")
    tele_cli=input("Escreve o telemovel do cliente\n")

    while not tele_cli.isdigit() or tele_cli.strip() == "":
        tele_cli=input("Escreve o telemovel do cliente\n")
    nif_cli=input("Escreve o nif do cliente\n")

    while not nif_cli.isdigit() or len(nif_cli) != 9 or nif_cli.strip() == "":
        nif_cli=input("Escreve o nif do cliente\n")

    while True:
        compra_cli = input("Escreve a compra do cliente\n")
        try:
            compra_cli = float(compra_cli)
            break

        except ValueError:
            print("Valor inválido, tente novamente.")

    if 100 <= compra_cli <= 200:
        desconto = 0.05

    elif 200 < compra_cli <= 500:
        desconto = 0.1

    elif compra_cli > 500:
        desconto = 0.15

    elif 0 < compra_cli < 100:
        desconto = 0

    dividafinal=compra_cli-(compra_cli * desconto)
    cliente = {

    "número": ultimo_id,
    "nome": nome_cli,
    "morada": morada_cli,
    "telemovel": tele_cli,
    "nif": nif_cli,
    "compra": compra_cli,
    "Divida Final": dividafinal
    }
    return cliente

ultimo_id = 1
lista = []
contador=0

while True:
    print("#" + 15 * "-" + " Menu " + 15 * "-" + "#") 
    print("1 - Inserir Cliente")
    print("2 - Listar Clientes")
    print("3 - Procurar por NumCli")
    print("4 - Sair")
    print("#" + 36 * "-" + "#") 

    try:
        opc = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opção inválida")
        continue
    
    if opc == 1:
        lista.append(inserir_cliente(ultimo_id))
        ultimo_id+=1

    elif opc == 2:
        for cliente in lista:
            print(f"Número: {cliente['número']}, Nome: {cliente['nome']}, Morada: {cliente['morada']}, Tel: {cliente['telemovel']}, NIF: {cliente['nif']}, Compra: {cliente['compra']:.2f}, Divida Final: {cliente['Divida Final']:.2f}")

            while True:
                contador=input("Queres ir para o proximo cliente: (sim / nao) \n")

                if contador == "sim" or contador == "nao":
                    break

                else:
                    print("Resposta inválida")

            if contador == "nao":
                break

    elif opc == 3:
        cli_encontrado = False
        try:
            opc_num_cli = int(input("Escreve o numero do Cliente que queres ver: "))
        except ValueError:
            print("Número inválido")
            continue

        for cliente in lista:
            if cliente["número"] == opc_num_cli:
                print(f"Número: {cliente['número']}, Nome: {cliente['nome']}, Morada: {cliente['morada']}, Tel: {cliente['telemovel']}, NIF: {cliente['nif']}, Compra: {cliente['compra']:.2f}, Divida Final: {cliente['Divida Final']:.2f}")
                cli_encontrado = True
                break

        if not cli_encontrado:
            print("Cliente não existe")

    elif opc == 4:
        break

    else:
        print("Resposta inválida")