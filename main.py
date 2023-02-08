from sys import argv
argv.pop(0)
programa =''
anterior = False
for e in argv:
    if e[0].isnumeric() and anterior: 
        raise Exception("Numero espaco Numero")
    programa += e
    if e[-1].isnumeric():
        anterior=True

if (not programa[0].isnumeric()) or (not programa[-1].isnumeric()):
    raise Exception("Sintax error: equacao nao pode comecar ou terminar com sinal")
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