from sys import argv
from Parser import *
from tolkens import tabela
arq = argv[1]
roda = Parser()
resul = roda.run(arq)
resul.evaluate(0)
assembler.write(arq)
assembler.write('teste')
print(tabela.tabela)
#resolver while: tem q evaluate condicao antes
# int*str
#
#
#
