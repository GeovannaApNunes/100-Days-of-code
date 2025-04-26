def palavra_mais_longa(frase):
    palavras = frase.split()  # Divide a frase em palavras
    return max(palavras, key=len)  # Retorna a palavra mais longa

# Exemplo de uso
frase = "Desenvolver em Python é muito divertido"
print(palavra_mais_longa(frase))