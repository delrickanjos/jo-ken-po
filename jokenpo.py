import random

# Cores ANSI
RESET = "\033[0m"
NEGRITO = "\033[1m"
VERDE = "\033[1;32m"
VERMELHO = "\033[1;31m"
AMARELO = "\033[1;33m"
AZUL = "\033[1;34m"
CIANO = "\033[1;36m"

# Inicialização de variáveis
jogador1 = 0
jogador2 = 0
CPU1 = random.choice(["Maya BOT", "Jessica BOT", "Rebeca BOT", "Marina BOT", "Maria Eduarda BOT"])
CPU2 = random.choice(["Carlos BOT", "Pedro BOT", "Juarez BOT", "Fabricio BOT", "Paulo Ricardo BOT"])
escolhaJogador1 = 0
escolhaJogador2 = 0
resultado = 0
pontosJogador1 = 0
pontosJogador2 = 0
placar = 0
vencedor = 0

# Mensagem inicial com as regras do jogo
print(f"{AZUL}{NEGRITO}===================================={RESET}")
print(f"{AZUL}{NEGRITO} BEM VINDO AO JO KEN PO DO DÉLRICK!{RESET}")
print(f"{AZUL}{NEGRITO}===================================={RESET}")
print(f"{CIANO}Caso não saiba jogar, as regras são simples: ")
print("Cada jogador escolherá uma opção secretamente: Pedra ganha de tesoura; Tesoura ganha de papel e")
print(f"papel ganha de pedra. Se escolherem igual, dá empate. Vamos começar, aqui estão as modalidades: {RESET}")

# Menu inicial de modalidades
print("1. Jogador 1 vs Jogador 2")
print("2. Jogador 1 vs Computador")
print("3. Computador vs Computador")
print(f"0. Encerrar o jogo")

# Escolha da modalidade
modalidade = int(input(f"{AMARELO}Digite 1, 2 ou 3 para definir a sua modalidade ou 0 para encerrar o jogo: {RESET}"))
print()

# Código de garantia para que o input seja válido
while modalidade < 0 or modalidade > 3:
    modalidade = int(input("Digite 1, 2 ou 3 para definir a sua modalidade ou 0 para encerrar o jogo: "))
    print()

# Definindo quem são os jogadores de acordo com a modalidade
if modalidade == 1:
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = input("Digite o nome do Jogador 2: ")
    print()
elif modalidade == 2:
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = CPU2
    print(f"O seu adversário será o {VERMELHO}{CPU2}{RESET}.")
    print()
elif modalidade == 3:
    jogador1 = CPU1
    jogador2 = CPU2
    print(f"Muito bem, teremos um embate entre {VERDE}{CPU1}{RESET} e {VERMELHO}{CPU2}{RESET}.")
    print()
