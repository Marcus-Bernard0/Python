lista = []
while True:
    num= int(input('Digite um numero: '))
    lista.append(num)
    per = str(input('Continuar [S/N]: ')).upper()[0]
    if per== 'N':
        break

maior =max(lista)
menor =min(lista)
soma  =sum(lista)
ordenar =sorted(lista)

print(f'Os valores digitados são: {lista}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
print(f'A soma é: {soma}')
