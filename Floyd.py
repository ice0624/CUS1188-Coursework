import math

# adjacency matrix for graph G (which is W,  or D superscript 0)
w = [[0, 1, math.inf, 1, 5],
    [9, 0, 3, 2, math.inf],
    [math.inf, math.inf, 0, 4, math.inf],
    [math.inf, math.inf, 2, 0, 3],
    [3, math.inf, math.inf, math.inf, 0]]


def floyd(n, w):
    d = w

    # first loop keeps track of which d superscript we are calculating
    for k in range(n):
        # second loop keeps track of which row of d we are in
        for i in range(n):
            # third loop keeps track of which column of d we are in
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    print("D" + str(n) + ": ")
    print_matrix(d)


# helper method
def print_matrix(m):
    for x in m:
        print(x)


floyd(5, w)
