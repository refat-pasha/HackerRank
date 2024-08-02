def strict_superset(a):
    n = int(input())
    for i in range(n):
        sub_set = set(input().split())
        if sub_set.difference(a):
            return False
    return True

a = set(input().split())
if strict_superset(a):
    print("True")
else:
    print("False")
