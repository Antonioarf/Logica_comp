from sys import argv
argv.pop(0)
programa =''
for e in argv:
    programa += e.replace(" ", "")
print(programa)
numeros = []
operacoes = ['+']
if not programa[0].isnumeric():
    raise Exception("Sintax error: equacao nao pode comecar com sinal")

for l in programa:
    if l.isnumeric():
        numeros.append(l)
    elif l =='+'or l=='-':
        operacoes.append(l)
    else:
        raise Exception("Invalid Char")

soma = 0
for e in range(len(numeros)):
    if operacoes[e]== '+':
        soma+= int(numeros[e]) 
    if operacoes[e]== '-':
        soma -= int(numeros[e]) 
print(soma)