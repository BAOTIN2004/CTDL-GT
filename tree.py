class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        
    def insert_key(self,key):
        new_node=Node(key)
        # nếu chưa có gì thì nhận làm gốc
        if self.key is None:
            self.key=new_node.key
            
        else:
            if key < self.key:
                if self.left is  None:
                    self.left=new_node
                else: self.left.insert_key(key)
            elif key> self.key:
                if self.right is None:
                    self.right=new_node
                else: self.right.insert_key(key)
            else: 
                print(f'Khóa bị trùng: {key}')

def Inorder_Traversal(node):
    if node is None: return
    print(node.key,end=' ')
    Inorder_Traversal(node.left)
    Inorder_Traversal(node.right)


a=Node(None)
a.insert_key(2)
a.insert_key(4)
a.insert_key(0)
Inorder_Traversal(a)
# class Binary_Tree:
#     def __init__(self,key=None):
#         node=Node(key)
#         if key is None:
#             self.root= None
#         else:
#             self.root=node
#     def insert_node(self,key):
#         node=Node(key)
#         if self.root is None:
#             self.root=node
#         else: 
#             self.root.insert_key(key) 
#     def delete_node( self,key):
#         pass
#     def hjh:pass
            