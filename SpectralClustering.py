import numpy as np
float_formatter = lambda x: "%.3f" % x
np.set_printoptions(formatter={'float_kind':float_formatter})
from sklearn.cluster import KMeans
from matplotlib import pyplot as plot


# helper function to create diagonal matrix from adjacent
def createDD(adj, nodes):
    D = []
    for a in range(nodes):
        D.append([])
        for b in range(nodes):
            if a == b:
                D[a].append(sum(adj[a]))
            else:
                D[a].append(0)
    return D

# this implementation assumes that a similarity graph of the data was already constructed and that there is one connected component 
# it accepts the similarity graph's adjacency matrix, the desired number of clusters and the number of data points as input

def spectralC(a, c, points):

    # create diagonal degree matrix based on the similarity graph
    D = createDD(a, points)

    # calculate Laplacian based on adjacency matrix and diagonal degree matrix
    W = np.matrix(a)
    d_D = np.matrix(D)
    L = np.subtract(d_D, W)
    print('Adjacency Matrix')
    print(W)
    print()
    
    print('Diagonal Degree Matrix:')
    print(d_D)
    print()
    
    print('Laplacian:')
    print(L)
    print()

    # compute the eigenvectors and eigenvalues of the Laplacian
    eigenvalues, eigenvectors = np.linalg.eig(L)
    
    # sort the eigenvalues and eigenvectors
    eigenvectors = eigenvectors[:,np.argsort(eigenvalues)]
    eigenvalues = eigenvalues[np.argsort(eigenvalues)]

    print('eigenvalues:')
    print(eigenvalues)
    print('eigenvectors:')
    print(eigenvectors)
    print()

    # apply k-means clustering with the eigenvectors corresponding to the first c positive eigenvalues
    kmeans = KMeans(n_clusters=c)
    kmeans.fit(eigenvectors[:,1:c])
    clusters = kmeans.labels_

    print('clusters: ')
    print(clusters)


# sample/example data (from narrative)
X = np.array([
    [11, 6], [10, 4], [12, 4],
    [11, 2], [9, 14], [10, 16],
    [12, 16], [13, 14], [11, 14]
    ])
plot.scatter(X[:,0], X[:,1], alpha=1.0, edgecolors='b')
plot.xlabel('X')
plot.ylabel('Y')

A = [[0, 1, 1, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 1, 1, 0, 0]]

spectralC(A, 3, 9)
