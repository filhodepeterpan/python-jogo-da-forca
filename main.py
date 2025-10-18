import forca

print(f"Palavra sorteada (teste): {forca.palavra_secreta}")

print(f"Bem-vindos ao jogo da Forca. Você terá {forca.erros} disponíveis para chutar as letras da palavra\n"
      f"Após os {forca.erros} erros, você terá que advinhar a palavra ou perderá o jogo\n")

while not forca.fim_de_jogo:

    palavra_erros_disponiveis : str = "erros disponíveis" if forca.erros > 1 else "erro disponível"

    print(f"1 - Chutar uma letra. Você tem {forca.erros} {palavra_erros_disponiveis}")
    print("2 - Advinhar a palavra")
    print("\n")

    try:
        escolha = int(input("Você  quer chutar uma letra ou adivinhar a palavra?: "))

        if escolha in [1, 2]:
            if escolha == 1:
                forca.chute(input("Digite uma letra: "))
            else:
                forca.advinha_palavra(input("Tente advinhar a palavra: "))

        else:
            print("ATENÇÃO: Escolha 1 ou 2!")

    except ValueError:
        print("ATENÇÃO: Digite apenas números.")