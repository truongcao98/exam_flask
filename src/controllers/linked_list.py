class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """ Append an item to the list. """

        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def delete(self, data):
        """ Delete a node from the list. """
        current = self.head
        node_deleted = False
        if current is None:  # Item to be deleted is not found in the list
            node_deleted = False

        elif current.data == data:  # Item to be deleted is found at starting of list
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:  # Item to be deleted is found at the end of list.
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:  # search item to be deleted, and delete that node
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node

        self.size += 1

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            # Kiểm tra điều kiện có phải node cần xóa
            if current.data == data:
                if current == self.tail:
                    # Node đầu tiên
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next


class CircularList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next


def test(a: list, b: list, c: dict):
    return a, b, c


if __name__ == '__main__':
    a  = test([], {'k': 'v'}, [0, 1, 2, 3, ])
