m = float(input("Informe o numero (M): "))
n = float(input("Informe o numero (N): "))

produto = m * n

if produto < 0:
    print("O Produto é numero Negativo")
elif produto > 0:
    print("O Produto é numero Positivo")
else:
    print("O Produto é Zero")

