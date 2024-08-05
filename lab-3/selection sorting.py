def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# List to be sorted
numbers = [22, 13, 4, 8, 17, 26, 53, 4]

# Sorting the list
sorted_numbers = selection_sort(numbers)

print("Sorted list:", sorted_numbers)
