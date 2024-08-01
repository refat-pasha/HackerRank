a = int(input())
a_list = list(map(int, input().split()))
b = int(input())
b_list = list(map(int, input().split()))

x = set(a_list + b_list)
print(len(x))


