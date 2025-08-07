# Crie uma lista apenas com elementos numéricos
lista = [1,5,6,8,9,10,12,15]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['Mauricio', True, 12, 15.1,[1,2,3]]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(mista[0:-1:2])
# Remova da lista o último item
lista.pop()
print(lista)
# Insira na lista um novo item
lista.append(25)
print(lista)
# Remova da lista um item específico
mista.remove(15.1)
print(mista)