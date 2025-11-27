import random


def boas_vindas():
    """Exibe a mensagem de boas-vindas e introduz o jogo."""
    print("*" * 35)
    print("🎯 Bem-vindo ao Jogo de Adivinhação! 🎯")
    print("*" * 35)


def definir_dificuldade():
    """Permite ao usuário escolher o nível de dificuldade e retorna o limite de tentativas."""
    print("\nEscolha o Nível de Dificuldade:")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    while True:
        try:
            nivel = int(input("Digite o nível (1, 2 ou 3): "))

            if nivel == 1:
                return 20  # Nível Fácil: 20 Tentativas
            elif nivel == 2:
                return 10  # Nível Médio: 10 Tentativas
            elif nivel == 3:
                return 5  # Nível Difícil: 5 Tentativas
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


def jogar():
    """Função principal que contém toda a lógica do jogo."""

    boas_vindas()

    # 1. Configuração
    numero_secreto = random.randint(1, 100)
    total_de_tentativas = definir_dificuldade()
    pontos = 1000  # Pontuação inicial

    print(f"\nO número secreto está entre 1 e 100. Você tem {total_de_tentativas} tentativas.")

    # 2. Laço Principal do Jogo (While)
    for rodada in range(1, total_de_tentativas + 1):
        print(f"\n--- Tentativa {rodada} de {total_de_tentativas} ---")

        try:
            chute_str = input("Digite o seu chute (um número inteiro): ")
            chute = int(chute_str)
        except ValueError:
            print("Você deve digitar um número inteiro. Perdeu uma rodada.")
            continue  # Pula para a próxima rodada

        # 3. Verificação de Intervalo (Melhoria)
        if chute < 1 or chute > 100:
            print("Atenção! O chute deve ser um número entre 1 e 100.")
            continue  # Pula para a próxima rodada

        # 4. Estrutura de Decisão (If/Elif/Else)
        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print(f"🥳 PARABÉNS! Você acertou na {rodada}ª tentativa!")
            print(f"Sua pontuação final foi de {pontos} pontos.")
            break  # Sai do loop for
        elif maior:
            print("📉 Você errou! O número secreto é MENOR. Tente novamente.")
        else:  # Menor
            print("📈 Você errou! O número secreto é MAIOR. Tente novamente.")

        # 5. Cálculo de Pontuação
        pontos_perdidos = abs(numero_secreto - chute)  # Quanto mais longe, mais pontos perde
        pontos = pontos - pontos_perdidos

    # 6. Fim do Jogo (Se o loop terminar sem acerto)
    if not acertou:
        print("\nVocê perdeu todas as tentativas!")
        print(f"O número secreto era {numero_secreto}.")

    print("\nFim do Jogo!")


if __name__ == "__main__":
    jogar()