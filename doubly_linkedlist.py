

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class doublyLinkedlist:
    def __init__(self):
        self.head=None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insertAtEnd(self,data):
        if self.head is None:
            node=Node(data)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None,itr)


    def insertValue(self,data_list):
        self.head=None
        for data in data_list:
            self.insertAtEnd(data)

if __name__=="__main__":
    l1=doublyLinkedlist()
    l1.insertAtEnd(4)
    l1.insertAtEnd(5)
    l1.insertAtEnd(6)
    l1.print_forward()

    l1.insertValue([1,2,3,4])
    l1.print_forward()