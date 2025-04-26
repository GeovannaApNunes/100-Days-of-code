def contar_vogais(texto): # Função que conta as vogais
    vogais = "aeiouAEIOU" 
    return sum(1 for letra in texto if letra in vogais) # Conta as vogais

# diditar a frase e saida do número de vogais
texto = input("Digite uma frase: ")
print("Número de vogais:", contar_vogais(texto)) # Exibe o número de vogais