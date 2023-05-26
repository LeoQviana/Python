#Crie uma classe chamada ingresso, que possui um valor em reais e um metodo imprimeValor()
#Crie um classe VIP, que herda de Ingresso e possui um valor adicional. Crie um método que retorne o valor do ingresso
# ViP (com o adicional incluido)

class Ingresso():
    def __init__(self,valor):
        self.valor=valor

    def ImprimeValor(self):
        print(f"O valor do ingresso é R${self.valor}")

class VIP(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)

    def ImprimeValor(self,addic):
        total=self.valor+self.valor*addic/100


normal=Ingresso(90)
normal.ImprimeValor()

VIP= VIP(100)
VIP.ImprimeValor(10)

