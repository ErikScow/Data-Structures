"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is not None:
            old_head = self.head
            new_node.next = old_head
            old_head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        return self.head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        removed = self.delete(self.head)
        return removed

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.tail is not None:
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
        else:
            self.head = new_node
        self.tail = new_node
        return self.tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        removed = self.delete(self.tail)
        return removed
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = self.delete(node)
        self.add_to_head(value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1

        value = node.value

        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next == None and node.prev == None:
            self.head = None
            self.tail = None
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        
        return value
                

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        value = current_node.value
        while current_node is not None:
            if current_node.value > value:
                value = current_node.value
            current_node = current_node.next
        return value