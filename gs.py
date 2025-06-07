# Luiz Fernando Balbino RM:566222
# Pedro Rodrigues Almeida RM:564711
# Gabriel Inague RM:561985

def verifica_risco_enchente(x):
    nivel = 0.25 * x + 0.25

    if nivel > 2:
        return f"Risco de enchente! Nível do rio: {nivel:.2f}m"
    else:
        return f"Sem risco de enchente. Nível do rio: {nivel:.2f}m"

while True:
    entrada = input("Informe um dia de 1 a 10 para saber se há risco de enchente: ")
    try:
        dias = int(entrada)
        resultado = verifica_risco_enchente(dias)
        print(resultado)
        break 
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
