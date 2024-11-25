# Bem-vindo ao meu código
# Aluno: Isaías Levi Tavares da Silva, 37023010

from abc import ABC, abstractmethod

# Classe base Pessoa(Abstrata)
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def exibir_informacoes(self):
        pass

# Subclasse UsuarioComum
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"Livro '{livro.titulo}' emprestado com sucesso para {self.nome}.")
        else:
            print(f"Não foi possível emprestar o livro '{livro.titulo}'.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"Livro '{livro.titulo}' devolvido com sucesso por {self.nome}.")
        else:
            print(f"O livro '{livro.titulo}' não está emprestado por {self.nome}.")

    def exibir_informacoes(self):
        print(f"Usuário: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

# Subclasse Administrador
class Administrador(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def cadastrar_livro(self, biblioteca, livro):
        biblioteca.adicionar_livro(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso.")

    def exibir_informacoes(self):
        print(f"Administrador: {self.nome}, Idade: {self.idade}")

# Classe base ItemBiblioteca
class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    @abstractmethod
    def exibir_detalhes(self):
        pass

# Subclasse Livro
class Livro(ItemBiblioteca):
    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Status: {status}")

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        print("\nLivros disponíveis:")
        for livro in self.livros:
            if livro.disponivel:
                livro.exibir_detalhes()

    def listar_usuarios_com_emprestimos(self):
        print("\nUsuários com livros emprestados:")
        for usuario in self.usuarios:
            if usuario.livros_emprestados:
                print(f"\n{usuario.nome} possui os seguintes livros emprestados:")
                for livro in usuario.livros_emprestados:
                    print(f"- {livro.titulo}")

# Demonstração de uso
if __name__ == "__main__":
    # Criando a biblioteca
    biblioteca = Biblioteca()

    # Criando administrador
    admin = Administrador("João", 35)

    # Criando livros
    livro1 = Livro("Python Básico", "Autor A", 2021)
    livro2 = Livro("POO Avançado", "Autor B", 2020)
    livro3 = Livro("Estruturas de Dados", "Autor C", 2019)

    # Administrador cadastra livros
    admin.cadastrar_livro(biblioteca, livro1)
    admin.cadastrar_livro(biblioteca, livro2)
    admin.cadastrar_livro(biblioteca, livro3)

    # Criando usuários
    usuario1 = UsuarioComum("Maria", 22, "2022001")
    usuario2 = UsuarioComum("Pedro", 25, "2022002")

    # Cadastrando usuários na biblioteca
    biblioteca.cadastrar_usuario(usuario1)
    biblioteca.cadastrar_usuario(usuario2)

    # Operações de empréstimos
    usuario1.emprestar_livro(livro1)
    usuario1.emprestar_livro(livro2)

    # Listando relatórios
    biblioteca.listar_livros_disponiveis()
    biblioteca.listar_usuarios_com_emprestimos()

    # Devolvendo livro
    usuario1.devolver_livro(livro1)

    # Atualizando relatórios
    biblioteca.listar_livros_disponiveis()
    biblioteca.listar_usuarios_com_emprestimos()


