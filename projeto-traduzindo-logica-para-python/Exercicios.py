# EX4 - Traduzindo Lógica para Python
# 1. Função: processar_vendas

def processar_vendas():
 total_compra = 0.0
 itens_comprados = 0

 print ("Quantos produtos diferentes foram comprados?")
 quantidade_tipos = int(input("Quantos produto diferentes foram comprados"))

 for i in range(1, quantidade_tipos + 1):
  nome = str(input("Nome do produto: "))
  preco = float(input("Preço unitário: "))
  qtd = int(input("Quantidade deste produto: "))

  if preco <= 0 or qtd <= 0:
    print(f"Erro: Valores inválidos para {nome}")
  else:
    subtotal = preco * qtd
    total_compra = total_compra + subtotal
    itens_comprados = itens_comprados + qtd

 if total_compra > 500.00:
   total_final = total_compra * 0.90

   print("Desconto de 10% aplicado!")
 elif total_compra > 200.00:
  total_final = total_compra * 0.95
 else:
  total_final = total_compra

 print (f"Resumo: {itens_comprados} itens. Total a pagar: R$ {total_final:.2f}")

#2. Função: analisar_clima

def analisar_clima():

 soma_temperaturas = 0.0
 dias_quentes = 0
 alerta_extremo = False

 for dia in range(1, 8):

  temp = float(input("Digite a temperatura do dia "))
  soma_temperaturas = soma_temperaturas + temp

  if temp > 35.0:
   dias_quentes = dias_quentes + 1

  if temp > 45.0 or temp < -5.0:
   alerta_extremo = True

 media = soma_temperaturas / 7

 print(f"Média semanal: {media}")

 print(f"Dias acima de 35°C: {dias_quentes}")

 if alerta_extremo == True:
  print("CUIDADO: Condições climáticas perigosas detectadas!")
 else:
  print("Clima dentro da normalidade operacional.")

# 3. Função: sistema_notas_turma

def sistema_notas_turma():

 print("Quantos alunos existem na turma?")
 total_alunos = int(input())

 for j in range(1, total_alunos + 1):
  print("Nome do aluno:")
  aluno_nome = str(input())
  print("Nota 1:")

  n1 = float(input())
  print("Nota 2:")

  n2 = float(input())

  media_aluno = (n1 + n2) / 2

  if media_aluno >= 7.0:
   print(f"{aluno_nome}: Aprovado com média {media_aluno}")
  elif media_aluno >= 5.0:
   print(f"{aluno_nome}: Recuperação (Média: {media_aluno})")
  else:
   print(f"{aluno_nome}: Reprovado")

# 4. Função: simulador_poupanca

def simulador_poupanca():

 print("Valor inicial do investimento:")
 saldo = float(input())

 print("Taxa de juros mensal (em %):")
 taxa = float(input())

 print("Número de meses da simulação:")
 meses = int(input())

 for m in range(1, meses + 1):
  print("Quanto deseja depositar no mês ", m, "? (0 para nenhum)")
  aporte = float(input())

  saldo = saldo + aporte
  juros = saldo * (taxa / 100)
  saldo = saldo + juros

  print("Mês ", m, ": Saldo atualizado = R$", saldo)

  if saldo > 10000.0:
   print("Parabéns! Você atingiu a meta de 10k no mês ", m)

 print("Resultado final após ", meses, " meses: R$", saldo)
