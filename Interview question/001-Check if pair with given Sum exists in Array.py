def check(A, size, x):
    for i in range(0,size-1):
        for(j) in range(i+1,size):
            if(A[i]+A[j]==x):
                return True
    return False


if __name__ == '__main__':
    A = [0, -1,  2, -3,  1]
    x = -2
    size  = len(A)
    print(check(A,size,x))