# Declare 4 variáveis do tipo numérica
x = 4
y = 12
z = 1
w = 8
# Crie uma estrutura condicional para comparar dois números
if x < y:
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
  print (f"Condição cumprida: o número {x} é menor que o número {y}")
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
else:
  print (f"Condição NÃO foi cumprida: o número {x} é maior que o número {y}")
# Insira outras condições na estrutura condicional usando o elif
if x < z:
  print (f"Condição cumprida: o número {x} é menor que o número {z}")
elif x < w:
  print (f"Condição cumprida: o número {x} é menor que o número {w}")
else:
  print (f"Condição NÃO foi cumprida: o número {x} é maior que o número {z} e o número {w}")
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (x < z) or (x < w):
  print (f"Condição cumprida: o número {x} é menor que o número {z} ou menor que o número {w}")
else:
  print (f"Condição NÃO foi cumprida: o número {x} é maior que o número {z} e o número {w}")
if (y > z) and (y > w):
  print (f"Condição cumprida: o número {y} é maior que o número {z} e o número {w}")
else:
  print (f"Condição NÃO foi cumprida: o número {y} é menor que o número {z} ou menor que o número {w}")
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if x < y:
  print (f"Condição cumprida: o número {x} é menor que o número {y}")
if z < w:
  print (f"Condição cumprida: o número {z} é menor que o número {w}")
