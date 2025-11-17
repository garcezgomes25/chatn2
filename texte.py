
print("🎲 Jogo de Adivinhação 🎲")
numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    palpite = int(input("Tente adivinhar o número (1 a 10): "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"🎉 Acertou! O número era {numero_secreto}. Você conseguiu em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("🔼 O número é maior!")
    else:
        print("🔽 O número é menor!")



