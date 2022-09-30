
# Functions of the LinkedList
# add() -> to add element at the back of the LinkedList
# size() -> to get the size of the LinkedList
# insert() -> to insert a element at a particular position
# addToHead() -> adding a head node to the LinkedList
# getMid() -> to find the middle element of the LinkedList
# removeFront() -> to remove elements from the front element of the LinkedList
# removeBack() -> to remove element from the tail of the LinkedList


from black import main


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


list = LinkedList()


def size():
    if list.head is None:
        return -1

    count = 0
    temp = list.head
    while temp is not None:
        count = count+1
        temp = temp.next

    return count


def add(data):

    if list.head is None:
        node = Node(data)
        list.head = node
        node.next = None
        return

    temp = list.head
    while temp.next is not None:
        temp = temp.next

    node = Node(data)
    temp.next = node
    node.next = None


def insert(data, index):

    if list.head is None:
        return

    if index == 1:
        addToHead(data)
        return

    if index == size():
        add(data)
        return

    temp = list.head
    for i in range(index-1):
        temp = temp.next
    nextNode = temp.next

    node = Node(data)
    temp.next = node
    node.next = nextNode


def addToHead(data):
    if list.head is None:
        node = Node(data)
        list.head = node
        node.next = None
        return

    node = Node(data)
    node.next = list.head
    list.head = node


def getMid():
    if list.head is None:
        return

    fast = list.head
    slow = list.head

    while (fast is not None) and (fast.next is not None):
        fast = fast.next.next
        slow = slow.next

    return slow


def removeFront():
    if list.head is None:
        return

    list.head = list.head.next


def removeBack():
    if list.head is None:
        return

    temp = list.head

    while temp.next is not None:
        temp = temp.next

    temp.next = None


# main
add(1)
add(2)
add(3)
add(4)
insert(5, 4)
addToHead(6)
removeBack()

print(size())

temp = list.head

while temp.next.next is not None:
    print(temp.data, end="->")
    temp = temp.next
print(temp.data)

print("The mid element is ", getMid().data)
