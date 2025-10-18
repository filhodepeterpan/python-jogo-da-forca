from random import choice

with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip().upper() for linha in  arquivo]

palavra_secreta: str = choice(palavras)
erros: int = 5
fim_de_jogo: bool = False
letras_chutadas = []

def chute(letra: str):
    global erros
    global palavra_secreta

    if erros > 1:

        letra = letra.upper().strip()

        if letra in letras_chutadas:
            print(f"Você já chutou a letra {letra}!")
            return

        if letra in palavra_secreta:
            print(f"✅ A letra '{letra}' está na palavra!")
        else:
            print(f"❌ A letra '{letra}' não está na palavra!")
            erros-=1

        letras_chutadas.append(letra)
    else:
        advinha_palavra(str(input("Seus chutes acabaram! Tente advinhar a palavra completa: ")))

def advinha_palavra(palavra: str):
    global fim_de_jogo
    palavra = palavra.upper().strip()

    if palavra_secreta == palavra:
        print(f"✅ Você acertou! A palavra é {palavra}!")

    else:
        print(f"❌ Você errou... A palavra era {palavra_secreta}!")

    fim_de_jogo = True