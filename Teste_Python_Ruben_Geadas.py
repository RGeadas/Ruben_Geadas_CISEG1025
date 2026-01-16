limite_filmes = 100
ano_minimo = 1888
ano_atual = 2026

catalogo_filmes = []

def normalizar_texto(texto):
    return texto.strip().lower()

def ler_ano_lancamento():
    try:
        ano = int(input("Ano de lançamento: ").strip())
    except ValueError:
        raise ValueError("Ano inválido: tens de introduzir um número inteiro.")

    if ano < ano_minimo or ano > ano_atual:
        raise ValueError(f"Ano inválido: tem de estar entre {ano_minimo} e {ano_atual}.")
    return ano

def filme_ja_existe(titulo_norm, realizador_norm):
    for filme in catalogo_filmes:
        if filme["titulo"] == titulo_norm and filme["realizador"] == realizador_norm:
            return True
    return False

def adicionar_filme():
    if len(catalogo_filmes) >= limite_filmes:
        print(f"Limite máximo atingido: {limite_filmes} filmes.")
        return

    titulo_original = input("Título do filme: ")
    realizador_original = input("Realizador do filme: ")
    genero_original = input("Género do filme: ")

    titulo = normalizar_texto(titulo_original)
    realizador = normalizar_texto(realizador_original)
    genero = normalizar_texto(genero_original)

    if not titulo or not realizador or not genero:
        print("Erro: título, realizador e género não podem ficar vazios.")
        return

    if filme_ja_existe(titulo, realizador):
        print("Este filme já está registado (mesmo título e realizador).")
        return

    try:
        ano = ler_ano_lancamento()
    except ValueError as erro:
        print(erro)
        return

    catalogo_filmes.append({
        "titulo": titulo,
        "realizador": realizador,
        "ano": ano,
        "genero": genero
    })

    print("\nFilme adicionado com sucesso!")
    print(f"Título:     {titulo_original.strip()}")
    print(f"Realizador: {realizador_original.strip()}")
    print(f"Ano:        {ano}")
    print(f"Género:     {genero_original.strip()}")

def procurar_filmes():
    if not catalogo_filmes:
        print("Não existem filmes registados para procurar.")
        return

    print("\nProcurar por:")
    print("1 - Título")
    print("2 - Realizador")
    print("3 - Género")

    try:
        opcao = int(input("Escolhe uma opção (1-3): ").strip())
    except ValueError:
        print("Entrada inválida. Tens de introduzir um número (1 a 3).")
        return

    if opcao == 1:
        campo = "titulo"
        termo = normalizar_texto(input("Indica o título a procurar: "))
    elif opcao == 2:
        campo = "realizador"
        termo = normalizar_texto(input("Indica o realizador a procurar: "))
    elif opcao == 3:
        campo = "genero"
        termo = normalizar_texto(input("Indica o género a procurar: "))
    else:
        print("Opção inválida.")
        return

    encontrou = False
    for indice, filme in enumerate(catalogo_filmes):
        if filme[campo] == termo:
            encontrou = True
            print(f"\nEncontrado no índice {indice}:")
            print(f"  Título:     {filme['titulo']}")
            print(f"  Realizador: {filme['realizador']}")
            print(f"  Ano:        {filme['ano']}")
            print(f"  Género:     {filme['genero']}")

    if not encontrou:
        print("Não foi encontrado nenhum filme com esse critério.")

def listar_filmes():
    if not catalogo_filmes:
        print("Não existem filmes registados.")
        return

    print("\n===== LISTA DE FILMES REGISTADOS =====")
    for indice, filme in enumerate(catalogo_filmes):
        print(
            f"{indice} -> "
            f"Título: {filme['titulo']} | "
            f"Realizador: {filme['realizador']} | "
            f"Ano: {filme['ano']} | "
            f"Género: {filme['genero']}"
        )

def excluir_filme():
    if not catalogo_filmes:
        print("Não existem filmes para eliminar.")
        return

    listar_filmes()

    try:
        indice = int(input("\nIndica o índice do filme a eliminar: ").strip())
        filme = catalogo_filmes[indice]
    except ValueError:
        print("Entrada inválida. Tens de introduzir um número inteiro.")
        return
    except IndexError:
        print("Índice inválido. Não existe nenhum filme nessa posição.")
        return

    confirmacao = normalizar_texto(
        input(f"Confirmas a eliminação do filme '{filme['titulo']}'? (s/n): ")
    )

    if confirmacao == "s":
        removido = catalogo_filmes.pop(indice)
        print(f"Filme eliminado com sucesso: {removido['titulo']}")
    else:
        print("Eliminação cancelada.")

def ordenar_filmes():
    if not catalogo_filmes:
        print("Não existem filmes para ordenar.")
        return

    print("\nOrdenar por:")
    print("1 - Título")
    print("2 - Realizador")
    print("3 - Ano de lançamento")

    try:
        opcao = int(input("Escolhe uma opção (1-3): ").strip())
    except ValueError:
        print("Entrada inválida. Tens de introduzir um número (1 a 3).")
        return

    print("\nTipo de ordenação:")
    print("1 - Crescente (A -> Z / mais antigo -> mais recente)")
    print("2 - Decrescente (Z -> A / mais recente -> mais antigo)")

    try:
        tipo = int(input("Escolhe uma opção (1-2): ").strip())
    except ValueError:
        print("Entrada inválida. Tens de introduzir um número (1 ou 2).")
        return

    reverso = (tipo == 2)

    if opcao == 1:
        catalogo_filmes.sort(key=lambda f: f["titulo"], reverse=reverso)
        print("Catálogo ordenado por título.")
    elif opcao == 2:
        catalogo_filmes.sort(key=lambda f: f["realizador"], reverse=reverso)
        print("Catálogo ordenado por realizador.")
    elif opcao == 3:
        catalogo_filmes.sort(key=lambda f: f["ano"], reverse=reverso)
        print("Catálogo ordenado por ano de lançamento.")
    else:
        print("Opção inválida.")

def mostrar_menu():
    print("\n#" + 15 * "-" + " Menu do Programa " + 15 * "-" + "#")
    print("1 - Adicionar novo filme")
    print("2 - Procurar por título, realizador ou género")
    print("3 - Eliminar filme")
    print("4 - Ordenar filmes")
    print("5 - Listar filmes")
    print("6 - Sair do programa")
    print("#" + 48 * "-" + "#")

def programa_principal():
    while True:
        mostrar_menu()

        try:
            opcao = int(input("Escolhe uma opção (1-6): ").strip())
        except ValueError:
            print("Opção inválida. Introduz um número de 1 a 6.")
            continue

        if opcao == 1:
            adicionar_filme()
        elif opcao == 2:
            procurar_filmes()
        elif opcao == 3:
            excluir_filme()
        elif opcao == 4:
            ordenar_filmes()
        elif opcao == 5:
            listar_filmes()
        elif opcao == 6:
            print("Programa terminado!")
            break
        else:
            print("Opção inválida. Escolhe um número entre 1 e 6.")

programa_principal()