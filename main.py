from cliente import Cliente
from sistema_cadastro import SistemaCadastro

def menu():
    sistema = SistemaCadastro()

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            cliente = Cliente(nome, email)
            sistema.adicionar_cliente(cliente)

        elif opcao == '2':
            sistema.listar_clientes()

        elif opcao == '3':
            nome = input("Digite o nome do cliente para buscar: ")
            sistema.buscar_cliente(nome)

        elif opcao == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()