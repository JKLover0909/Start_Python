def ketqua(arr):
    res = 0
    for i in range (len(arr)):
        for j in range (i+1, len(arr)):
            res = max(res, min(arr[i], arr[j])*(j-i))
    return res

if __name__ == '__main__':
    arr1 = input()
    arr = list(map(int,arr1.split()))
    print(ketqua(arr))