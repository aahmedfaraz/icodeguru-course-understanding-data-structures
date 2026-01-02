class Node:
    def __init__(self, data):
        self.data = data      # stores value
        self.prev = None      # reference to previous node
        self.next = None      # reference to next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None      # first node
        self.tail = None      # last node

    # INSERT - at Beginning - O(1)
    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head is None:
            # List is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # INSERT - at End - O(1)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            # List is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # DELETE - from Beginning - O(1)
    def delete_from_start(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # DELETE - from End - O(1)
    def delete_from_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # SEARCH - O(n)
    def search(self, key):
        temp = self.head
        pos = 0

        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1

        return -1

    # DISPLAY - Forward - O(n)
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # DISPLAY - Reverse - O(n)
    def display_reverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

ll = DoublyLinkedList()

ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.display()
# 20 <-> 10 <-> 30 <-> 40 <-> None

ll.display_reverse()
# 40 <-> 30 <-> 10 <-> 20 <-> None

ll.delete_from_start()
ll.display()
# 10 <-> 30 <-> 40 <-> None

ll.delete_from_end()
ll.display()
# 10 <-> 30 <-> None

print(ll.search(30))  # 1
print(ll.search(50))  # -1
