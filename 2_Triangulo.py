l1, l2, l3 = sorted(map(int, input("Digite os comprimentos dos lados do triângulo separados por espaço: ").split()))
s = (l1 + l2 + l3) / 2
a = (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5 if l1 + l2 > l3 else None
print(f"{'Parabéns!' if a else 'Desculpe'}, {'Os comprimentos formam um triângulo e a área é: {:.2f}'.format(a) if a else f'os comprimentos {l1}, {l2} e {l3} não formam um triângulo.'}")
