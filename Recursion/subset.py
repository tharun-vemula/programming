def print_subsets_util(arr, subset, index):
    if index == len(arr):
        print(subset)
        return

    subset.append(arr[index])
    print_subsets_util(arr, subset, index + 1)

    # Exclude the current element from the subset
    subset.pop()
    print_subsets_util(arr, subset, index + 1)


def print_subsets(arr):
    subset = []
    print_subsets_util(arr, subset, 0)

arr = [1, 2, 3]
print("Set:", arr)
print("Subsets:")
print_subsets(arr)