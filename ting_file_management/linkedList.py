from node import Node


class LinkedList:
    def __init__(self, value) -> None:
        self.__length = 0
        self.__head, self.__tail = None, None
        self.__curr = None

        if type(value) in (list, tuple):
            self.extend(value)
        elif value:
            self.__init_list(value)

    def __len__(self):
        return self.__length

    def __iter__(self):
        self.__curr = self.__head
        return self

    def __next__(self):
        curr = self.__curr
        if curr:
            self.__curr = self.__curr.next
            return curr.value
        raise StopIteration

    def __init_list(self, value):
        node = Node(value)
        self.__length = 1
        self.__head = node
        self.__tail = node

    def extend(self, list):
        for value in list:
            self.add(value)

    def add(self, value):
        if self.__tail:
            node = Node(value, prev=self.__tail)
            self.__tail.next = node
            self.__tail = node
            self.__length += 1
        else:
            self.__init_list(value)

    def add_first(self, value):
        if self.__head:
            node = Node(value, next=self.__head)
            self.__head.prev = node
            self.__head = node
            self.__length += 1
        else:
            self.__init_list(value)

    def __remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.value

    def pop(self, index=0):
        if not (index > (0 - self.__length) and index < self.__length):
            raise IndexError
        if index == -1:
            return self.pop_last()
        if index == 0:
            return self.pop_first()
        return self.__pop_at(index)

    def __pop_at(self, index: int):
        node = None
        if index > 0:
            node = self.__head.next
            curr_ind = 1
            while curr_ind < index:
                curr_ind += 1
                node = node.next
        if index < -1:
            node = self.__tail.prev
            curr_ind = -2
            while curr_ind > index:
                curr_ind -= 1
                node = node.prev
        return self.__remove(node)

    def pop_first(self):
        first = self.__head
        self.__head = self.__head.next
        self.__head.prev = None
        return first

    def pop_last(self):
        last = self.__tail
        self.__tail = self.__tail.prev
        self.__tail.next = None
        return last

    def get_first(self):
        return self.__head.value

    def get_last(self):
        return self.__tail.value
