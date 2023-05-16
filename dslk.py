
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Dslk:
    def __init__(self):
        self.dau=None
        self.duoi=None
    
    def add_LinkedList(self, data):
        node=Node(data)
        if self.dau is None:
            self.dau=node
            self.duoi=node
        else: 
            self.duoi.next=node
            self.duoi=node
            
    def insert_LinkedList(self,index,value):
        node=Node(value)
        before=None
        now=self.dau
        i=0
        while i<index and now is not None:
            i+=1
            before=now
            now=now.next
        if before==None:
            # chen dau dslk
            node.next=self.dau
            self.dau=node   
            if self.duoi==None:
                self.duoi=node
        else:
            if now== None:
                # them vao cuoi ds
                self.duoi.next=node
                self.duoi=node
            else:
                # chen vao giua ds
                before.next=node
                node.next=now
                         
    
   
    
    def find_LinkedList(self,data):
        now=self.dau
        index=0
        a=[]
        while now!= None:
            if now.data==data:
                a.append(index)
            now=now.next
            index +=1
        return a
    
    
    
    def print_LinkedList(self):
        print('Danh sách liên kết:',end=' ')
        temp=self.dau
        while (temp):
            print(temp.data,end=' ')
            temp=temp.next
            
    def remove_LinkedList(self,data):
         
        if self.dau is None:
            return
        
        if self.dau.data == data:
            self.dau = self.dau.next
            
    
        now = self.dau
        prev = None
        while now is not None:
            if now.data == data:
                # nut trc se tro toi nut tiep theo , bo qua nut hien tai
                prev.next = now.next  
            prev = now
            now = now.next 
    
    
def main():
    ds=Dslk()
    ds.add_LinkedList(int(input('Thêm giá trị vào danh sách:')))
    ds.add_LinkedList(int(input('Thêm giá trị vào danh sách:')))
    ds.add_LinkedList(int(input('Thêm giá trị vào danh sách:')))

    ds.add_LinkedList(int(input('Thêm giá trị vào danh sách:')))
    # ds.add_LinkedList(int(input('Thêm giá trị vào danh sách:')))
    # index,value = map(int, input('Nhập lần lượt vị trí và giá trị muốn chèn (phân tách bằng dấu chấm phẩy): ').split(" "))
    # ds.insert_LinkedList(index,value)
    # ds.add_LinkedList(int(input('Thêm giá trị vào danh sách:')))
    print(ds.find_LinkedList(int(input('Nhập giá trị muốn tìm kiếm trong danh sách:'))))
    # ds.insert_LinkedList(7,18)
    ds.remove_LinkedList(int(input('Nhập giá trị muốn xóa khỏi danh sách liên kết:')))
    ds.print_LinkedList()
if __name__ =='__main__':
    main()