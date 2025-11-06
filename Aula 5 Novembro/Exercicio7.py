"""7. Classificação de produto
Recebe um dicionário com as chaves "categoria" e "preco".
Retorna:
•	“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
•	“Produto comum” se categoria for “eletrônico” e preço até 1000
•	“Produto alimentar” se categoria for “alimento”
•	“Categoria desconhecida” caso contrário
Exemplo:
Entrada → {"categoria": "eletrônico", "preco": 1500}
Saída → Produto de luxo
"""

produto = {
    "categoria": input("Categoria (eletrônico/alimento) ").lower(),
    "preco": float(input("Preço (€) "))
}

if produto["categoria"] == "eletrônico" and produto["preco"] > 1000:
    print("Produto de luxo")
elif produto["categoria"] == "eletrônico":
    print("Produto comum")
elif produto["categoria"] == "alimento":
    print("Produto alimentar")
else:
    print("Categoria desconhecida")
