#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Informe a temperatura em Celsius pra conversão: "))

farenheit = float(celsius*1.8 + 32)
print(round(farenheit, 2),"°F")