from collections import deque

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            #Can also be used for duplicate prevention
            print('Could not insert, something went wrong')
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target > self.value:
                #Examine right
                if self.right is not None:
                    return self.right.contains(target)
                else:
                    return False
            elif target < self.value:
                #Examine left
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False
            else:
                #Whatchama-case
                return False #Cause screw this case

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
    
    def iterative_for_each(self, cb):
        stack = []

        stack.append(self)

        while len(stack) > 0:
            current_node = stack.pop()

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_iterative_for_each(self, cb):
        # Build a queue that intakes node
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)

            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        
        if self.left:
            self.left.in_order_print('wat')
            print(self.value)
        else:
            print(self.value)

        if self.right:
            self.right.in_order_print('wut')
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()
        q.append(node) # Add given node

        # Check Q should list a series of nodes of which needs
        # To have their children 'checked'
        # This is essentially an order designation mechanism to keep
        # The pointer from wandering into depth before clearing breadth
        # Whereas 'q' holds the final print ordering
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

            print(current_node.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []

        stack.append(self)

        # while len(stack) > 0:
        #     current_node = stack.pop()

        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)
        #     print(current_node.value)

        order = deque()

        order.append(node)
        while len(order) > 0:
            cur = order.pop()
            print(cur.value)
            if cur.right:
                order.append(cur.right)
            if cur.left:
                order.append(cur.left)