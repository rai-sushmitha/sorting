def SelectionSort(arr, n):
    idx_min = 0
    for i in range(0,n-1):
        idx_min = i
        for j in range(i,n):

            if(arr[idx_min]> arr[j]):
                temp = arr[idx_min]
                arr[idx_min] = arr[j]
                arr[j] = temp
    return arr
  
if __name__ == "__main__":

    arr = [32,1,45,2,23,1,5]

    print(arr)
    arr = SelectionSort(arr, len(arr))
    print(arr)
