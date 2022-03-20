#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
from statistics import median

Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
Nota3 = float(input("Digite a terceira nota: "))
Nota4 = float(input("Digite a quarta nota: "))

media = (Nota1+Nota2+Nota3+Nota4)/4

print("A média final é: " , media)