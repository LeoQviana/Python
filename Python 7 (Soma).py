def somar(*numeros):
    total=0
    for x in numeros:
        total+=x
    return total

total=somar(*(10,20,10,5))
print(total)



