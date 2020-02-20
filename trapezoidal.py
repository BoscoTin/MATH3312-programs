import math

# what need in e:
# a0
# b0
# interval
# func
# ddfunc


def trapezodial(a, b, interval, func, ddfunc):
    count = (b-a)/interval
    print count

    result = 0.0
    if count.is_integer():
        i = 0
        while i <= int(count):
            if i == 0 or i == count:
                result += func(a + i * interval)
                print "+ f({})".format(a+ i * interval)
            else:
                result += 2 * func(a + i * interval)
                print "+ 2f({})".format(a+ i * interval)
            i = i+1

        result = result * interval / 2
        print "* {}/2".format(interval)

        print "Approx value is {0:.10f}".format(result)
        print "Error is {0:.10f}".format(ddfunc(a) * math.pow(interval, 3) / 12)
        print "Error is {0:.10f}".format(ddfunc(b) * math.pow(interval, 3) / 12)

    else:
        print "Error in count"


import e
trapezodial(e.a0, e.b0, e.interval, e.func, e.ddfunc)
