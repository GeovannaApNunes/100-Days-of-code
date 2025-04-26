# crud_app.py

# Lista que simula um banco de dados
usuarios = []

# Função para criar um novo usuário
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    usuario = {"id": len(usuarios) + 1, "nome": nome, "email": email}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")

# Função para listar todos os usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, E-mail: {usuario['email']}")

# Função para atualizar um usuário existente
def atualizar_usuario():
    id_usuario = int(input("Digite o ID do usuário que deseja atualizar: "))
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario["nome"] = input("Digite o novo nome: ")
            usuario["email"] = input("Digite o novo e-mail: ")
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado.")

# Função para excluir um usuário
def excluir_usuario():
    id_usuario = int(input("Digite o ID do usuário que deseja excluir: "))
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuarios.remove(usuario)
            print("Usuário excluído com sucesso!")
            return
    print("Usuário não encontrado.")

# Menu principal
def menu():
    while True:
        print("\n=== MENU CRUD ===")
        print("1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()
