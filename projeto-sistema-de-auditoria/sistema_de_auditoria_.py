import time

#exemplo professor
empresa_data = {
    "Matriz": {
        "TI": {
            "Infraestrutura": {
                "Servidores": 50000,
                "Seguranca": 30000
            },
            "Desenvolvimento": {
                "Frontend": 20000,
                "Backend": 25000,
                "DevOps": 15000
            }
        },

        "RH": {
            "Recrutamento": 10000,
            "Treinamento": 12000,
            "Cultura": {
                "Eventos": 5000,
                "Brindes": 2000
            }
        },

        "Financeiro": 40000,


        "Marketing": {
            "Publicidade": 18000,
            "Design": 9000
        }
    },

    "Empresa_SP": {
        "Comercial": {
            "Vendas": 35000,
            "Parcerias": 12000
        },

        "Atendimento_Cliente": {
            "Atendimento": 8000,
        }
    }
}



def auditor(func):

    def wrapper(*args, **kwargs):

        print("===== INICIANDO AUDITORIA =====")

        inicio = time.time()

        print(f"Nomes no dicionario: {args}")
        print(f"Parâmetros utilizados: {kwargs}")

        resultado = func(*args, **kwargs)

        fim = time.time()

        print(f"Tempo de execução: {fim - inicio:.6f} segundos")
        print("--- FIM DA AUDITORIA ---")

        return resultado

    return wrapper



@auditor
def calcular_orcamento(estrutura, *departamentos_ignorados, **kwargs):

    total = 0

    taxa_cambio = kwargs.get("taxa_cambio", 1)
    moeda_destino = kwargs.get("moeda_destino", "BRL")

    def somar(dados):

        subtotal = 0

        for chave, valor in dados.items():


            if chave in departamentos_ignorados:
                print(f"Departamento ignorado: {chave}")
                continue


            if isinstance(valor, dict):
                subtotal += somar(valor)


            elif isinstance(valor, (int, float)):
                subtotal += valor

        return subtotal

    total = somar(estrutura)

    total_convertido = total * taxa_cambio

    print(f"\nMoeda destino: {moeda_destino}")
    print(f"Taxa de câmbio aplicada: {taxa_cambio}")

    return total_convertido


resultado = calcular_orcamento(
    empresa_data,
    "RH",
    moeda_destino="BRL",
    taxa_cambio=1
)

print(f"\nOrçamento total calculado: R$ {resultado:.2f}")
