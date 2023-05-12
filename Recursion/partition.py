#Given an unsorted sequence, S, of integers and an integer k, 
#describe a recursive algorithm for rearranging the elements in S so that all elements less than or equal to k come 
#before any elements larger than k. What is the running time of your algorithm on a sequence of n values


def partition(arr, low, high, k):
    i = low - 1

    for j in range(low, high):
        if arr[j] <= k:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def rearrange(arr, low, high, k):
    if low < high:
        pivot = partition(arr, low, high, k)
        rearrange(arr, low, pivot-1, k)
        rearrange(arr, pivot+1, high, k)

arr = [8, 3, 5, 1, 4, 2, 7, 6]
k = 4

print("Original Array:", arr)
rearrange(arr, 0, len(arr) - 1, k)
print("Rearranged Array:", arr)