import forca
import cor

# print(f"Palavra sorteada (teste): {forca.palavra_secreta}")

print(f"Bem-vindos ao {cor.verde}Jogo da Forca{cor.padrao}. Você terá {forca.erros} erros disponíveis para chutar as letras da palavra.\n"
      f"Após os {forca.erros} erros, você terá que adivinhar a palavra ou perderá o jogo. IMPORTANTE: Desconsidere acentos.\n")

while not forca.fim_de_jogo:

    palavra_erros_disponiveis : str = "erros disponíveis" if forca.erros > 1 else "erro disponível"

    print(f"{cor.rosa}1 - Chutar uma letra. Você tem {forca.erros} {palavra_erros_disponiveis}")
    print(f"{cor.azul}2 - Adivinhar a palavra")
    print(f"{cor.padrao}\n")

    try:
        escolha = int(input("Você  quer chutar uma letra ou adivinhar a palavra?: "))

        if escolha in [1, 2]:
            if escolha == 1:
                letra = str(input("Digite uma letra: "))

                if len(letra) == 1 and letra.isalpha():
                    forca.chute(letra)
                else:
                    print(f"\n{cor.vermelho}Você {'só pode' if len(letra) > 1 else 'precisa'} digitar uma letra.{cor.padrao}")

                forca.status_palavra()

            else:
                tentativa_palavra = str(input("Tente adivinhar a palavra: ")).strip()

                if tentativa_palavra.isalpha():
                    forca.adivinha_palavra(tentativa_palavra)
                else:
                    print(f"{cor.vermelho}A palavra contém apenas letras.\n")
        else:
            print(f"{cor.vermelho}ATENÇÃO: Escolha 1 ou 2!\n")

    except ValueError:
        print(f"{cor.vermelho}ATENÇÃO: Digite apenas números.\n")

input(f"\n{cor.verde}Pressione Enter para sair...")
