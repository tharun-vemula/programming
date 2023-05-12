import math
def min_max(arr,idx, curr_min, curr_max):
    if idx == len(arr):
        return (curr_max, curr_min)
    else:
        curr_min = min(curr_min, arr[idx])
        curr_max = max(curr_max, arr[idx])
        return min_max(arr, idx+1, curr_min, curr_max)


arr = [1,4,3,46,78,9,67] 
print(min_max(arr,0, math.inf, -math.inf))