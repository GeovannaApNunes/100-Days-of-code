def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Solicitando a entrada do usuário
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")