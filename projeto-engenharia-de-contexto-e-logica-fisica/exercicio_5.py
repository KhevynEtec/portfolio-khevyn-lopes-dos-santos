# Exercicio 01

def analisar_dados():



  dados_locais = [

    ["Parque Linear", [25, 70, 35]],

    ["Parque Linear", [28, 60, 40]],

    ["Av. Mateo Bei", [27, 60, 65]],

    ["Av. Mateo Bei", [31, 50, 80]],

    ["UNICID", [26, 65, 55]],

    ["UNICID", [30, 55, 70]]

  ]


# 1º for
  for local in dados_locais:

    nome = local[0]

    metricas = local[1]



    print("\nLocal:", nome)



    nomes_metricas = ["Temperatura", "Umidade", "IQA"]



    # 2º for (aninhado)

    for i in range(len(metricas)):

      if nomes_metricas[i] == "Temperatura":

        print(nomes_metricas[i] + ":", metricas[i], "°C")

      elif nomes_metricas[i] == "Umidade":

        print(nomes_metricas[i] + ":", metricas[i], "%")

      else:

        print(nomes_metricas[i] + ":", metricas[i])



    temperatura = metricas[0]

    umidade = metricas[1]

    iqa = metricas[2]



    # classificação do IQA

    match iqa:

      case iqa if iqa <= 40:

        qualidade = "Boa"

      case iqa if iqa <= 80:

        qualidade = "Moderada"

      case iqa if iqa <= 120:

        qualidade = "Ruim"

      case _:

        qualidade = "Muito Ruim"



    # cálculo do conforto

    conforto = 10



    if temperatura > 30:

      conforto -= 2



    if umidade < 60:

      conforto -= 2



    if iqa > 80:

      conforto -= 2

    elif iqa > 40:

      conforto -= 1



    print("Qualidade do ar:", qualidade)

    print("Conforto:", conforto)





analisar_dados()

# Lista

locais = [

  "Porta da casa",

  "Escada estreita",

  "Segunda porta",

  "Corredor com plantas",

  "Escada",

  "Corredor com carros",

  "Portão (saída)"

]



estados = [

  "fechada",

  "estreita_com_corrimao",

  "destrancada",

  "livre_com_obstaculos",

  "escada",

  "apertado",

  "portao_trancado"

]



energia = 10

posicao = 0

tem_chave = True



while energia > 0:

  print("\nVocê está em:", locais[posicao])

  estado = estados[posicao]



  # Pra conseguir sair

  if estado == "portao_trancado":

    print("Você chegou ao portão!")



    if tem_chave:

      print("Usando a chave para abrir o portão...")

      print("Você conseguiu sair com segurança!")

      break

    else:

      print("O portão está trancado e você não tem a chave!")

      posicao -= 1



  # análise do ambiente

  elif estado == "fechada":

    print("Abrindo a porta...")

    posicao += 1



  elif estado == "estreita_com_corrimao":

    print("Descendo com cuidado pela escada...")

    posicao += 1



  elif estado == "destrancada":

    print("A porta está destrancada, passando...")

    posicao += 1



  elif estado == "livre_com_obstaculos":

    print("Desviando dos vasos...")

    posicao += 1



  elif estado == "escada":

    print("Descendo mais uma escada...")

    posicao += 1



  elif estado == "apertado":

    print("Passando com dificuldade entre os carros...")

    posicao += 1



  # perda de energia

  energia -= 1

  print("Energia restante:", energia)



# caso acabe energia

if energia == 0:

  print("Você ficou sem energia e não conseguiu sair.")
