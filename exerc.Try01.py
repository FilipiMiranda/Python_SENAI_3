try:
    num = int(input("Digite um numero: "))
    resultado = 30 / num
    print(resultado)

except:
    print("Digite um numero inteiro!!!")
else:
    print("Nenhuma ocorrencia encontrada!")
finally:
    print("Fim")