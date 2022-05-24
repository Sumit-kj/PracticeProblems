def isSafe(matrix, visited, x, y):
    """
    This function checks if it is safe to travel next co-ordinate
    :param matrix: The matrix of 1's and 0's
    :param visited: The visited array
    :param x: position on x
    :param y: position on y
    :return: The safe boolean value
    """
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not (matrix[x][y] == 0 or visited[x][y])


def findLongestPath(matrix, visited, i, j, destination, max_dist=0, dist=0):
    """
    This function finds the longest path between 1's
    :param matrix: The matrix of 1's and 0's
    :param visited: The visited array
    :param i: position on x
    :param j: position on y
    :param destination: The destination ot current path
    :param max_dist: The maximum distance so far
    :param dist: The current distance
    :return: the maximum distance
    """
    if matrix[i][j] == 0:
        return 0
    if (i, j) == destination:
        return max(dist, max_dist)
    visited[i][j] = 1

    if isSafe(matrix, visited, i + 1, j):
        max_dist = findLongestPath(matrix, visited, i + 1, j, destination, max_dist, dist + 1)
    if isSafe(matrix, visited, i, j + 1):
        max_dist = findLongestPath(matrix, visited, i, j + 1, destination, max_dist, dist + 1)
    if isSafe(matrix, visited, i - 1, j):
        max_dist = findLongestPath(matrix, visited, i - 1, j, destination, max_dist, dist + 1)
    if isSafe(matrix, visited, i, j - 1):
        max_dist = findLongestPath(matrix, visited, i, j - 1, destination, max_dist, dist + 1)

    visited[i][j] = 0
    return max_dist


def findLongestPathLength(mat, src, dest):
    i, j = src

    x, y = dest

    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return 0

    (M, N) = (len(mat), len(mat[0]))

    visited = [[0 for x in range(N)] for y in range(M)]

    return findLongestPath(mat, visited, i, j, dest)


if __name__ == '__main__':
    mat = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]

    src = (0, 0)
    dest = (5, 7)

    print("The maximum length path is", findLongestPathLength(mat, src, dest))