from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, email):
        self._nome = nome  # Encapsulamento com underline
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @abstractmethod
    def __str__(self):
        pass