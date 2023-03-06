from sys import argv
from Parser import Parser

argv.pop(0)
programa = " ".join(argv)
roda = Parser()
resul = roda.run(programa)
print(resul)