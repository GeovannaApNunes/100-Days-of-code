class Livro:
    def __init__(self, titulo, autor, descricao):
        self.titulo = titulo
        self.autor = autor
        self.descricao = descricao

    def exibir_info(self):
        """Exibe as informações do livro"""
        return f"Título: {self.titulo}\nAutor: {self.autor}\nDescrição: {self.descricao}"


# Criando um objeto Livro para "Jogos Vorazes"
livro = Livro(
    titulo="Jogos Vorazes",
    autor="Suzanne Collins",
    descricao="Em um futuro distópico, a jovem Katniss Everdeen se oferece como tributo para participar dos Jogos Vorazes, "
              "uma competição mortal televisionada pelo governo da Capital, onde apenas um pode sobreviver."
)

# Exibindo as informações do livro
print(livro.exibir_info())