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
    def __init__(self,items):
        self.items=items
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

# cài đặt queue ( vào trước ra trước)




class Queue:
    def __init__(self):
        self.front = None # tham chiếu đến nút đầu tiên
        self.rear = None # tham chiếu đến nút cuối cùng

    def put(self, data):
        new_node = Dslk(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def get(self):
        if self.front is None:
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data

    # hàm kiểm tra xem ngăn đợi có trống hay không
    def empty(self):
        # chỉ cần kiểm tra nút đầu tiên
        if self.front is None:
            return True
        else:
            return False

  
def tim_kiem():
    a=[0,2]
    b=[1,34,2,3,4,0]
    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]: c.append(j)
    return c
tim_kiem()