import random
opcoes = ["pedra", "papel", "tesoura"]
vitoria_maquina = 0
vitoria_user = 0
empate = 0
while True:
    maquina = random.choice(opcoes)
    user = input("Digite sua escolha: ")
    print(f"Máquina: {maquina}" )
    if user.lower() == maquina:
        print("É um empate!")
        empate += 1
    elif user.lower() == "tesoura" and maquina == "pedra" or user.lower() == "pedra" and maquina == "papel" or user.lower() == "papel" and maquina == "tesoura":
        print("Vitória da máquina!") 
        vitoria_maquina += 1
    else: 
        print("Você ganhou!")
        vitoria_user += 1 
    print(f"Suas vitórias: {vitoria_user}")
    print(f"Vitórias da máquina: {vitoria_maquina}")
    print(f"Empates: {empate}")  
    final = input("Você deseja continuar? (s/n): ")
    if final.lower() == "s":
        print("Então vamos para mais uma rodada!")
        continue
    elif final == "n":
        print("Ok, volte sempre!")
        break