def palindromo(texto):
    texto = texto.lower().replace(" ", "")  # Convertendo para minúsculas e removendo espaços
    return texto == texto[::-1]

# Exemplo de uso
entrada = input("Digite uma palavra ou frase: ")
if palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")