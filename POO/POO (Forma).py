#Crie uma classe chamada Forma, que possui os atributos area e perimetro.
#Implemente as subclasses Retangulo e Triangulo, que devem conter os metodos calculaArea e calculaPerimetro.
#A classe Triangulo deve ter tambem o atributo altura.
#No código de teste crie um objeto da classe Triangulo e outros da Classe Retangulo. Verifique se os dois são mesmo
#instancias de Forma (use instanceof), e calcule a area de cada um.

class Forma:
    def __init__(self, area,perimetro):
        self.area=area
        self.perimetro=perimetro

class Retangulo(Forma):
    def __init__(self,altura,largura):
        area=altura*largura
        perimetro=2*(altura+largura)
        super().__init__(area,perimetro)

    def imprimiarea(self):
        print(f"A area do Retangulo é: {self.area}")
    def imprimeperimetro(self):
        print(f"O perimetro do Retangulo é: {self.perimetro}")

class Triangulo(Forma):
    def __init__(self,lado1,lado2,lado3):
        semiperimetro=(lado1+lado2+lado3)/2
        area=(semiperimetro*(semiperimetro-lado1)*(semiperimetro-lado2)*(semiperimetro-lado3))**0.5
        perimetro=lado1+lado2+lado3
        super().__init__(area, perimetro)

    def imprimearea(self):
        print(f"A area do Triangulo é: {self.area}")

    def imprimeperimetro(self):
        print(f"O perimetro do Triangulo é:{self.perimetro}")

retangulo=Retangulo(5,8)
retangulo.imprimearea()
retangulo.imprimeperimetro()

triangulo=Triangulo(3,4,5)
triangulo.imprimearea()
triangulo.imprimeperimetro()