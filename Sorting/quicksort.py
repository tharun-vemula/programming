def quicksort(S, a, b):
    if a >= b:
        return
    pivot = S[b]
    left = a
    right = b - 1

    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1

        while left <= right and S[right] > pivot:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]

    quicksort(S, a, left - 1)
    quicksort(S, left + 1, b)


S = [31, 96, 85, 63, 24, 45, 17, 50]
quicksort(0, len(S) - 1)
print(S)
