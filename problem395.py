#!/usr/bin/python

# Euler Project Problem 395

"""Benchmark
Intel Core2 Duo CPU P8400  @ 2.26GHz 
real    0m0.150s
user    0m0.124s
sys 0m0.028s
"""

from numpy import matrix, array, arcsin, sin, cos

DIRECTIONS = {'NORTH' : 0, 'SOUTH' : 1, 'WEST' : 2, 'EAST' : 3}
ALPHA = arcsin(0.6)
BETA = arcsin(0.8)

def traverse(origin, theta, base, depth, max_depth, direction, min_max_set):
    minx, miny, maxx, maxy = min_max_set
    min_max_set[0] = min((origin[0], minx))
    min_max_set[1] = min((origin[1], miny))
    min_max_set[2] = max((origin[0], maxx))
    min_max_set[3] = max((origin[1], maxy))
    if depth == max_depth:
        return min_max_set

    a = base
    b = 0.8*a
    c = 0.6*a

    origin_left = origin + [-b*sin(theta+ALPHA), b*cos(theta+ALPHA)]

    left_top = origin_left + [b*cos(theta+ALPHA), b*sin(theta+ALPHA)]

    origin_right = origin + [a*cos(theta), a*sin(theta)] + \
            [c*(-sin(theta-BETA)-cos(theta-BETA)),\
             c*(-sin(theta-BETA)+cos(theta-BETA))]

    if direction == DIRECTIONS['NORTH']: 
        go_left = left_top[1] > origin_right[1]
    elif direction == DIRECTIONS['SOUTH']:
        go_left = left_top[1] < origin_right[1] or depth == 0
    elif direction == DIRECTIONS['WEST']: 
        go_left = left_top[0] > origin_right[0]
    else: #direction == DIRECTIONS['EAST']:
        go_left = left_top[0] < origin_right[0]

    if go_left:
        traverse(origin_left, theta+ALPHA, b, \
                depth+1, max_depth, direction, min_max_set)
    else: 
        traverse(origin_right, theta-BETA, c, \
                depth+1, max_depth, direction, min_max_set)


def calc_area(max_depth):
    min_max_set = [0, 0, 1, 1]
    traverse(array([0., 1.]), 0., 1., 0, \
            max_depth, DIRECTIONS['NORTH'], min_max_set)
    traverse(array([0., 1.]), 0., 1., 0, \
            max_depth, DIRECTIONS['SOUTH'], min_max_set)
    traverse(array([0., 1.]), 0., 1., 0, \
            max_depth, DIRECTIONS['WEST'], min_max_set)
    traverse(array([0., 1.]), 0., 1., 0, \
            max_depth, DIRECTIONS['EAST'], min_max_set)
    return (min_max_set[3]-min_max_set[1])*(min_max_set[2]-min_max_set[0])


area = calc_area(100)
print 'Answer to problem 395:', area
