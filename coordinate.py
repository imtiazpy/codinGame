# On a Cartesian plane, given a point of coordinates (A, B) and N circles. Each circle is specified by its center coordinates (x, y) and its radius r.
# Calculate how many circles contains the point (A, B).
# Note: the point is counted if it is either inside or on the circle.
# Input
# Line 1 : A pair of integers A and B which is the coordinates of the point in question.
# Line 2 : An integer N which is the number of circles.
# N next lines : Three integers x, y, r where (x, y) are the coordinates of a circle center and r is the circle radius.
# Output
# Line 1 : A single integer which is the number of circles that contains point (A, B).


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    x, y, r = [int(j) for j in input().split()]

