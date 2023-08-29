def findpivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((low + high)/2)
    if mid < high and arr[mid] > arr[mid +1]:
        return mid
    if mid > low  and arr[mid] < arr[mid -1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return findpivot(arr, low, mid-1)
    return findpivot(arr, mid + 1, high)

def binarysearch(arr, low, high, key):
    if high < low:
        return -1
    mid = int((low+high)/2)
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarysearch(arr, (mid+1), high, key)
    return binarysearch(arr, low, (mid-1), key)

def pivotbinarysearch(arr, n, key):
    pivot = findpivot(arr, 0, n-1)
    if pivot == -1:
        return binarysearch(arr, 0, n-1, key)
    if arr[pivot] == key:
        return pivot
    if arr[0] >= key:
        return binarysearch(arr, pivot+1, n-1, key)
    return binarysearch(arr, 0, pivot-1, key)

if __name__ == '__main__':
    arr1 = input()
    arr = list(map(int,arr1.split()))
    key = int(input())
    n = len(arr)
    print(pivotbinarysearch(arr, n, key))