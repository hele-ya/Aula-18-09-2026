class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def editar_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def mostrar_tudo(self):
        print(f"O título do livro é {self.titulo};\nO autor é {self.autor};\nO ano é {self.ano}")
        print("-----------------------------------")


livro1 = Livro("Casmurro", "Machado de Assis", 1899)

print(f"O título do livro é: {livro1.titulo}")

livro1.mostrar_tudo()
livro1.editar_titulo("Dom Casmurro") #Chamando o método
livro1.mostrar_tudo()

#print(f"O novo título do livro é: {livro1.titulo}")

