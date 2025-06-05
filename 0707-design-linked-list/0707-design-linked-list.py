class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        temp = self.head
        i = 0

        while temp:
            if i == index:
                return temp.val
            temp = temp.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.tail:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return


        i = 0
        temp = self.head

        while temp and i < index - 1:
            i += 1
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
            

        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return None
        
        temp = self.head
        i = 0
        while temp and i < index - 1:
            i += 1
            temp = temp.next

        temp.next = temp.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)