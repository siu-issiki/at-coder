n, k, m = input().split()
a = input().split()

passage = sum(int(i) for i in a)
goal = int(n) * int(m)
required = goal - passage
if required > int(k):
    required = -1
elif required < 0:
    required = 0
print(required)
