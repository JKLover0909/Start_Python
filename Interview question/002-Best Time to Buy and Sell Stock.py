
if __name__ == '__main__':
    A = [7,1,5,3,6,4]
    size  = len(A)
    maxProfit = 0
    buy = A[0]
    for i in range(0,size-1):
        if(A[i]<buy):
            buy = A[i]
        else :
            if(A[i]-buy>maxProfit):
                maxProfit = A[i]-buy   
    print(maxProfit)                 