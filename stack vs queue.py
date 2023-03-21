# sắp xếp các số theo thứ tự tăng dần
def bai_1(lst):
    # dùng vòng lặp để sắp xếp
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    # còn cách khác dùng lệnh có sẵn : sort(reverse=False)            
    return lst
    


# đếm số lần xuất hiện các phần tử trong list
def bai_2(lst):
    # chuyển về kiểu set để lấy các phần tử ở trong list bởi vì kiểu set không bị trùng giá trị
    a=set(lst)
    # duyệt qua tất cả các phần từ trong biến a
    for item in a:
            # dùng hàm count để đếm số lần xuất hiện của các phần tử trong set của list
            print(f'{item,lst.count(item)}')
            
## cài đặt stack 
#họkjll,;;
