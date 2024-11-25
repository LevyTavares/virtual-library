# Eu fiquei meio na dúvida se era pra ter uma interatividade ou não
# Então peguei as classes que são o principal e fui indo atrás de aprender como fazer uma interatividade
# Saindo isso:

from abc import ABC, abstractmethod

# Classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Subclasse UsuarioComum
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, numeroMatricula):
        super().__init__(nome, idade)
        self.numeroMatricula = numeroMatricula
        self.livrosEmprestados = []

    def realizarEmprestimo(self, livro):
        if len(self.livrosEmprestados) < 3 and livro.statusDisponibilidade:
            self.livrosEmprestados.append(livro)
            livro.statusDisponibilidade = False
            print(f"Empréstimo realizado: {livro.titulo} por {self.nome}")
        else:
            print("Não foi possível realizar o empréstimo.")

    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            self.livrosEmprestados.remove(livro)
            livro.statusDisponibilidade = True
            print(f"Devolução realizada: {livro.titulo}")
        else:
            print("Livro não encontrado nos empréstimos do usuário.")

# Subclasse Administrador
class Administrador(Pessoa):
    def cadastrarLivro(self, livros, titulo, autor, anoPublicacao):
        novo_livro = Livro(titulo, autor, anoPublicacao)
        livros.append(novo_livro)
        print(f"Livro cadastrado: {titulo}")

    def exibirRelatorios(self, livros, usuarios):
        print("\nRelatório de Livros Disponíveis:")
        for livro in livros:
            if livro.statusDisponibilidade:
                print(f" - {livro.titulo} por {livro.autor}")
        
        print("\nRelatório de Usuários com Livros Emprestados:")
        for usuario in usuarios:
            if usuario.livrosEmprestados:
                print(f" - {usuario.nome} ({usuario.numeroMatricula}) tem:")
                for livro in usuario.livrosEmprestados:
                    print(f"    * {livro.titulo}")

# Classe abstrata ItemBiblioteca
class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, anoPublicacao, statusDisponibilidade=True):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.statusDisponibilidade = statusDisponibilidade

# Subclasse Livro
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, anoPublicacao, statusDisponibilidade=True):
        super().__init__(titulo, autor, anoPublicacao, statusDisponibilidade)

# Função principal com menu
def menu():
    livros = []
    usuarios = []
    administrador = Administrador("Admin", 30)  # Administrador padrão

    while True:
        print("\n--- Biblioteca Virtual ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Realizar Empréstimo")
        print("4. Devolver Livro")
        print("5. Relatórios")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # Cadastrar Livro
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            ano = int(input("Ano de Publicação: "))
            administrador.cadastrarLivro(livros, titulo, autor, ano)

        elif opcao == "2":  # Cadastrar Usuário
            nome = input("Nome do Usuário: ")
            idade = int(input("Idade do Usuário: "))
            matricula = input("Número de Matrícula: ")
            novo_usuario = UsuarioComum(nome, idade, matricula)
            usuarios.append(novo_usuario)
            print(f"Usuário cadastrado: {nome}")

        elif opcao == "3":  # Realizar Empréstimo
            matricula = input("Matrícula do Usuário: ")
            usuario = next((u for u in usuarios if u.numeroMatricula == matricula), None)
            if usuario:
                print("Livros Disponíveis:")
                livros_disponiveis = [livro for livro in livros if livro.statusDisponibilidade]
                for idx, livro in enumerate(livros_disponiveis):
                    print(f"{idx + 1}. {livro.titulo} por {livro.autor}")
                if livros_disponiveis:
                    escolha = int(input("Escolha o número do livro: ")) - 1
                    if 0 <= escolha < len(livros_disponiveis):
                        usuario.realizarEmprestimo(livros_disponiveis[escolha])
                    else:
                        print("Escolha inválida.")
                else:
                    print("Nenhum livro disponível.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":  # Devolver Livro
            matricula = input("Matrícula do Usuário: ")
            usuario = next((u for u in usuarios if u.numeroMatricula == matricula), None)
            if usuario:
                if usuario.livrosEmprestados:
                    print("Livros Emprestados:")
                    for idx, livro in enumerate(usuario.livrosEmprestados):
                        print(f"{idx + 1}. {livro.titulo} por {livro.autor}")
                    escolha = int(input("Escolha o número do livro para devolver: ")) - 1
                    if 0 <= escolha < len(usuario.livrosEmprestados):
                        usuario.devolverLivro(usuario.livrosEmprestados[escolha])
                    else:
                        print("Escolha inválida.")
                else:
                    print("Nenhum livro emprestado.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":  # Relatórios
            administrador.exibirRelatorios(livros, usuarios)

        elif opcao == "6":  # Sair
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()


# Assim fica melhor
