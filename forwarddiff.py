import math

# what need in e:
# xs
# xv
# func
# ddfunc

def printf(h, approx, err, err2):
    print "{0}\t{1:.10f}\t{2:.10f}\t{3:.10f}".format(h, approx, err, err2)


def forwarddiff(hs, xv, func, ddfunc):
    print "h\tf'({0})     \terror1    \terror2".format(xv)
    i = 0
    while i < len(hs):
        approx = (func(xv + hs[i]) - func(xv)) / hs[i]
        ddv = abs(ddfunc(xv))
        ddv2 = abs(ddfunc(xv + hs[i]))
        printf(hs[i], approx, abs(hs[i])*ddv/2, abs(hs[i])*ddv2/2)

        i = i+1


import e
forwarddiff(e.xs, e.xv, e.func, e.ddfunc)
