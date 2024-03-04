if __name__ == '__main__':
    arr = []
    n = int(input())
    arr = map(int,input().split())
    arr = set(arr)
    arr = sorted(arr)
    
    print(arr[-2])