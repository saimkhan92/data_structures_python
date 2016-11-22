# add new node in the front (at thr root's side)
import sys
class node():
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n
        
class linked_list(node):
    def __init__(self,r=None,l=0):
        self.length=l
        self.root=r
        
    def add(self,d):
        new_node=node()
        new_node.data=d
        if (self.root==None):  
            self.root=new_node
            new_node.next=None
            self.length=1
        else:
            self.length+=1
            new_node.next=self.root
            self.root=new_node
            
    def display(self):
        i=self.root
        while i:
            print(str(i.data)+" --> ",end="")
            i=i.next
        print("None")

    def delete(self,i):
        if self.root.data==i:
            self.root=self.root.next
        else:
            current_node=self.root.next
            previous_node=self.root
            while current_node:
                if current_node.data==i:
                    previous_node.next=current_node.next
                    return True
                    print(2)
                else:
                    previous_node=current_node
                    current_node=current_node.next
                    print("3")
                    
                    


lnk=linked_list()

lnk.add(10)
lnk.add(20)
lnk.add(30)
lnk.add(25)
lnk.display()
lnk.delete(30)
lnk.display()

        
            
    
