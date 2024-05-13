def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # L = [0] * (n1)
    # R = [0] * (n2)
    L = []
    R = []

    for i in range(0, n1):
        L.append(arr[l+i])

    for j in range(0, n2):
        R.append(arr[m+1+j])

    i, j = 0, 0
    k = l
    while(i<n1 and j<n2):
        if(L[i]<=R[j]):
            arr[k] = L[i]
            i=i+1
        else:
            arr[k] = R[j]
            j=j+1
        k=k+1
    while (i < n1):
        arr[k] = L[i]
        k = k + 1
        i = i + 1
    while (j < n2):
        arr[k] = R[j]
        k = k + 1
        j = j + 1

    # temp = []
    # k = 0
    # i, j = l, m+1
    #
    # print("m + 1 + n2  = ", m + 1 + n2)
    # print("l + n1  = ", l + n1)
    # while (i < l + n1 and j < m + 1 + n2):
    #     if (arr[i] <= arr[j]):
    #         temp[k].append(arr[i])
    #         i = i + 1
    #     else:
    #         temp[k].append(arr[j])
    #         j = j + 1
    #     k = k + 1
    # while (i < l + n1):
    #     temp[k].append(arr[i])
    #     k = k + 1
    #     i = i + 1
    # while (j < m + 1 + n2):
    #     temp[k].append(arr[j])
    #     k = k + 1
    #     j = j + 1
    #
    # for i in range(0, n1 + n2):
    #     arr[l + i] = temp[i]


def mergeSort(arr, l, r):
    if (l < r):
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == "__main__":
    arr = [6, 2, 9, 1, 2, 0]
    print("Unsorted array: ", arr)
    mergeSort(arr, 0, len(arr)-1)
    print("Sorted array: ", arr)
