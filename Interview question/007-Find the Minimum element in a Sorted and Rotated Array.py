def findmin(a,size):
    for i in range(0,size):
        if(a[i]>a[i+1]):
            return a[i+1]
        
if __name__ == '__main__':
    arr1 = input()
    arr = list(map(int,arr1.split()))
    n = len(arr)
    print(findmin(arr,n))