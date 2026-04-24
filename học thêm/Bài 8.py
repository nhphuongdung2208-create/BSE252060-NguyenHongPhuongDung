#Thuật toám sắp xếp
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # So sánh 2 phần tử liền kề
            if arr[j] > arr[j + 1]:
                # Hoán đổi trong Python
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr