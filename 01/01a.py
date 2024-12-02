import numpy

matrix = numpy.loadtxt("01/01a.txt", usecols=range(2), dtype=int)
smatrix = numpy.sort(matrix, axis=0)
total: int = 0
for riga in smatrix:
    total += abs(riga[0] - riga[1])
print(total)