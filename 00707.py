# https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self, value: int):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1
        
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        self.count += 1


    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.count:
            return
        if index == 0: # push
            self.addAtHead(val)
            return
        if index == self.count: # insere no fim
            self.addAtTail(val)
            return

        current = self.head
        for i in range(index-1): # percorre até anterior do index
            current = current.next
        
        # amarrar os nós:
        newNode = Node(val)
        aux = current.next
        current.next = newNode
        newNode.next = aux
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.count == 0:
            return
        if index == 0:
            self.head = self.head.next
        else:
            if index < self.count:
                current = self.head
                for i in range(index-1):
                    current = current.next
                current.next = current.next.next
                if current.next == None: # atualiza novo fim
                    self.tail = current
            else:
                return # index >= tam. da lista

        self.count -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
