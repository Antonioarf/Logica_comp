from sys import argv
from Tolkenizer import Tolkenizer
from Parser import Parser



argv.pop(0)
programa = " ".join(argv)
roda = Parser()
resul = roda.run(programa)
print(int(resul))