from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self._cargo = cargo

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Cargo: {self._cargo}"