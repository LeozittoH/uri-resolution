codepeca1, pecas1, valor1 = list(map(float, input().split(" ")))
codepeca2, pecas2, valor2 = list(map(float, input().split(" ")))

produto1 = pecas1 * valor1
produto2 = pecas2 * valor2

valor = produto1 + produto2

print("VALOR A PAGAR: R$ %.2f" %valor)
