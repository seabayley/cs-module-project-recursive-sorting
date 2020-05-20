# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    while (arrA and arrB):
        merged_arr.append((arrA.pop(0) if arrA[0] < arrB[0] else arrB.pop(0)))
    merged_arr.extend(arrA + arrB)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    length = len(arr)
    if length > 1:
        middle_index = int(length/2)
        arr = merge(merge_sort(arr[:middle_index]),
                    merge_sort(arr[middle_index:]))
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    if arr[mid] <= arr[mid+1]:
        return
    while start <= mid and mid + 1 <= end:
        if arr[start] <= arr[mid+1]:
            start += 1
        else:
            v = arr[mid+1]
            i = mid+1
            while i != start:
                arr[i] = arr[i-1]

            arr[start] = v
            start += 1
            mid += 1

    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:
        m = l + (r-1) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)
        merge_in_place(arr, l, m, r)

    return arr


arr = [1, 9, 32, 7, 4, 7, 2, 8]
merge_sort_in_place(arr, 0, len(arr)-1)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
