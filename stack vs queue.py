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
class stack:
    # hàm khởi tạo rỗng 
    def __init__(self):
        self.items=[0,2,4]
    # hàm thêm phần tử
    def push(self,item):
        self.items.append(item)
        # hàm tính độ dài stack
    def __len__(self):
        return (f'Độ dài ngăn sắp xếp: {len(self.items)}')
    # hàm lấy phần tử , nếu độ dài của ngăn xếp bằng 0 thì trả về stack is empty
    def pop(self):
        if len(self.items==0): return " stack is empty"
        return self.items.pop()
    # hàm kiểm tra ngăn xếp rỗng
    def stack_is_empty(self):
        return "Ngăn xếp rỗng",len(self.items==0)
    # hàm hiển thị các phần tử trong ngăn xếp
    def __str__(self):
        return str(self.items)
    

