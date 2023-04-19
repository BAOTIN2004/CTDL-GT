# tạo lớp dslk
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f'{self.data} vs { self.next}'
class Dslk:
    def __init__(self):
        self.dau=None
        self.duoi=None
    
    def add_LinkedList(self, data):
        # thêm vào sau
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
            truoc=now
            now=now.next
        if before==None:
            # chen dau dslk
            node.n
            
    
    def remove_LinkedList(self,data):
        pass
    
    def find_LinkedList(self,data):
        pass
    
    def print_LinkedList(self):
        print('Danh sách liên kết:',end=' ')
        temp=self.dau
        while (temp):
            print(temp.data,end='; ')
            temp=temp.next
def main():
    ds=Dslk()
    ds.add_LinkedList(12)
    ds.add_LinkedList(19)
    ds.print_LinkedList()
if __name__ =='__main__':
    main()