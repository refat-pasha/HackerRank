if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i,j,k] for i in range(2) for j in range(2) for k in range(2) if (i+j+k)!=n])
