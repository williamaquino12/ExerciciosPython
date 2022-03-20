#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor = int(input('Quando você ganha por horas trabalhadas?: '))
horas = int(input('Quantas horas, você trabalha por mês?: '))
salario = valor * horas
salario_total = valor * horas

print("Salário total: ", salario_total)