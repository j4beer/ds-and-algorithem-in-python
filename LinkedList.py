class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data);
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp=temp.next
        temp.next = new_node

    def delBeg(self):
        temp = self.head.next
        self.head = temp

    def delEnd(self):
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next = None


def main():

    ll = LinkedList()

    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)
    ll.end(40)
    ll.delEnd();
    ll.delEnd();
    ll.printList()

main()
