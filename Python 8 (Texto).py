def contarletras(t):
    cont=0
    textoi= " "
    for x in t:
        if x not in " ":
            cont+=1
    print(cont)
    for y in range(len(t)-1,-1,-1):
        textoi+=t[y]
    print(textoi)


texto="Faça uma contagem"
contarletras(texto)