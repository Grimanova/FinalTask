def sort_list(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 9, 1, 7, 9, 14, 0]
    print("Sorted array:", sort_list(arr))
