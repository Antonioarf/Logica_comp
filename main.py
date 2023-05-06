from sys import argv
from Parser import *
from tolkens import tabela
arq = argv[1]
roda = Parser()
resul = roda.run(arq)
resul.evaluate()
print(tabela.tabela)

# tupla quando var vem direto





