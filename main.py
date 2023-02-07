from sys import argv
argv.pop(0)
programa =''
for e in argv:
    programa += e.replace(" ", "")

if not programa[0].isnumeric():
    raise Exception("Sintax error: equacao nao pode comecar com sinal")
numeros = []
operacoes = ['+']
ultimo_n= False
for l in programa:
    if l.isnumeric():
        if ultimo_n:
            numeros[-1] +=l
        else:
            numeros.append(l)
        ultimo_n=True
    elif l =='+'or l=='-':
        operacoes.append(l)
        ultimo_n=False
    else:
        raise Error("Invalid Char")

soma = 0
for e in range(len(numeros)):
    if operacoes[e]== '+':
        soma+= int(numeros[e]) 
    if operacoes[e]== '-':
        soma -= int(numeros[e]) 
print(soma)