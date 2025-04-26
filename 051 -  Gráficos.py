import matplotlib.pyplot as plt

def criar_grafico_pizza():
 
    # Dados para o gráfico de pizza
    categorias = ['Python', 'Java', 'JavaScript', 'C++', 'C#']
    valores = [35, 25, 20, 10, 10]
    cores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    explode = (0.1, 0, 0, 0, 0)  # Destaca a primeira fatia
    
    # Criando o gráfico de pizza
    plt.figure(figsize=(10, 7))
    plt.pie(valores, explode=explode, labels=categorias, colors=cores, 
            autopct='%1.1f%%', shadow=True, startangle=90)
    
    # Adicionando título
    plt.title('Linguagens de Programação Mais Populares', fontsize=15)
    
    # Garantindo que o gráfico seja um círculo
    plt.axis('equal')
    
    # Exibindo o gráfico
    plt.show()

if __name__ == "__main__":
    # Criando e exibindo um gráfico de pizza
    print("Criando gráfico de pizza...")
    criar_grafico_pizza()
