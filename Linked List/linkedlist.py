from os import curdir


class Node:
    def __init__(self, item=None) -> int:
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self) -> int:
        self.head = Node()

# Adding of Linked List
    def append(self, item) -> int:
        new_node = Node(item)
        cursor = self.head
        while cursor.next != None:
            cursor = cursor.next
        cursor.next = new_node


# Total length of Linked List
    def length(self):
        cursor = self.head
        total = 0
        while cursor.next != None:
            total +=1
            cursor = cursor.next
        return total

# Display List 

    def display(self):
        elem = []
        new_cursor = self.head
        while new_cursor.next != None:
            new_cursor = new_cursor.next
            elem.append(new_cursor.item)
        print(elem)


# Get specifice data
    def get(self, index):
        if index >= self.length():
            print("Linked List out of range")
            return None
        cur_node = self.head
        cur_id = 0
        while True:
            cur_node = cur_node.next
            if cur_id == index: 
                return cur_node.item
            cur_id += 1
            

    def delete(self, index):
        if index >= self.length():
            print("Linked List out of range")
            return 
        cur_id = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_id == index:
                last_node.next = cur_node.next
                return
            cur_id += 1




list = LinkedList()