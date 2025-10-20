import forca
import cor

# print(f"Palavra sorteada (teste): {forca.palavra_secreta}")

print(f"Bem-vindos ao {cor.verde}Jogo da Forca{cor.padrao}. Você terá {forca.erros} erros disponíveis para chutar as letras da palavra.\n"
      f"Após os {forca.erros} erros, você terá que adivinhar a palavra ou perderá o jogo. {cor.azul}IMPORTANTE: Desconsidere acentos.{cor.padrao}\n")

while not forca.fim_de_jogo:

    palavra_erros_disponiveis : str = "erros disponíveis" if forca.erros > 1 else "erro disponível"

    print(f"{cor.rosa}Você tem {forca.erros} {palavra_erros_disponiveis}")
    print(f"{cor.padrao}\n")

    try:
        letra = str(input("Digite uma letra ou tente adivinhar uma palavra: "))

        if letra.isalpha():
            forca.chute(letra)

            if len(letra) == 1:
                forca.status_palavra()
        else:
            print(f"{cor.vermelho}ATENÇÃO: Digite apenas letras.\n")
            
    except ValueError:
        print(f"{cor.vermelho}ATENÇÃO: Digite apenas letras.\n")

input(f"\n{cor.verde}Pressione Enter para sair...")
