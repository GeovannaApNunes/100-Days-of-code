def contar_frequencia_palavras(frase):
    palavras = frase.lower().split()  # Converte para minúsculas e divide a frase em palavras
    frequencia = {}

    for palavra in palavras:
        palavra = palavra.strip(".,!?()[]{}\"'")  # Remove pontuações ao redor das palavras
        if palavra:
            frequencia[palavra] = frequencia.get(palavra, 0) + 1  # Incrementa a contagem

    return frequencia

# Exemplo de uso:
frase = "Olá, mundo! Olá, Python. Python é incrível, incrível!"
print(contar_frequencia_palavras(frase))