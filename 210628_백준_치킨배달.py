import sys
from pprint import pprint
from itertools import combinations


def dist(y1, x1, y2, x2):
    return abs(y2 - y1) + abs(x2 - x1)


input = sys.stdin.readline

n, m = map(int, input().split())
chicken = []
home = []

for i in range(n):
    for j, value in enumerate(map(int, input().split())):
        if value == 1:
            home.append([i, j])
        elif value == 2:
            chicken.append([i, j])

combi = list(combinations(chicken, m))

min_value = 1e6
for chicken_candidate in combi:
    total_distance = 0
    for y, x in home:
        distance = 1e6
        for chicken_house in chicken_candidate:
            cy, cx = chicken_house
            chicken_distance = dist(y, x, cy, cx)
            if chicken_distance < distance:
                distance = chicken_distance
        total_distance += distance
    min_value = min(min_value, total_distance)

print(min_value)
