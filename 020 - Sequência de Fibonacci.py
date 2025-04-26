def fibonacci(limite):
    sequencia = [0, 1]  # Os dois primeiros números da sequência
    while True:
        proximo = sequencia[-1] + sequencia[-2]  # Soma dos dois últimos números
        if proximo > limite:
            break  # Para quando o próximo número ultrapassar o limite
        sequencia.append(proximo)  # Adiciona o próximo número à sequência
    return sequencia

# Exemplo de uso
limite = 50
print(fibonacci(limite))