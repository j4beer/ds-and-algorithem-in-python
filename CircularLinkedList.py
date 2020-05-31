class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def push(self,data):
        node = Node(data)
        temp = self.head

        node.next=self.head


        if self.head is not None:
            while(temp.next != self.head):
                temp=temp.next
            temp.next = node
        else:
            node.next = node

        self.head = node
        self.size += 1


    def printList(self):
        temp = self.head
        while(self.size != 0):
            print(temp.data)
            temp=temp.next
            self.size -= 1
        

def main():

    cll = CircularLinkedList()
    cll.push(20)
    cll.push(40)
    cll.push(22)
    cll.printList()

main()
