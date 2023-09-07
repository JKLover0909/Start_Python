numray = [0,4,3,2,7,8,2,3,1]
arr_size = len(numray)
for i in range(arr_size):
    x = numray[i] % arr_size
    numray[x] = numray[x] + arr_size
for i in range(arr_size):
    if (numray[i] >= arr_size*2):
        print(i, " ")       