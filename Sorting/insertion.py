def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [4, 3, 1, 7, 54]
insertion_sort(arr)
print(arr)
