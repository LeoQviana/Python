##Faça uma função que recebe uma lista como argumento e crie uma nova lista, somente com numeros unicos.
a=[1,2,2,3,4,4,5,3,6,7,6,8]
novalista=[]

def lista(a):
    for x in a:
        if x not in novalista:
            novalista.append(x)
    return novalista

lista(a)
print(novalista)