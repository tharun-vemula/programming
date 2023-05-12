#Given an unsorted sequence, S, of integers and an integer k, 
#describe a recursive algorithm for finding the elements in S that sum to k. 


def find_sum_subset_util(arr, subset, target_sum, index):
    if target_sum == 0:
        print(subset)
        return
    
    if index == len(arr):
        return
    
    if arr[index] <= target_sum:
        subset.append(arr[index])
        find_sum_subset_util(arr, subset, target_sum - arr[index], index + 1)
        subset.pop()

    find_sum_subset_util(arr, subset, target_sum, index + 1)


def find_sum_subset(arr, k):
    subset = []
    find_sum_subset_util(arr, subset, k, 0)

arr = [1, 2, 3, 4, 5]
k = 6
print("Array:", arr)
print("Sum:", k)
print("Subsets that add up to the sum:")
find_sum_subset(arr, k)