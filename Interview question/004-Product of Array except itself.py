def productarray(arr, n):
    if(n==1):
        print(0)
        return
    left = [0]*n
    right = [0]*n
    prod = [0]*n
    left[0] = 1
    right[n-1] = 1
    for i in range(1,n):
        left[i] = arr[i-1]*left[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1]*arr[i+1]
    for i in range(n):
        prod[i]  = left[i]*right[i]
    for i in range(n):
        print(prod[i],end=' ')

if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    n = len(arr)
    productarray(arr, n)            
