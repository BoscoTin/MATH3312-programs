import e
values = e.xs


# change xs and xv in e.py then run this file to see functions in lagrangefun.py
# then calculate by running lagrange.py



# gen file
import os
filepath = os.getcwd()
filename = filepath + "/lagrangefun.py"
file = open(filename, 'r+')

# clear file
file.truncate(0)

i = 0
while i < len(values):
    file.write('L{}x = lambda x: '.format(i))

    j = 0
    count = 0
    while j < len(values):
        if i == j:
            pass
        else:
            file.write('(x - {})'.format(values[j]))
            if count < len(values) - 2:
                file.write('*')
                count = count + 1
        j = j+1
    file.write('/(')
    j = 0
    count = 0
    while j < len(values):
        if i == j:
            pass
        else:
            file.write('({} - {})'.format(values[i], values[j]))
            if count < len(values) - 2:
                file.write('*')
                count = count + 1
        j = j+1
    file.write(')\n')
    i = i+1

i = 0
file.write('functions = [')
while i < len(values):
    file.write('L{}x'.format(i))
    if i != len(values) - 1:
        file.write(', ')
    i = i+1
file.write(']')

print "Finish"
