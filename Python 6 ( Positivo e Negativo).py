def num(n):

    if n==0:
        return "Z"
    if n>0:
        return "P"
    if n<0:
        return "N"

n=int(input("Digite um numero"))
resultado=num(n)
print(resultado)