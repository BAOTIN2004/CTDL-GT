# các loại sắp xếp.
# lưu ý các mã lệnh phía dưới đều là sắp xếp tăng dần.


def sap_xep_chon(lst):
    lst_1=lst.copy()
    for i in range(len(lst)-1):
        min=i
        for j in range(i+1,len(lst_1)):
            if lst_1[j]<lst_1[min]:
                min=j
        lst_1[min],lst_1[i]=lst_1[i],lst_1[min]
    return lst_1

# sắp xếp nổi bọt
def sap_xep_noi(lst):
    lst_1=lst.copy()
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst_1[i]>lst_1[j]:
                lst_1[i],lst_1[j]=lst_1[j],lst_1[i]
    return lst_1

# sắp xếp chèn  
def sap_xep_chen(lst):
    lst_1=lst.copy()
    for i in range(len(lst)):
        index_min=i
        min=lst_1[i]
        while( index_min>0 and(lst_1[index_min-1]>min)):
            lst_1[index_min]=lst_1[index_min-1]
            index_min-=1
        lst_1[index_min]=min
    
    return lst_1
# sắp xếp nhanh
def sap_xep_nhanh(lst):
    lst_1=lst.copy()
    left=0
    right=len(lst)-1
    pivot=lst_1[right] # khai báo phần tử đánh 

    while(True):
        while(left<=right and lst_1[left]<pivot ):
            left +=1
        while (right>=left and lst_1[right]>pivot):
            right-=1
        if left>= right: break
        lst_1[left],lst_1[right]=lst_1[right],lst_1[left]
        left+=1
        right -=1
  #  lst_1[left],lst_1[right]=lst_1[right],lst_1[left]
    return lst_1

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
arr = [3, 1, 7, 5, 2, 4, 6]
quicksort(arr, 0, len(arr) - 1)
# print(arr)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # So sánh nút gốc với nút con bên trái
    if left < n and arr[i] < arr[left]:
        largest = left

    # So sánh nút gốc với nút con bên phải
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Nếu nút gốc không lớn nhất, hoán đổi với nút con lớn nhất và tiếp tục đệ quy
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Xây dựng vun đống (heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Trích xuất từng phần tử từ vun đống đã xây dựng
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Hoán đổi nút gốc với nút cuối cùng chưa sắp xếp
        heapify(arr, i, 0)

# Ví dụ sử dụng
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Mảng đã sắp xếp: ")
for i in range(len(arr)):
    print( arr[i], end=" ")

