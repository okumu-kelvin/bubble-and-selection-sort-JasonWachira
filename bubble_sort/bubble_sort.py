def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    n = len(unsorted_list)
    for i in range(n-1):
        # We don't need to compare with the already sorted elements at the end of the array
        # so the inner loop runs less i times
        for j in range(n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list




