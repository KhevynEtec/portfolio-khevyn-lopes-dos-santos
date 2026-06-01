# 🛡️ Sistema de Monitoramento de Vendas e Segurança

## 📝 Descrição do Projeto
Este projeto consiste em uma ferramenta de análise e validação de transações financeiras desenvolvida em Python. O objetivo principal é automatizar o cálculo de médias de vendas e implementar camadas de segurança para identificar anomalias ou valores atípicos que necessitem de intervenção humana (Revisão Manual).

O sistema processa entradas de vendas, calcula métricas básicas e utiliza um **Limite de Segurança** dinâmico para decidir se uma operação deve ser aprovada automaticamente ou enviada para quarentena. É uma solução voltada para integridade de dados e prevenção de erros operacionais em fluxos de vendas.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Conceitos:** Funções, Estruturas Condicionais (if/else), Manipulação de Variáveis Globais e Tipagem de Dados.
* **Ambiente:** Terminal / CLI (Command Line Interface).

## 📊 Funcionalidades e Regras de Negócio
O sistema opera baseado em fluxos lógicos de validação:
* **Cálculo de Média:** Processa o valor de múltiplas vendas para estabelecer um parâmetro de comparação.
* **Detecção de Anomalias:** Identifica se alguma venda individual excede drasticamente a média (5x superior), disparando um alerta de **Revisão Manual**.
* **Gestão de Limites:** Permite que um operador ajuste o `LIMITE_SEGURANCA` em tempo real, validando se o novo valor é compatível com a média atual.
* **Sistema de Quarentena:** Bloqueia operações onde a média calculada ultrapassa o teto de segurança estabelecido.

## 🔧 Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Execute o script principal:
   ```bash
   python main.py
   
---
## 👤 Autor
 
* **Khevyn Lopes dos Santos** * LinkedIn: https://br.linkedin.com/in/khevynlopesdossantos
* E-mail: khevyn.lopes@gmail.com
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
---
[Voltar ao início](https://github.com/KhevynEtec/portfolio-khevyn-lopes-dos-santos)
