def texto(texto):
    texto_2=''.join(texto.split())
    return len(texto_2), texto[::-1]
print(texto("O pai ta on"))