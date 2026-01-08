# Colab File Link: 
# https://colab.research.google.com/drive/12LkxyloIQt2B5fHBAW5GHfxsM6ce34CM

# Singly Linked List
# list: a collection of items (nodes in this case)
# linked: connected to form a collection (using pointer in this case)
# singly: single connection for each node (next pointer for each node)

# Node strucutre
# data
# pointer to next node

# Other items in list
# head: pointer to first node of the list
# null pointer: used in last node to indicate the end of the list


# ------------------------- Creating a node -------------------------

class Node:
    def __init__(self, data=None):
        self.data = data # data stored in node
        self.next = None # pointer to next node

node1 = Node("A")
print(node1)
print(node1.data)
print(node1.next)

# Output:
# <__main__.Node object at 0x7ebf34d111c0>
# A
# None


# ------------------------- Address -------------------------

# identity and address
print(node1) # identity of the object

#  Output
# <__main__.Node object at 0x7ebf34d111c0>
# 139359689970112

# id() returns unique id of object
print(id(node1)) # memory address in CPython (version of Python)

node2 = Node("B")
print(node2.data)
print(node2.next)

print(node2)
print(id(node2))

# Output
# B
# None
# <__main__.Node object at 0x7ebf34d10e30>
# 139359689969200


# ------------------------- Linking Nodes -------------------------

# A link is established using a pointer

node1.next = node2
# now node1 points to node2

print(node1.data, node1.next)
print(id(node1.next), "id of node1.next")
print(id(node2), "id of node2")

# Output
# A <__main__.Node object at 0x7ebf34d10e30>
# 139359689969200 id of node1.next
# 139359689969200 id of node2


# ------------------------- Head -------------------------

head = node1
print(head.data)

# Output
# A


# ------------------------- Creating Linked List -------------------------

# function to link nodes and create list
def insert_at_start(head, data):
    new_node = Node(data) # create node
    new_node.next = head # connect to head | node -> head (prev_node)
    return new_node # return head (new_node is the head)

head = None # None
head = insert_at_start(head, "a") # a -> None
head = insert_at_start(head, "b") # b -> a -> None
head = insert_at_start(head, "c") # c -> b -> a - > None
head = insert_at_start(head, "d") # d -> c -> b -> a -> None
head = insert_at_start(head, "e") # e -> d -> c -> b -> a -> None


# ------------------------- Traversion -------------------------

# Traversion:
# Visiting every node once
# we move through next pointer

def traverse_list(head):
  curr = head # current node
  print(curr.data)

  while curr.next != None: # check if there is a node ahead
    curr = curr.next # move to that node
    print(curr.data)

traverse_list(head)

# Output:
# e
# d
# c
# b
# a

# Time Complexity O(n)
# Space Complexity O(1)


# ------------------------- Insertion - Start -------------------------

# Insertion at start
def insert_at_start(head, data):
    new_node = Node(data) # create node
    new_node.next = head # connect to head | node -> head (prev_node)
    return new_node # return head (new_node is the head)

head = insert_at_start(head, "f")

# lets check it
traverse_list(head)

# Output
# f
# e
# d
# c
# b
# a

# Time complexity: O(1)
# Space complexity O(1)


# ------------------------- Insertion - End -------------------------

# basic check
# move to end
# insert node
# connect to list

def insert_at_end(head, data):
    new_node = Node(data)

    # check if list is empty, then its first node
    if head is None:
        return new_node

    # move to end (traverse)
    curr = head
    while curr.next:
        curr = curr.next

    curr.next = new_node # connect node | last_node -> new_node
    return head

head = insert_at_end(head, "g")

# lets check it
traverse_list(head)

# Output
# f
# e
# d
# c
# b
# a
# g

# Time complexity: O(n)
# Space complexity O(1)


# ------------------------- Insertion - Middle -------------------------

# Insert after a given node
# basic check
# we access nodes through next pointer
# so we can insert new node next to a given node

def insert_at_specific(node, data):
    if node is None:
        print("Error: The given node is None")
        return

    new_node = Node(data) # create node
    new_node.next = node.next # connect to next | new_node -> node.next
    node.next = new_node # connect to previous | node -> new_node

insert_at_specific(head, "h")

# lets check it
traverse_list(head)

# Output
# f
# h
# e
# d
# c
# b
# a
# g

# Time complexity: O(1)
# Space complexity O(1)


# ------------------------- Deletion - Start -------------------------

# basic check
# point head to 2nd node
# delete 1st node
# return new head

def delete_from_start(head):
  # basic check
  if head is None: # list is empty
    print("Error: Singly linked list is empty")
    return None

  new_head = head.next
  return new_head

head = delete_from_start(head)

# lets check it
traverse_list(head)

# Output
# h
# e
# d
# c
# b
# a
# g

# Time complexity: O(1)
# Space complexity O(1)


# ------------------------- Deletion - End -------------------------

# basic check
# last node can be accessed through 2nd last node's next pointer
# so go to 2nd last node, update pointer

def delete_at_end(head):
    # basic check
    if head is None or head.next is None:
        print("Error: Singly linked list is empty or has only one node")
        return None

    # move to 2nd last node (note next.next)
    curr = head
    while curr.next.next: # differnece between traversion to last node and this
        curr = curr.next

    del_node = curr.next # last node stored
    curr.next = None # 2nd last points to None, so ends the list
    # del del_node

    return head

head = delete_at_end(head)

# lets check it
traverse_list(head)

# Output
# h
# e
# d
# c
# b

# Time complexity: O(n)
# Space complexity O(1)


# ------------------------- Deletion - Middle -------------------------

# basic check
# update next pointer of given node

def delete_after_node(node):
    # basic check: no node, or only node
    if node is None or node.next is None:
        print("Error: The given node is None or the next node is None")
        return

    next_node = node.next
    node.next = next_node.next
    
delete_after_node(head.next)

traverse_list(head)

# Output 
# h
# e
# c
# b

# Time complexity: O(1)
# Space complexity O(1)


# ------------------------- List versus Linked List -------------------------

# Comparing time complexity
# -------------------------------------------------
# | Operation        | List (array)|  Linked List |
# |------------------|-------------|---------------
# | Insert - Start   |     O(1)    |     O(n)     |
# | Insert - End     |     O(n)    |     O(1)     |
# | Insert - Middle  |     O(1)    |     O(n)     |
# | Delete - Start   |     O(1)    |     O(n)     |
# | Delete - End     |     O(n)    |     O(1)     |
# | Delete - Middle  |     O(1)    |     O(n)     |
# -------------------------------------------------


