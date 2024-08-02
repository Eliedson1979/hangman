import random


# Função para ler palavras do arquivo
def ler_palavras(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip().upper() for linha in f]


# Função para selecionar dificuldade
def selecionar_dificuldade():
    print("Selecione a dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Sair")
    dificuldade = int(input('Digite a aqui: '))
    print('--------------------------')

    if dificuldade == 1:
        erros_permitidos = 6
        palavras = ler_palavras('palavras_facil.txt')
    elif dificuldade == 2:
        erros_permitidos = 6
        palavras = ler_palavras('palavras_medio.txt')
    elif dificuldade == 3:
        erros_permitidos = 6
        palavras = ler_palavras('palavras_dificil.txt')
    elif dificuldade == 4:
       print("Saindo do jogo...")
       exit()
    else:
        print("Opção inválida. Tente novamente.")

    palavra_secreta = random.choice(palavras)
    return palavra_secreta, erros_permitidos


# Função para calcular o número de tentativas restantes
def numero_tentativas_restantes(erros, erros_permitidos):
    return erros_permitidos - erros


# Função principal do jogo
def jogar_forca():
    nickname = input("Digite seu nickname: ").upper()
    print(f"Seja Bem-vindo(a), {nickname}!")
    print('--------------------------')
    print('      JOGO DA FORCA')
    print('--------------------------')
    palavra_secreta, erros_permitidos = selecionar_dificuldade()
    letras_acertadas = ['_' for _ in palavra_secreta]
    letras_chutadas = []  # Lista para armazenar as letras já chutadas
    erros = 0

    while True:
        print('\nPalavra:', ' '.join(letras_acertadas))
        tentativas_restantes = numero_tentativas_restantes(erros, erros_permitidos)
        print(f"Tentativas restantes: {tentativas_restantes}")

        chute = input("\nChute uma letra ou a palavra completa: ").strip().upper()

        if len(chute) == 1:
            if chute in letras_chutadas:
                print(f"\nVocê já chutou a letra '{chute}'. Tente outra.")
                continue

            letras_chutadas.append(chute)

            if chute in palavra_secreta:
                for i, letra in enumerate(palavra_secreta):
                    if letra == chute:
                        letras_acertadas[i] = letra
            else:
                erros += 1
                print(f"\nErro! Letra '{chute}' não está na palavra.")

        elif chute == palavra_secreta:
            print("\nParabéns! Você acertou a palavra completa!")
            break
        else:
            erros += len(palavra_secreta)  # Penalidade por chutar a palavra errada
            print(f"\nErro! Palavra '{chute}' não está correta.")

        if '_' not in letras_acertadas:
            print("\nParabéns! Você venceu!")
            break

        if erros >= erros_permitidos:
            print(f"\nGame Over! A palavra era '{palavra_secreta}'.")
            break


# Executando o jogo
jogar_forca()
