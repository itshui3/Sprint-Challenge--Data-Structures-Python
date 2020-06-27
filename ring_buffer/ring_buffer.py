from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None
        # what is current? How should I use it?
        # what if I make current the last placed node

    def append(self, item1):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item1)
            self.current = self.storage.tail

        elif len(self.storage) == self.capacity:
            if self.current.next is None:
                self.current = self.storage.head
            else:
                self.current = self.current.next

            self.current.value = item1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        prev_cur = self.current
        self.current = self.storage.head
        for i in range(len(self.storage)):
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next

        self.current = prev_cur

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.current = len(self.storage) - 1
            # leaves off on the item I just changed

        elif self.capacity == len(self.storage):
            if self.current == len(self.storage) - 1:
                self.current = 0
                self.storage[self.current] = item
            elif self.current < len(self.storage) - 1:
                self.current += 1
                self.storage[self.current] = item



    def get(self):
        return self.storage
