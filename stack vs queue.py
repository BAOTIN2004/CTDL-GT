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
            
## cài đặt stack ( vào sau ra trước)
class Stack:
    # hàm khởi tạo 
    def __init__(self):
        self.items=[]
    # hàm thêm phần tử
    def push(self,item):
        self.items.append(item)
        # hàm tính độ dài stack
    def __len__(self):
        return (f'Độ dài ngăn sắp xếp: {len(self.items)}')
    # hàm lấy phần tử , nếu độ dài của ngăn xếp bằng 0 thì trả về stack is empty
    def pop(self):
        if len(self.items)==0: 
            return None
        return self.items.pop()
    # hàm kiểm tra ngăn xếp rỗng
    def stack_is_empty(self):
        if len(self.items)==0:
            return "Ngăn xếp rỗng"
        else: return len(self.items)
    # hàm hiển thị các phần tử trong ngăn xếp
    def __str__(self):
        return str(self.items)
a=Stack()
a.push(7)
a.push(6)
a.push(4)
print(a.pop())
print(a.__len__())
print(a)
# cài đặt queue ( vào trước ra trước)



# cài đặt Queue (vào trước ra trước)
class Queue:
    
    # phương thức khởi tạo hàng đợi rỗng
    def __init__(self):
        self.items = []
        
    # kiểm tra hàng đợi có rỗng hay không, trả về True hoặc False
    def is_empty(self):
        return len(self.items) == 0
    
    # thêm phần tử vào cuối hàng đợi
    def enqueue(self, item):
        self.items.append(item)
    # lấy phần từ theo quy tắc FIFO ra khỏi hàng đợi
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    # truy xuất thông tin số phần tử trong hàng đợi
    def __len__(self):
        return len(self.items)

def tim_kiem():
    a=[0,2]
    b=[1,34,2,3,4,0]
    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]: c.append(j)
    return c