from sys import argv
from Parser import Parser

arq = argv[1]
# arq = " ".join(argv)
print(arq)
roda = Parser()
resul = roda.run(arq)
print(resul.evaluate())