LIMITE_SEGURANCA = 10000

venda1 = float(input("Valor de venda 01: "))
venda2 = float(input("Valor de venda 02: "))
venda3 = float(input("Valor de venda 03: "))

def analisar_vendas(venda1, venda2, venda3):
    global LIMITE_SEGURANCA

media = (venda1 + venda2 + venda3) / 3


print("-"*40)
print(f"Venda1: {venda1} ")
print(f"Venda2: {venda2} ")
print(f"Venda3: {venda3} ")
print(f"Média vendas: R$ {media:.2f}")
print("-"*40)

# Observação: pela minha linha raciocionio a venda nunca vai conseguir superar a (media * 5), ou seja pra esse código realmente funcionar deveria colocar "if (venda1/2/3 > LIMITE_SEGURANCA * 5)"
if (venda1 > media * 5) or (venda2 > media * 5) or (venda3 > media * 5):
    print("REVISÃO MANUAL")

    resposta = input("Essa venda é legítima? (s/n): ")

    if resposta.lower() == "s": #teste letra minuscula
        LimiteAltera = float(input("Digite um novo limite: "))

        if LimiteAltera < media:
            print("Limite inválido!")
        else:
            LIMITE_SEGURANCA = LimiteAltera
            print(f"Novo limite definido: {LIMITE_SEGURANCA}")

print("-"*40)
if media > LIMITE_SEGURANCA:
  print("SISTEMA EM QUARENTENA")
else:
  print("VALOR APROVADO")
print("-"*40)

print(f"Venda 1: {venda1} -> {type(venda1)}")
print(f"Venda 2: {venda2} -> {type(venda2)}")
print(f"Venda 3: {venda3} -> {type(venda3)}")
print(f"Média: {media} -> {type(media)}")
print(f"Limite: {LIMITE_SEGURANCA} -> {type(LIMITE_SEGURANCA)}")

analisar_vendas(venda1, venda2, venda3)
