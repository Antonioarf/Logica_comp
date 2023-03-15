from sys import argv
from Parser import Parser

arq = argv[1]
# arq = " ".join(argv)
roda = Parser()
programa = roda.leitura(arq)
resul = roda.run(programa)
print(resul.evaluate())