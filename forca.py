from random import choice
from pathlib import Path
import cor

caminho = Path(__file__).parent / "palavras.txt"
with open(caminho, "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip().upper() for linha in arquivo]

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
            print(f"\n✅ A letra {cor.verde}{letra}{cor.padrao} está na palavra!")

        else:
            print(f"\n❌ A letra {cor.vermelho}{letra}{cor.padrao} não está na palavra!")
            erros-=1

        letras_chutadas.append(letra)
    else:
        adivinha_palavra(str(input("\nSeus chutes acabaram! Tente adivinhar a palavra completa: ")))

def status_palavra():
    global fim_de_jogo
    status = " ".join(
        [letra if letra in letras_chutadas
         else "_"
         for letra in palavra_secreta]
    )
    print(f"\n{cor.negativo}  {status}  {cor.padrao}\n")

    if all(letra in letras_chutadas for letra in palavra_secreta):
        print(f"\n🎉 Você completou a palavra!")
        fim_de_jogo = True

def adivinha_palavra(palavra: str):
    global fim_de_jogo
    palavra = palavra.upper()

    if palavra_secreta == palavra:
        print(f"\n✅ Você acertou! A palavra é {palavra}!")

    else:
        print(f"\n❌ Você errou... A palavra era {palavra_secreta}!")

    fim_de_jogo = True