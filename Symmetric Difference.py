
a = int(input())
a_set = set(input().split())
b = int(input())
b_set = set(input().split())


x = list(a_set.difference(b_set))
y = list(b_set.difference(a_set))

z = x +y
z = list(map(int, z))
z.sort(reverse=False)

for i in range(0, len(z)):
    print(z[i])