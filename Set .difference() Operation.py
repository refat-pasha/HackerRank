a = int(input())
a_list = set(map(int, input().split()))
b = int(input())
b_list = set(map(int, input().split()))

x = a_list.difference(b_list)
print(len(x))


