#!/usr/bin/python

# Euler Project Problem 393

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
"""
def count_paths(i, j, n, grid, steps, path):

    if steps == n*n and (i, j) == (0, 0):
        print path
        return 1

    path_cnt = 0
    if j != 0 and not grid[i][j-1] and steps != 1:
        grid[i][j-1] = True
        path.append((i, j-1))
        path_cnt += count_paths(i, j-1, n, grid, steps+1, path)
        path.remove((i, j-1))
        grid[i][j-1] = False

    if i != 0 and not grid[i-1][j] and steps != 1:
        grid[i-1][j] = True
        path.append((i-1, j))
        path_cnt += count_paths(i-1, j, n, grid, steps+1, path)
        path.remove((i-1, j))
        grid[i-1][j] = False

    if i != n-1 and not grid[i+1][j]:
        grid[i+1][j] = True
        path.append((i+1, j))
        path_cnt += count_paths(i+1, j, n, grid, steps+1, path)
        path.remove((i+1, j))
        grid[i+1][j] = False

    if j != n-1 and not grid[i][j+1]:
        grid[i][j+1] = True
        path.append((i, j+1))
        path_cnt += count_paths(i, j+1, n, grid, steps+1, path)
        path.remove((i, j+1))
        grid[i][j+1] = False

    return path_cnt

n = 4
grid = [[False]*n for _ in xrange(n)]
cnt = count_paths(0, 0, n, grid, 0, [])
print cnt
