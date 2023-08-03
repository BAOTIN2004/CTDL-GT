def sap_xep_chon(lst):
    for i in range(len(lst)-1):
        index_min=i
        for j in range(i+1,len(lst)):
            if lst[index_min]>lst[j]:
                index_min=j
        lst[index_min],lst[i]=lst[i],lst[index_min]
    return lst

def sap_xep_chen(lst):
    for i in range(1,len(lst)):
        min_value=lst[i] # 0
        min_index=i     # 3
        while (min_value<lst[min_index-1]and min_index>0):
            lst[min_index]=lst[min_index-1]    #1204  1024  1124
            min_index-=1                        # 2   1
        lst[min_index]=min_value                # 0124
    return lst

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Sử dụng hàm quicksort
arr = [8,7,4,9]
quicksort(arr,0,len(arr)-1)