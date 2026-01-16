#input() le o que escrevemos no terminal

nome=""
altura=0.0           #tipo float numeros com virgula (.)
num1=0

print("Introduza o seu nome")
nome=input()

print(type(nome))

        #float <---- String     casting
altura=float(input("introduza a sua altura"))

print(type(altura))

        #int <---- String     casting

num1=int(input("introduza um numero"))

print(type(num1), end="\n\n")

print(f"Este é o seu nome : {nome} e a sua altura é {altura} e o seu numero é {num1}" )
