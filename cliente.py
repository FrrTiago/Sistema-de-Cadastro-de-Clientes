from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"