"""Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects
all the vertices together. A single graph can have many spanning trees. A minimum spanning tree (MST) or
minimum weight spanning tree for a weighted, connected, undirected graph is a spanning tree with a weight less than
or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to
each edge of the spanning tree. """
from src.res.Greedy.kruskals_mst import input as ip


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    n = ip.n
    result, cost = kruskals_mst(arr, n)
    print(result)
    print(cost)


def kruskals_mst(arr, n):
    """
    TO implement the kruskals mst
    :param arr: the array of (u, v, w)
    :param n: number of vertices
    :return: the list of all edges present in the mst
    """
    result = []
    u, v, w = [], [], []
    parent = [i for i in range(n)]
    number_of_edges = 0
    arr = sort_based_on_w(arr)
    cost = 0
    for a in arr:
        u.append(a[0])
        v.append(a[1])
        w.append(a[2])

    for i, weight in enumerate(w):
        source_origin = find_origin(u[i], parent)
        dest_origin = find_origin(v[i], parent)
        if source_origin != dest_origin and number_of_edges < n-1:
            parent[u[i]] = v[i]
            result.append((u[i], v[i]))
            number_of_edges += 1
            cost += weight
    return result, cost


def sort_based_on_w(arr):
    """
    This function sorts the edges based upon their weight
    :param arr: unsorted array of edges
    :return: sorted array of edges
    """
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j][2] < arr[min_index][2]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def find_origin(child, parent):
    """
    To find the origin for the graph
    :param child: the node for which we've to find origin
    :param parent: the parent array
    :return: the origin of
    """
    while parent[child] != child:
        child = parent[child]
    return parent[child]
