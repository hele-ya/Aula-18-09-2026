class Aluno:
    def __init__(self, nome, matricula,nota1, nota2, nota3, nota4, nota5):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5

    def calcular_media(self):
        soma = self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5
        self.media = soma/5

        return self.media

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")
            


aluno1 = Aluno("Helen", "123456", 80, 75, 89, 90, 80)
aluno2 = Aluno( "Júlia", "654321", 80, 85, 79, 90, 85)

aluno1.calcular_media()
aluno1.verificar_aprovacao()

'''for atributo, valor in vars(aluno2).items():
    print(atributo+":", valor)'''