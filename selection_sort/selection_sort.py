def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    for i in range(n-1):
        min_elem = arr[i]
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_elem = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
    return arr


unsorted = [9,8,5,4,3]
print(selection_sort(unsorted))