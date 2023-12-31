from sys import maxsize

def maxSubArraySum(a, size):
    max_so_far = -maxsize -1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if(max_ending_here < 0):
            max_ending_here = 0
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far

if __name__ == '__main__':
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubArraySum(a,len(a)))             
