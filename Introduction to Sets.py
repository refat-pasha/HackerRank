def average(array):
    s= 0
    array = set(array)
    for i in array:
        s=s+i
    avg = f"{(s/len(array)):.3f}"
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)