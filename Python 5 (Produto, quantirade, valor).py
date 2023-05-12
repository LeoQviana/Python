def estoque(nome, quantidade,valor):
    return nome, quantidade*valor

total=estoque("Fubá",30,5)

custo=estoque("O fubá custou R$",30,5)

print(total)
print(custo)

