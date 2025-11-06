"""9. Processamento de requisição
Recebe um dicionário com as chaves "metodo" e "conteudo".
Retorna:
•	“Requisição GET recebida” se o método for “GET”
•	“Requisição POST com dados válidos” se o método for “POST” e o conteúdo não estiver vazio
•	“Requisição POST sem dados” se o método for “POST” e o conteúdo estiver vazio
•	“Método não suportado” caso contrário
Exemplo:
Entrada → {"metodo": "POST", "conteudo": ""}
Saída → Requisição POST sem dados
"""

metodo = input("Método (GET/POST) ").upper()
conteudo = input("Conteúdo ")

requisicao = {"metodo": metodo, "conteudo": conteudo}

if requisicao["metodo"] == "GET":
    print("Requisição GET recebida")
elif requisicao["metodo"] == "POST" and requisicao["conteudo"]:
    print("Requisição POST com dados válidos")
elif requisicao["metodo"] == "POST":
    print("Requisição POST sem dados")
else:
    print("Método não suportado")
