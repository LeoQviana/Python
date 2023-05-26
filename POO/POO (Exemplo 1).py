class Pessoa:
    def __init__(self,nome, peso, idade, comendo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=False
        self.dormindo=False

    def comer(self,comida):
        if self.comendo==False:
            print(f"{self.nome} começou a comer {comida}.")
            self.comando=True
        else:
            print(f"{self.nome} ja está comendo.")

    def parar_de_comer(self):
        if self.comendo==True:
            print(f"{self.nome} parou de comer.")
            self.comendo=False
        else:
            print(f"{self.nome} não está comendo")
    def falar(self):
        if self.falando==True:
            print(f"{self.nome} não pode falar, porque está comendo")
            self.falando=False
        else:
            print(f"{self.nome} está falando")
    def parardefalar(self):
        if self.falando:
            self.falando=False
            print(f"{self.nome} parar de falar")
        else:
            print(f"{self.nome} não está falando")

    def dormir(self):
        if not self.falando and not self.comendo and not self.dormindo:
            self.dormindo=True
            print(f"{self.nome} começou a dormir")
        elif self.dormindo:
            print(f"{self.nome} já está dormindo.")
        elif self.falando:
            print(f"{self.nome} não pode dormir falando")
        else:
            print(f"{self.nome} não pode dormir estando comendo")
    def acordar(self):
        if self.dormindo:
            self.dormindo = False
            print(f"{self.nome} acordou")
        else:
            print(f"{self.nome} ja está acordada")





p1=Pessoa("João",80,23)
p2=Pessoa("Maria",54,20)

print(f'{p1.nome}, tem {p1.idade} anos e pesa {p1.peso} quilos.')
print(f'{p2.nome}, tem {p2.idade} anos e pesa {p2.peso} quilos.')

p1.comer("Maçã")
p2.comer("Banana")
p1.parar_de_comer()
p2.parar_de_comer()
p1.falar()
p2.falar()
p1.parardefalar()
p2.parardefalar()
p1.dormir()
p2.dormir()
p1.acordar()
p2.acordar()