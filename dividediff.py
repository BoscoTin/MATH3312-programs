import math
import e
import numpy

# what need in e
# xs
# iteration


a = numpy.zeros((len(e.xs), len(e.xs)))

i = 0
while i < e.iteration:
    count = len(e.xs) - i
    j = 0
    while j < count:
        print (i, j, count)
        if i == 0:
            a[i][j] = e.func(e.xs[j])
        else:
            a[i][j] = (a[i-1][j] - a[i-1][j+1]) / (e.xs[j] - e.xs[j+i])
        print a[i][j]
        j = j+1
    i = i+1

i = 0
while i < len(a):
    print a[i]
    i = i+1


# gen file
import os
filepath = os.getcwd()
filename = filepath + "/ddifffun.py"
file = open(filename, 'r+')

file.truncate(0)
file.write('PnX = lambda x:')

#loop
i = 0
while i < len(a):
    if i != 0:
        file.write('+ ')
    j = 0
    file.write('{0:.10f}'.format(a[i][j]))
    while j < i:
        file.write(' * (x - {})'.format(e.xs[j]))
        j = j+1
    file.write('\n')
    i = i+1

print "finish"
