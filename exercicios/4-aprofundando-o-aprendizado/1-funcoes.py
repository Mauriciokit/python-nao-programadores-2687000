# Crie uma função para selecionar o curso desejado em uma trilha profissional
def seleciona_curso_trilha():
  curso = int(input(
      'Digite o número do curso que você deseja iniciar: 1 - introdução SQL, 2 - Python formação básica, 3 - EOS introdução:  '))
  return curso
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def percorre_curso(curso_selecionado):
  trilha = {1:{'titulo': 'introdução SQL', 'total_niveis':3}, 
            2:{'titulo': 'Python: formação básica', 'total_niveis':7}}
  
  curso_atual = trilha[curso_selecionado]['titulo']
  curso_nivel_atual = 1
  curso_total_niveis = trilha[curso_selecionado]['total_niveis']

  print(
      f'Bem vinda ao curso "{curso_atual}"!. Você esta iniciando o curso no nivel {curso_nivel_atual}. \n........')
  
  while curso_nivel_atual <= curso_total_niveis:
    print(
      f'Parabéns! Você acaba de finalizar a fase {curso_nivel_atual} do curso "{curso_atual}". ')
    curso_nivel_atual += 1
  else:
    print(f'Você concluiu o {curso_atual} com suceso!')

# Execute as funções

curso = seleciona_curso_trilha()
percorre_curso(curso)