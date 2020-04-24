from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item): # Append expects value
        if len(self.storage) < self.capacity:
            self.storage.add_to_head(item)
            if len(self.storage) == 1:
                self.current = self.storage.head
            return
        if len(self.storage) == self.capacity:
            self.current.value = item
            if self.current.prev is not None:
                self.current = self.current.prev
            else:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        cur = self.storage.tail
        for i in range(0, len(self.storage)):
            list_buffer_contents.append(cur.value)
            cur = cur.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1


    def get(self):
        notNones = []
        for i in self.storage:
            if i is not None:
                notNones.append(i)
        return notNones