'''
Implementations of 1D and 2D peak-finding algorithms

Author: GotoCode
'''

import random


# 1D peak-finder #

def lin_find_peak(A):
    
    if len(A) == 0:
        return None
    elif len(A) == 1:
        return A[0]
    else:
        for i in range(len(A)):
            if i == 0 and A[i] >= A[i+1]:
                return i
            elif i == len(A)-1 and A[i] >= A[i-1]:
                return i
            elif A[i] >= A[i-1] and A[i] >= A[i+1]:
                return i

def log_find_peak(A, start, end):
    
    if (end - start) == 0:
        return None
    elif (end - start) == 1:
        return start
    else:
        mid = (start + end) / 2
        
        print 'mid:', mid
        
        if A[mid-1] >= A[mid]:
            return log_find_peak(A, start, mid)
        elif A[mid+1] >= A[mid]:
            return log_find_peak(A, mid+1, end)
        else:
            return mid


def main():
    # testing code #
    
    NUM_TESTS = 1
    
    for i in range(NUM_TESTS):
    
        test_arr = range(9)
    
        random.shuffle(test_arr)
        inp_arr, peak = test_arr, log_find_peak(test_arr, 0, len(test_arr))
    
        print inp_arr, '-> i =', peak


if __name__ == '__main__':
    main()