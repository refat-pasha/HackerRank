a = int(input())
for i in range(a):
    a_ = int(input())
    a_set = set(map(int, input().split()))
    b = int(input())
    b_set = set(map(int, input().split()))
    if a_set.difference(b_set):
        print("False")
    else:
        print("True")