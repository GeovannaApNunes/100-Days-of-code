def sao_anagramas(str1, str2): # Função que recebe duas strings e verifica se são anagramas
    return sorted(str1) == sorted(str2)

# Exemplo de uso:
print(sao_anagramas("amor", "roma"))  
print(sao_anagramas("python", "typhon")) 
print(sao_anagramas("teste", "texto"))  