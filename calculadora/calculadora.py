import numpy as np

mensagem = "Inisira a operação que deseja"
mensagem += "\n+ para adição"
mensagem += "\n- para subtração"
mensagem += "\n* para multiplicação"
mensagem += "\n/ para divisãoo \n"

operação =input(mensagem)

num_1=int(input("Insira o primeiro numero: "));
num_2 =int(input("Inisira o segundo numero: "))

if operação == '+':
    print (f"Operação: {num_1} {operação} {num_2} = {num_1 + num_2}")
elif operação == '-':
    print(f"Operação: {num_1} {operação} {num_2} = {num_1} - {num_2}")
elif operação == '*':
     print (f"Operação: {num_1} {operação} {num_2} = {num_1 * num_2}")
elif operação =='/':
    print (f"Operação: {num_1} {operação} {num_2} = {num_1 / num_2}")
else:
    print("Operação inválida")