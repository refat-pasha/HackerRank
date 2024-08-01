a = int(input())
original_list = list(map(int, input().split()))
unique_list = []
for item in original_list:
    if item != original_list:
        x = unique_list.append(item)
print(x)


