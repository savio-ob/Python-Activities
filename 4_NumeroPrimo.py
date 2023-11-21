def eh_primo(numero):
    return numero > 1 and all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))

primos = [num for num in range(1, 101) if eh_primo(num)]
print("Números primos de 1 a 100:", primos)
