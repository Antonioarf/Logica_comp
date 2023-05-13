from sys import argv
from Parser import *
from tolkens import tabela, assembler
arq = argv[1]
roda = Parser()
resul = roda.run(arq)
resul.evaluate(0)
assembler.write(arq)
# print(tabela.tabela)