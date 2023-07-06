def maxproductarray(a, size):
    max_so_far = 1
    max_ending_here = 1
    flag = 0
    for i in range(0, size):

        max_ending_here = max_ending_here * a[i]

        if(a[i] > 0):
            flag = 1

        if(max_ending_here == 0):
            max_ending_here = 1

        if(max_ending_here > max_so_far):
            max_so_far = max_ending_here

    if(flag == 0):
        return 1
    else :    
        return max_so_far 

if __name__ == '__main__':
    arr1 = input()
    arr = list(map(int,arr1.split()))
    n = len(arr)
print(maxproductarray(arr, n))
