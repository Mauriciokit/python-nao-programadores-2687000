# Crie uma lista
cursos = ['SQL para iniciantes','EOS na prática','OKR e seus difereciais','Python para iniciantes','Estrutura de dados']
# Crie um for loop para imprimir cada elemento dessa lista
for cursor in cursos:
  print(cursor)

# Crie um objeto iterável utilizando a função range()
ranger = [range(5)]

# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
for ranger in range(5):
  print(f"{ranger} - Estou aprendendo uma linguagem de programação.")
else:
  print("fim do loop")