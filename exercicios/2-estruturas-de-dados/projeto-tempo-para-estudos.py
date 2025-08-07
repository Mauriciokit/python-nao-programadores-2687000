# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

total_dias = int(input("Qual o total de dias dedicados ao estudo por semana: "))
print(f"{total_dias} é o total de dia(s) de estudos por semana!")

total_horas = int(input("Qual a média de horas estudada por dia: "))
print(f"{total_horas} é a média de estudo por dia!")

curso = input("Qual o título do curso desejado: ")
print(f"{curso} é o título do curso desejado!")

soma = (total_dias * total_horas)

print(f"O estudante {nome}, dedica {total_dias} dia(s) aos estudos, no total de {soma} hora(s) semanais para o {curso}.")