class Animal:
    def __init__(self,nome):
        self.nome = nome
        print("O nome do animal é:",self.nome)

    def peso_animal(self,peso):
        self.peso = peso
        if(self.peso >10):
            print("O animal está acima do peso")
        else:
            print("O animal esta com peso normal")

nome_animal = input("Digite o nome do animal:")
animal1=Animal(nome_animal)

pesoanimal = float(input("Qual o peso do animal?"))
animal1.peso_animal(pesoanimal)