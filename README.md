# Sistema de Cadastro de Clientes

Este é um sistema simples de cadastro de clientes desenvolvido em **Python**, utilizando o paradigma de **Programação Orientada a Objetos (POO)**. O sistema permite:

✅ Cadastrar novos clientes  
✅ Listar todos os clientes cadastrados  
✅ Buscar clientes pelo nome  

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Paradigma: Programação Orientada a Objetos (POO)

---

## 🚀 Como Executar o Projeto

1. Clone ou baixe este repositório:

```bash
git clone https://github.com/seu-usuario/sistema-cadastro-clientes.git
```

2. Acesse a pasta do projeto:

```bash
cd sistema-cadastro-clientes
```

3. Execute o arquivo `main.py`:

```bash
python main.py
```

---

## 📁 Estrutura do Projeto

```
sistema_cadastro/
│
├── main.py                        # Interface do menu principal
│
├── pessoa.py                     # Classe abstrata Pessoa (abstração)
├── cliente.py                    # Classe Cliente que herda de Pessoa
├── funcionario.py                # Classe Funcionario que herda de Pessoa
│
├── sistema_cadastro.py           # SistemaCadastro manipula objetos Pessoa (polimorfismo)
```

---

## ✨ Funcionalidades

- **Cadastrar Cliente**: inserção de nome e email.
- **Listar Clientes**: exibe todos os clientes cadastrados.
- **Buscar Cliente**: pesquisa por nome (não diferencia maiúsculas/minúsculas).
- **Sair**: encerra o sistema.

---

## 👥 Desenvolvedores

- **Tiago Ferreira da Silva**  
  [GitHub: Tiago Ferreira da Silva](https://github.com/FrrTiago)

- **Renato Xavier Portela Giordano**  
  [GitHub: Renato Xavier Portela Giordano](https://github.com/aluno-renato)

---

## 💡 Observações

- Este projeto é um exemplo didático para demonstrar a aplicação do paradigma de Programação Orientada a Objetos.
- Futuras melhorias podem incluir:  
  ➡️ Armazenamento dos dados em arquivos ou bancos de dados  
  ➡️ Funcionalidades de edição e remoção de clientes  
  ➡️ Interface gráfica (GUI)

---

## 🤝 Contribuições

Sinta-se à vontade para contribuir! Basta fazer um **fork** do projeto e enviar um **pull request** com suas melhorias ou correções.
