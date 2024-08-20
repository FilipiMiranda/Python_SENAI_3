fatura = 0

print("\n=== Central de Fotocopias ===")
print("1 - R$ 0,25 pelas primeiras 10 fotocópias")
print("2 - R$ 0,20 pelas próximas vinte")
print("3 - R$ 0,10 pelas mais de vinte")

fotocopias = int(input("Informe a quantidade de fotocopias que voce deseja: "))

if fotocopias <= 10:
   fatura=0.25 * fotocopias
   print (f"Valor da fatura é {fatura}")
if fotocopias > 10 and fotocopias < 20:
    fatura= 10 * 0.25 + (fotocopias - 10) * 0.20
    print (f"Valor da fatura é {fatura}")
    
if fotocopias > 20:
    fatura= (10 * 0.25) + (10 * 0.20) + (fotocopias - 20) * 0.10
    print (f"Valor da fatura é {fatura}")