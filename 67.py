def find_max_path(triangle):
    # Start from bottom of triangle
    for row in xrange(len(triangle)-1, 0, -1):
        for col in xrange(0, row):
            triangle[row-1][col] += max( #Get max of adjacent 1 of 2
                triangle[row][col],
                triangle[row][col+1]
            )

    return triangle[0][0]


if __name__ == '__main__':

    file = "p067_triangle.txt"
    tri = [
        [int(n) for n in line.split()]
        for line in open(file).readlines()
    ]

    print "Max total: ", find_max_path(tri)
