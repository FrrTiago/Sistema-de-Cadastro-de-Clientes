from cliente import Cliente

class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"\nCliente {cliente.nome} adicionado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
        else:
            print("\nLista de Clientes:")
            for cliente in self.clientes:
                print(cliente)

    def buscar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome.lower():
                print("\nCliente encontrado:")
                print(cliente)
                return
        print("\nCliente não encontrado.")