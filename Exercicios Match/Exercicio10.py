"""10. Jogo: Pedra, Papel ou Tesoura
Cria um programa que receba duas jogadas:
•	Jogador 1
•	Jogador 2
Usa match para determinar o resultado:
•	Pedra ganha de Tesoura
•	Tesoura ganha de Papel
•	Papel ganha de Pedra
•	Se forem iguais, é Empate
Exemplo:
Entrada →
Jogador 1: pedra
Jogador 2: tesoura
Saída → Jogador 1 venceu
"""

jogador1 = input("Jogada do Jogador 1 (pedra/papel/tesoura) ").lower()
jogador2 = input("Jogada do Jogador 2 (pedra/papel/tesoura) ").lower()

match (jogador1, jogador2):
    case (a, b) if a == b:
        print("Empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")
