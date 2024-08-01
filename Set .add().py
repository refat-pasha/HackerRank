def Names(n):
    names = set()
    while n > 0:
        names.add(input())
        n -= 1
    return names
n = int(input())
print(len(Names(n)))