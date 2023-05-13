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

    def prepend(self, data):
        new_node = Node(data)  # Tạo một nút mới với dữ liệu
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node  # Gắn con trỏ trỏ tới nút mới
            new_node.next = self.head  # Gắn con trỏ trỏ tới nút đầu tiên
            self.head = new_node  # Cập nhật con trỏ đầu tiên
    def insert(self,data,index):
        new_node=Node(data)
        now=self.head
        temp=None
        i=0
        while i<index and self.head!= None:
             temp=now
             now=now.next
        #nut hien tại trống: them dau ds
        if temp==None:
            self.head=new_node
        else:
            # now dang trỏ tới nut kế tiếp nếu trông thì tức là thêm vào cuối ds
            if now == None:
                temp.next=new_node
                
            
        
        
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:  # Kiểm tra nếu nút hiện tại chứa dữ liệu cần xóa
                if current.prev:  # Kiểm tra nếu nút hiện tại không phải là nút đầu tiên
                    current.prev.next = current.next  # Cập nhật con trỏ của nút trước đó
                else:
                    self.head = current.next  # Cập nhật con trỏ đầu tiên nếu nút hiện tại là nút đầu tiên
                if current.next:  # Kiểm tra nếu nút hiện tại không phải là nút cuối cùng
                    current.next.prev = current.prev  # Cập nhật con trỏ của nút kế tiếp
                break
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')  # In ra dữ liệu của nút hiện tại
            current = current.next
a=DoublyLinkedList()
a.append(1)
a.append(2)
a.append(3)
a.insert(4,3)
a.display()