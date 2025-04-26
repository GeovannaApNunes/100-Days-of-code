import json

# Função para coletar informações da pessoa
def coletar_dados():
    dados_pessoais = {
        "Nome": input("Nome: "),
        "Idade": input("Idade: "),
        "Escolaridade": input("Escolaridade: ")
    }
    
    dados_profissionais = {
        "Profissão": input("Profissão: "),
        "Empresa": input("Empresa (se não tiver, deixe em branco): "),
        "Experiência": input("Anos de experiência: ")
    }
    
    dados_contato = {
        "E-mail": input("E-mail: "),
        "Telefone": input("Telefone: "),
        "Cidade": input("Cidade: ")
    }

    # Mesclando todos os dicionários em um só
    dados_completos = {**dados_pessoais, **dados_profissionais, **dados_contato}
    
    return dados_completos

# Coletando os dados
dados_final = coletar_dados()

# Exibindo os dados formatados
print("\nDados coletados:")
print(json.dumps(dados_final, indent=4, ensure_ascii=False))