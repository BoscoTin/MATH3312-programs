L0x = lambda x: (x - 0.6)*(x - 0.9)/((0 - 0.6)*(0 - 0.9))
L1x = lambda x: (x - 0)*(x - 0.9)/((0.6 - 0)*(0.6 - 0.9))
L2x = lambda x: (x - 0)*(x - 0.6)/((0.9 - 0)*(0.9 - 0.6))
functions = [L0x, L1x, L2x]