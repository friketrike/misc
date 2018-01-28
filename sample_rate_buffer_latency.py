from __future__ import print_function
srs = [44.1, 48, 96]
bss = map(lambda x : 2**x, range(6, 12))
for sr in srs:
    print("SR: {0}".format(sr*1000))
    print("Buffer Size: {} ".format(bss[0]), end=" ")
    print(*("{:9d}".format(bs) for bs in bss[1:]), end=" ")
    print(" ")
    print("Period:    ", end=" ")
    for bs in map(lambda x : x/float(sr), bss):
        print("{0:6.3f}ms".format(bs), end="  ")
    print('\n')
    
