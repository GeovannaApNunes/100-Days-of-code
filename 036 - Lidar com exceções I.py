try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    
    resultado = numerador / denominador
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Digite apenas números válidos.")