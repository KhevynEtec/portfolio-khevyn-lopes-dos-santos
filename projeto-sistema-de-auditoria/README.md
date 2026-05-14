# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de Programação de Computadores  do curso de Ciência da computação. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.
 
### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/KhevynEtec/portfolio-khevyn-lopes-dos-santos/tree/main/projeto_sistema_de_auditoria
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o script principal:
   ```bash
   python sistema_de_auditoria_.py
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
* A arquitetura do sistema foi pensada para separar a lógica de negócio (o cálculo financeiro) da lógica de monitoramento (a auditoria).
* Para isso, utilizei um Decorator que envolve a função principal, capturando automaticamente os metadados da execução, como o tempo gasto e os argumentos fornecidos, sem poluir o código de soma.

A construção do cálculo baseia-se em uma função recursiva que atua como um verificador de dados: ela verifica cada chave do dicionário corporativo; 
se o valor for outro dicionário, a função chama a si mesma para mergulhar um nível abaixo; se for um número, ela o soma ao subtotal. 
Essa abordagem permite que o sistema processe empresas com infinitos níveis de sub-departamentos sem necessidade de loops manuais complexos.

* **Dados:** Os dados simulados da empresa foram estruturados em um dicionário aninhado de múltiplos níveis. A estrutura raiz contém chaves como "Matriz" e "Empresa_SP", que se ramificam em setores (ex: TI, RH) e subsetores (ex: Infraestrutura, Desenvolvimento), culminando em valores numéricos que representam os custos operacionais de cada unidade.
 
## 👤 Autor
 
* **Khevyn Lopes dos Santos** * LinkedIn: https://br.linkedin.com/in/khevynlopesdossantos
* E-mail: khevyn.lopes@gmail.com
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*

[Voltar ao início](https://github.com/KhevynEtec/portfolio-khevyn-lopes-dos-santos)
