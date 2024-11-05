import math


points = [(2, 3), (5, 8), (1, 7), (4, 6)]

# Öklid mesafesi 
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafe hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = min(distances)

print("Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)
