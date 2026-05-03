# 💸 Sistema de Caixa e Troco Inteligente

## 📝 Descrição do Projeto
Este projeto consiste em um simulador de sistema de PDV (Ponto de Venda) focado na lógica de **caixa e cálculo de troco**. O objetivo principal é automatizar o processo de conferência de pagamentos e a devolução otimizada de valores ao cliente, garantindo que o troco seja entregue com o **menor número possível de cédulas**.

O diferencial deste desenvolvimento é a aplicação de conceitos de **modularização**, onde o sistema é dividido em responsabilidades isoladas para facilitar a manutenção e a escalabilidade do código. O algoritmo processa a entrada do valor de compra e o valor pago, valida a viabilidade da transação e executa a decomposição matemática para as denominações sugeridas (100, 50, 10, 5 e 1).

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Conceitos Aplicados:** Lógica de Programação, Modularização de Funções, Estruturas Condicionais e Operadores Aritméticos (Divisão Inteira e Resto).
* **Ferramentas:** VS Code / Ambiente de desenvolvimento local.

## 🏗️ Arquitetura do Sistema (Modularização)
Para evitar um bloco de código único e complexo, o sistema foi estruturado seguindo uma interface de responsabilidades bem definidas:

* **`validar_pagamento()`**: Verifica se o valor entregue pelo cliente é suficiente para cobrir o total da compra.
* **`calcular_troco()`**: Realiza a subtração bruta entre o valor pago e o total da compra para encontrar a diferença matemática.
* **`decompor_notas()`**: Processa a divisão e os restos para cada denominação de nota, garantindo a eficiência na entrega do troco.

## 📊 Exemplo de Fluxo
Ao processar uma compra de **R$ 57,00** com um pagamento de **R$ 100,00**:
1. O sistema valida que o pagamento é superior ao total.
2. Calcula o troco bruto de **R$ 43,00**.
3. Decompõe o valor para retornar o menor número de notas possível.

## 🔧 Como Executar
1. Clone o repositório.
2. Certifique-se de ter o Python instalado.
3. Execute o comando: `python main.py`.

---
[Voltar ao início](https://github.com/KhevynEtec/portfolio-khevyn-lopes-dos-santos)
