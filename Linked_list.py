

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"-->" if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)

    def insertValues(self,data_list):
        self.head=None
        for data in data_list:
            self.insertAtEnd(data)

    def insertAtBeginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)

    def insertAt(self,data,index):
        if index<0 or index>self.getLength():
            raise Exception("Invalid index")
        if index==0:
            self.insertAtBeginning(data)
        count=1
        itr=self.head
        while itr:
            if count==index:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1


    def getLength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def deleteAtbeginning(self):
        if self.head is None:
            return
        self.head=self.head.next

    def deleteAt(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid index")
        if index==0:
            self.deleteAtbeginning()
            return
        itr=self.head
        count=1
        while itr:
            if count==index:
                itr.next=itr.next.next
            itr=itr.next
            count+=1


if __name__=="__main__":
    l1=LinkedList()
    l1.insertAtEnd(5)
    l1.insertAtEnd(6)
    # 5 -->6
    # length
    # 2

    l1.insertValues([2,3,4])
    l1.print()
    print(f"length {l1.getLength()}")
    l1.deleteAtbeginning()
    l1.print()
    print(f"length {l1.getLength()}")
    # 2 -->3 -->4
    # length
    # 3
    # 3 -->4
    # length
    # 2
    print()

    l1.insertValues([2, 3, 4,5,6,7])
    l1.print()
    # 2 -->3 -->4 -->5 -->6 -->7
    l1.deleteAt(3) #index starts from 0
    l1.print()
    # 2 -->3 -->4 -->6 -->7

    l1.insertAt(12,2)
    l1.print()
    # 2 -->3 -->12 -->4 -->6 -->7