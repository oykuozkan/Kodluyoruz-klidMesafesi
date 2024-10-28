Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... 
... points = [(1, 3), (4, 2), (5, 6), (7, 8)]
... 
... def euclideanDistance(point1, point2):
...     return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
... 
... distances = []
... for i in range(len(points)):
...     for j in range(i + 1, len(points)):
...         distance = euclideanDistance(points[i], points[j])
...         distances.append(distance)
... 
... min_distance = min(distances)
... 
... print("Mesafeler:", distances)
... print("Minimum Mesafe:", min_distance)
... 
