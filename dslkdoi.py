class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Con trỏ trỏ tới nút trước đó
        self.next = None  # Con trỏ trỏ tới nút kế tiếp

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Con trỏ đầu tiên của danh sách
        
    def append(self, data):
        new_node = Node(data)  # Tạo một nút mới với dữ liệu
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next!=None:
                current = current.next
            current.next = new_node  # Gắn nút mới vào cuối danh sách
            new_node.prev = current  # Gắn con trỏ trỏ tới nút trước đó
    def insert(self,data,index):
        new_node=Node(data)
        now=self.head
        temp=None
        i=0
        while i<index and now!= None:
            i+=1
            temp=now
            now=now.next
        #nut hien tại trống: them dau ds
        if temp==None:
            new_node.next=self.head
            self.head=new_node
        # index vuot qua danh sach thì thêm vào cuối, kh thì vào giữa        
        else:
                temp.next=new_node
                new_node.next=now

    def delete(self, data):        
        temp=self.head
        while temp is not None:
            if temp.data==data:
                if temp.prev is None:
                     self.head = temp.next
                else: 
                    if self.head is  None:
                        self.head.prev = None
        # Nếu phần tử cần xóa không phải là nút đầu tiên
                    else:
                        if temp.next is not None:
                            temp.prev.next=temp.next
                            temp.next.prev=temp.prev
                        else:
                            temp.prev.next=None
            temp=temp.next 
    
    def search(self,data):
        i=0
        a=[]
        temp=self.head
        while temp is not None:
            if temp.data==data:
                a.append(i)
            i+=1
            temp=temp.next
        if a is None: return None
        else: return a
            
               
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')  # In ra dữ liệu của nút hiện tại
            current = current.next
a=DoublyLinkedList()
a.append(0)
a.append(1)
a.append(1)
a.append(2)
a.append(3)
a.delete(1)

a.display()
print('\n',a.search(7))

