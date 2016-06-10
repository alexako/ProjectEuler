indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
array = ''.join([str(x) for x in xrange(1000000)])
ans = reduce(lambda x, y: x * y, [int(array[i]) for i in indices])
print "Answer:", ans
