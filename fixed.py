import math

# what need in e
# func
# p0
# epsilon
# iteration
# specified

def printf(np, lp, diff, iter):
    print "{3}\t{1:.10f}\t{0:.10f}\t{2:.10f}".format(np, lp, diff, iter)


def fixed(func, lp, epsilon, iter, max_iter=None):
    try:
        np = func(lp)
    except ValueError:
        print "Error in iteration {}".format(iter)
        return (lp, iter - 1)

    diff = abs(np-lp)
    printf(np, lp, diff, iter)

    if(iter == max_iter):
        return (np, iter)
    if(diff < epsilon):
        return (np, iter)

    return fixed(func, np, epsilon, iter + 1, max_iter)


import e
if e.specified:
    root = fixed(e.func, e.p0, e.epsilon, 1, e.iteration)
else:
    root = fixed(e.func, e.p0, e.epsilon, 1)

print root
