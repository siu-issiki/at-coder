n, m = input().split()
a = [False] * int(n)
penalty = [0] * int(n)
AC = 0
WA = 0
for i in range(int(m)):
  p, s = input().split()
  if(s == "AC" and a[int(p) - 1] == False):
    a[int(p) - 1] = True
    WA += penalty[int(p) - 1]
    AC += 1
  if(s == "WA" and a[int(p) - 1] == False):
    penalty[int(p) - 1] += 1

print(AC, WA)
