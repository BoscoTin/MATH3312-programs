import lagrangefun
import e


fvs = []
i = 0
while i < len(e.xs):
    fvs.append(e.func(e.xs[i]))
    i = i+1

result = 0
i = 0
while i < len(e.xs):
    result += fvs[i] * lagrangefun.functions[i](e.xv)
    i = i+1

print "P({}) = {}".format(e.xv, result)
print "|P({0}) - f({0})| = {1}".format(e.xv, abs(result - e.func(e.xv)))
