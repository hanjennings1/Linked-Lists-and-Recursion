class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data  # the value this node holds
        self.next = None  # no connection yet — set when linked into a list


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None  # empty list: no nodes yet

    def insert_at_front(self, data):
        new_node = Node(data)      # create the node to insert
        new_node.next = self.head  # point it at the current first node
        self.head = new_node       # new node is now the front of the list

    def insert_at_end(self, data):
        """(Optional)"""
        new_node = Node(data)           # create the node to insert

        if self.head is None:           # special case: list is currently empty
            self.head = new_node        # new node becomes the only node, and the head
            return

        current = self.head             # start at the front
        while current.next:             # walk until 'current' is the LAST node (its .next is None)
            current = current.next
        current.next = new_node         # attach the new node after the last one


    # SUM OF LIST
    def recursive_sum(self):
        def _sum_helper(node):
            if node is None:                            # base case: nothing left to add
                return 0
            return node.data + _sum_helper(node.next)   # this node's value + sum of the rest

        return _sum_helper(self.head)                   # start the recursion at the front of the list

    # REVERSE LIST
    def recursive_reverse(self):
        def _reverse_helper(prev, current):
            if current is None:                         # base case: fell off the end
                return prev                             # 'prev' is the last node we touched — the new head

            next_node = current.next                    # save the rest of the list before we overwrite current.next
            current.next = prev                         # flip this node's arrow to point backward
            return _reverse_helper(current, next_node)  # move both pointers one step forward

        self.head = _reverse_helper(None, self.head)    # kick off with prev=None, current=head

    # SEARCH IN LIST
    def recursive_search(self, target):
        def _search_helper(node):
            if node is None:                   # base case 1: ran off the end, not found
                return False
            if node.data == target:            # base case 2: found it
                return True
            return _search_helper(node.next)   # otherwise, keep looking further down

        return _search_helper(self.head)       # start the search at the front of the list


    def display(self):
        values = []                             # collect each node's data as we go
        current = self.head                     # start at the front of the list
        while current:                          # keep going until we fall off the end (None)
            values.append(str(current.data))    # record this node's value
            current = current.next              # move to the next node
        print(" -> ".join(values) + " -> None") # join them into one readable line