# Loop principal do jogo
while modalidade != 0:
    print(f"{AZUL}{NEGRITO}------------------------------{RESET}")
    print(f"{AZUL}{NEGRITO}         NOVA RODADA           {RESET}")
    print(f"{AZUL}{NEGRITO}------------------------------{RESET}")
    print()
    # Modalidade 1: Jogador 1 contra Jogador 2
    while modalidade == 1:
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print()

        # Escolha do jogador 1
        escolhaJogador1 = int(
            input(f"Muito bem. {VERDE}{jogador1}{RESET}, digite a sua escolha entre 1 e 3 com base no menu acima: "))

        # Outro código de garantia de input
        while escolhaJogador1 < 1 or escolhaJogador1 > 3:
            escolhaJogador1 = int(input(
                f"Muito bem. {VERDE}{jogador1}{RESET}, digite a sua escolha entre 1 e 3 com base no menu acima: "))
            print()

        # Escolha do jogador 2
        escolhaJogador2 = int(
            input(
                f"Agora é sua vez {VERMELHO}{jogador2}{RESET}, digite a sua escolha entre 1 e 3 com base no menu acima: "))
        print()

        # Garantia de input do jogador 2
        while escolhaJogador2 < 1 or escolhaJogador2 > 3:
            escolhaJogador2 = int(
                input(
                    f"Agora é sua vez {VERMELHO}{jogador2}{RESET}, digite a sua escolha entre 1 e 3 com base no menu acima: "))
            print()
        break

    # Modalidade 2: Jogador 1 contra CPU
    while modalidade == 2:
        escolhaCPU2 = (random.randint(1, 3))
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print()

        # Jogador 1 escolhe com o código de garantia
        escolhaJogador1 = int(
            input(f"Muito bem. {VERDE}{jogador1}{RESET}, digite a sua escolha entre 1 e 3 com base no menu acima: "))
        print()
        while escolhaJogador1 < 1 or escolhaJogador1 > 3:
            escolhaJogador1 = int(
                input(
                    f"Muito bem. {VERDE}{jogador1}{RESET}, digite a sua escolha entre 1 e 3 com base no menu acima: "))
            print()

        # CPU escolhe automaticamente e código mostra para o usuário qual foi a escolha
        print(f"O seu adversário, {VERMELHO}{CPU2}{RESET}, selecionou o número {escolhaCPU2}.")
        print()
        escolhaJogador2 = escolhaCPU2
        jogador2 = CPU2
        break

    # Modalidade 3: CPU vs CPU
    while modalidade == 3:
        escolhaCPU1 = (random.randint(1, 3))
        escolhaCPU2 = (random.randint(1, 3))
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print(
            f"A escolha da {VERDE}{CPU1}{RESET} foi {escolhaCPU1} e a escolha do {VERMELHO}{CPU2}{RESET} foi {escolhaCPU2}.")
        print()
        escolhaJogador1 = escolhaCPU1
        escolhaJogador2 = escolhaCPU2
        jogador1 = CPU1
        jogador2 = CPU2
        break

    # Verificação de resultados da rodada, independente da modalidade escolhida
    if escolhaJogador1 == 1 and escolhaJogador2 == 1:
        print(f"Como ambos escolheram Pedra, o resultado foi de {AMARELO}empate{RESET}!")
    elif escolhaJogador1 == 2 and escolhaJogador2 == 2:
        print(f"Como ambos escolheram Papel, o resultado foi de {AMARELO}empate{RESET}!")
    elif escolhaJogador1 == 3 and escolhaJogador2 == 3:
        print(f"Como ambos escolheram Tesoura, o resultado foi de {AMARELO}empate{RESET}!")
    elif escolhaJogador1 == 1 and escolhaJogador2 == 2:
        print(
            f"{VERDE}{jogador1}{RESET} escolheu Pedra e {VERMELHO}{jogador2}{RESET} escolheu Papel. {VERMELHO}{jogador2}{RESET} venceu!")
        pontosJogador2 = pontosJogador2 + 1
    elif escolhaJogador1 == 1 and escolhaJogador2 == 3:
        print(
            f"{VERDE}{jogador1}{RESET} escolheu Pedra e {VERMELHO}{jogador2}{RESET} escolheu Tesoura. {VERDE}{jogador1}{RESET} venceu!")
        pontosJogador1 = pontosJogador1 + 1
    elif escolhaJogador1 == 2 and escolhaJogador2 == 1:
        print(
            f"{VERDE}{jogador1}{RESET} escolheu Papel e {VERMELHO}{jogador2}{RESET} escolheu Pedra. {VERDE}{jogador1}{RESET} venceu!")
        pontosJogador1 = pontosJogador1 + 1
    elif escolhaJogador1 == 2 and escolhaJogador2 == 3:
        print(
            f"{VERDE}{jogador1}{RESET} escolheu Papel e {VERMELHO}{jogador2}{RESET} escolheu Tesoura. {VERMELHO}{jogador2}{RESET} venceu!")
        pontosJogador2 = pontosJogador2 + 1
    elif escolhaJogador1 == 3 and escolhaJogador2 == 1:
        print(
            f"{VERDE}{jogador1}{RESET} escolheu Tesoura e {VERMELHO}{jogador2}{RESET} escolheu Pedra. {VERMELHO}{jogador2}{RESET} venceu!")
        pontosJogador2 = pontosJogador2 + 1
    else:
        print(
            f"{VERDE}{jogador1}{RESET} escolheu Tesoura e {VERMELHO}{jogador2}{RESET} escolheu Papel. {VERDE}{jogador1}{RESET} venceu!")
        pontosJogador1 = pontosJogador1 + 1

    # Mostra o placar geral no fim da rodada
    placar = f"{VERDE}{jogador1}{RESET}: {pontosJogador1} e {VERMELHO}{jogador2}{RESET}: {pontosJogador2}"
    print(f"{CIANO}{NEGRITO}Placar geral:{RESET} {placar}")
    print()

    # Pergunta se o usuário deseja continuar jogando ou encerrar o programa
    continuar = int(input("Digite 1 para continuar o jogo e 0 para sair: "))
    print()
    while continuar != 0 and continuar != 1:
        continuar = int(input("Digite 1 para continuar o jogo e 0 para sair: "))
        print()

    # Se o jogador optar por sair, define quem é o vencedor e atualiza o placar sem exibir
    if continuar == 0:
        if pontosJogador1 > pontosJogador2:
            vencedor = f"O vencedor foi {VERDE}{jogador1}{RESET}. Parabéns!"
        elif pontosJogador1 < pontosJogador2:
            vencedor = f"O vencedor foi {VERMELHO}{jogador2}{RESET}. Parabéns!"
        else:
            vencedor = f"Houve um {AMARELO}empate{RESET}!"
        placar = f"{VERDE}{jogador1}{RESET}: {pontosJogador1} e {VERMELHO}{jogador2}{RESET}: {pontosJogador2}"

        # Tela de encerramento, exibindo o vencedor e o placar para o usuário

        print(f"{AZUL}{NEGRITO}===================================={RESET}")
        print(f"{AZUL}{NEGRITO}O placar final ficou:{RESET}")
        print(f"{AZUL}{NEGRITO}{placar}.{RESET}")
        print(f"{AZUL}{NEGRITO}{vencedor}{RESET}")
        print(f"{AZUL}{NEGRITO}Obrigado por jogar.")
        print(f"{VERDE}{NEGRITO}Jogo feito por Délrick dos Anjos Ramos {RESET}")
        print(f"{VERDE}{NEGRITO}BSI PUCPR - 2025-2 {RESET}")
        print(f"{AZUL}{NEGRITO}===================================={RESET}")
        modalidade = 0
