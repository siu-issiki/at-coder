import math

n = int(input())
coord = [[0,0]] * n

def getAngle(x1, y1, x2, y2):
  cosTheta = (x1 * y1 + x2 * y2) / (math.sqrt(x1 ** 2 + x2 ** 2) * math.sqrt(y1 ** 2 + y2 ** 2))
  print(x1 * y1 + x2 * y2)
  print(math.sqrt(x1 ** 2 + x2 ** 2) * math.sqrt(y1 ** 2 + y2 ** 2))
  print(cosTheta)
  return math.acos(cosTheta)

for i in range(n):
  x, y = map(int, input().split())
  coord[i] = [x, y]

print(getAngle(2,1,1,3))
