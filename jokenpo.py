import random
opcoes = ["pedra", "papel", "tesoura"]
vitoria_maquina = 0
vitoria_user = 0
empate = 0
print("""
Como jogar?
1 - Escolha uma opção (pedra, papel ou tesoura);
2 - A máquina vai escolher uma opção;
3 - Caso você ganhe, sera contabilizado, se perder tambem, e se empatar tambem;
4 - Pedra vence tesoura, papel vence pedra e tesoura vence papel.
Boa sorte!
""")
while True:
    maquina = random.choice(opcoes)
    user = input("Digite sua escolha: ")
    while user not in opcoes:
        print("Opção inválida! Jogue novamente.")
        user = input("Digite sua escolha: ")
    if user.lower() == maquina:
        print(f"Máquina: {maquina}")
        print("É um empate!")
        empate += 1
    elif user.lower() == "tesoura" and maquina == "pedra" or user.lower() == "pedra" and maquina == "papel" or user.lower() == "papel" and maquina == "tesoura":
        print(f"Máquina: {maquina}" )
        print("Vitória da máquina!") 
        vitoria_maquina += 1
    else:
        print(f"Máquina: {maquina}" ) 
        print("Você ganhou!")
        vitoria_user += 1 
    print(f"Suas vitórias: {vitoria_user}")
    print(f"Vitórias da máquina: {vitoria_maquina}")
    print(f"Empates: {empate}")  
    final = input("Você deseja continuar? (s/n): ").lower().strip()
    while final not in ("s", "n"):
        print("Opção inválida. Responda apenas com S ou N.")
        final = input("Você deseja continuar? (s/n): ").lower().strip()
    if final == "s":
        print("Então vamos para mais uma rodada!")
    elif final == "n":
        print("Ok, volte sempre!")
        break