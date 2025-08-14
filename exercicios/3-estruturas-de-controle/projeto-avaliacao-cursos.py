# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos = ['SQL para iniciantes',
          'EOS na prática',
          'OKR e seus difereciais',
          'Python para iniciantes',
          'Estrutura de dados']
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
primeiro_curso = 'EOS na prática'
melhor_curso = 'Python para iniciantes' 
ultimo_curso = 'Estrutura de dados'
# 3. Crie um dicionário vazio para armazenar a nota do curso
notas = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
if primeiro_curso in cursos:
  print (f"O curso {primeiro_curso} está contido na lista. Por favor infome a nota do curso: ")
  notas[primeiro_curso] = int(input('Qual a nota?'))
if primeiro_curso in cursos:
  print (f"O curso {melhor_curso} está contido na lista. Por favor infome a nota do curso: ")
  notas[melhor_curso] = int(input('Qual a nota?'))
if primeiro_curso in cursos:
  print (f"O curso {ultimo_curso} está contido na lista. Por favor infome a nota do curso: ")
  notas[ultimo_curso] = int(input('Qual a nota?'))

  print(notas)