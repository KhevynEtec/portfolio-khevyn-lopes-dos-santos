# 🛡️ Sistema de Auditoria de Vendas

## 📝 Descrição do Projeto
Este projeto consiste em um script de auditoria de segurança focado na análise de transações de vendas. O objetivo principal é monitorar entradas financeiras e sinalizar valores atípicos que possam indicar erros de digitação ou fraudes, colocando o sistema em estado de quarentena preventivo.

Desenvolvido como um notebook interativo, o algoritmo processa três entradas de vendas simultâneas, calculando sua média e comparando os resultados contra um limite de segurança pré-definido. Caso a média geral ou alguma venda individual ultrapasse o teto permitido, o sistema solicita uma revisão manual ao usuário, permitindo o reajuste dinâmico do limite para operações futuras.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Ambiente:** Jupyter Notebook, Google Colab
* **Conceitos:** Escopo de Variáveis (Global), Estruturas de Decisão Condicional e Tipagem Dinâmica

## 📊 Funcionalidades e Aprendizados
O projeto implementa uma lógica simples e eficaz de controle de risco para ambientes transacionais.
* **Sistema de Quarentena:** Validação automática que alerta "SISTEMA EM QUARENTENA" se a média das vendas atingir ou superar o limite de segurança inicial de 10.000.00.
* **Revisão Manual e Escalonamento:** Caso uma venda isolada ultrapasse o teto, o sistema aguarda a confirmação humana de legitimidade (s/n). Se a venda for confirmada como legítima ("s"), o limite de segurança da aplicação é multiplicado por 10.
* **Análise de Tipagem:** O código inspeciona e imprime os tipos de dados ao final da execução, confirmando o tratamento dos valores transacionais e da média como `<class 'float'>`.
* 
## 🔧 Como Executar 
1. Certifique-se de ter o Python instalado em sua máquina.
2. 2. Clone este repositório:
bash
   git clone [https://github.com/KhevynEtec/traduzindo-logica-para-python.git](https://github.com/KhevynEtec/atividade-logica-python.git)
[Voltar ao início](https://github.com/KhevynEtec/portfolio-khevyn-lopes-dos-santos)
