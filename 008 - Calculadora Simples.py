num1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operador == '+':
    print("Resultado:", num1 + num2)
elif operador == '-':
    print("Resultado:", num1 - num2)
elif operador == '*':
    print("Resultado:", num1 * num2)
elif operador == '/':
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: Divisão por zero!")
else:
    print("Operador inválido!")