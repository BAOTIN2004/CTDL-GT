
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
        while now!= None and now.data != data:
            # nếu tìm thấy thì kết thúc vòng lặp
            now=now.next
            index +=1
        if now==None: return None
        else: return index
    
    def print_LinkedList(self):
        print('Danh sách liên kết:',end=' ')
        temp=self.dau
        while (temp):
            print(temp.data,end=' ')
            temp=temp.next
            
    def remove_LinkedList(self,data):
        # kiem tra vo rong hay k
        if self.dau is None:
            return
        
        if self.dau.data == data:
            self.dau = self.dau.next
            return
        
        now = self.dau
        while now.next is not None:
            if now.next.data == data:
                now.next = now.next.next
                return
            now = now.next
    
    
def main():
    ds=Dslk()
    ds.add_LinkedList(11)
    ds.add_LinkedList(12)
    ds.add_LinkedList(13)
    ds.add_LinkedList(14)
    ds.insert_LinkedList(4,15)
    ds.add_LinkedList(19)
    print(ds.find_LinkedList(15))
    ds.remove_LinkedList(15)
    ds.print_LinkedList()
if __name__ =='__main__':
    main()