import math

def compute_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def compute_center(points):
    x = 0
    y = 0
    length = len(points)

    for point in points:
        x += point[1]
        y += point[0]
    x = math.ceil(x / length)
    y = math.ceil(y / length)
    return [y, x]

K = int(input())
points = []
# for _ in range(5):
#     point = input().split()
#     points.append([int(point[0]), int(point[1])])

for _ in range(5000):
    points.append([0, 0])
for _ in range(5000):
    points.append([2, 2])

# points = [[1, 1],
#           [1, 2],
#           [1, 4],
#           [3, 4],
#           [3, 5]]

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

for c in center:
    print('{0:.5f} {1:.5f}'.format(c[0], c[1]))
# print(center)
# print(distance_sum_last)


