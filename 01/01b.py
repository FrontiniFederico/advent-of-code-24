import numpy

matrix = numpy.loadtxt("01/01a.txt", usecols=range(2), dtype=int)
smatrix = numpy.sort(matrix, axis=0)
num_rows, num_cols = smatrix.shape
left: int = 0
right: int = 0 
score: int = 0
while left < num_rows-1 and right < num_rows-1:
    if smatrix[left][0] < smatrix[right][1]:
        left+=1
    elif smatrix[left][0] > smatrix[right][1]:
        right+=1
    else:
        count: int = 1
        while smatrix[right+count][1] == smatrix[right][1]:
            count += 1
        score += smatrix[left][0]*count
        left+=1
print(score)