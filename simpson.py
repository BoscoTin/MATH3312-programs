import math

# what need in e:
# a0
# b0
# interval
# func
# d4func

def simpson(a, b, interval, func, d4func):
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
                if i % 2 == 1:
                    # even
                    result += 4 * func(a + i * interval)
                    print "+ 4f({})".format(a+ i * interval)
                else:
                    # odd
                    result += 2 * func(a + i * interval)
                    print "+ 2f({})".format(a+ i * interval)
            i = i+1

        result = result * interval / 3
        print "* {}/3".format(interval)

        print "Approx value is {0:.10f}".format(result)
        print "Error is {0:.10f}".format(d4func(a) * math.pow(interval, 5) / 90)
        print "Error is {0:.10f}".format(d4func(b) * math.pow(interval, 5) / 90)

    else:
        print "Error in count"


import e
simpson(e.a0, e.b0, e.interval, e.func, e.d4func)
