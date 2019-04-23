
import numpy as np

def compute_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def compute_center(points):
    x = 0
    y = 0
    length = len(points)

    for point in points:
        x += point[1]
        y += point[0]
    x = np.ceil(x / length)
    y = np.ceil(y / length)
    return [y, x]

def compute_sum_distance():
    pass

K = 2
points = [[1, 1],
          [1, 2],
          [1, 4],
          [3, 4],
          [3, 5]]

center = []
i = 0
while i < K:
    center.append(points[(len(points)-1)//K * i])
    i += 1

distance_sum_last = 999999999
count = 0

while True:
    distance_sum = 0
    cluster = [[] for i in range(K)]
    for point in points:
        distances = [compute_distance(center[i], point) for i in range(K)]
        cluster[distances.index(min(distances))].append(point)
        distance_sum += min(distances)

    if distance_sum < distance_sum_last:
        distance_sum_last = distance_sum
    else:
        break

    for i in range(len(center)):
        center[i] = compute_center(cluster[i])


print(center)
print(distance_sum_last)


