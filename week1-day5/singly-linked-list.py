class Node:
    def __init__(self, data):
        self.data = data      # stores value
        self.next = None      # stores reference (address) of next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # INSERT - at Beginning - O(1)
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # INSERT - at End - O(n)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # DELETE - from Beginning - O(1)
    def delete_from_start(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # DELETE - from End - O(n)
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

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
    
    # DISPLAY - O(n)
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = SinglyLinkedList()

ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.display()          # 20 -> 10 -> 30 -> 40 -> None

ll.delete_from_start()
ll.display()          # 10 -> 30 -> 40 -> None

ll.delete_from_end()
ll.display()          # 10 -> 30 -> None

print(ll.search(30)) # 1
print(ll.search(50)) # -1




