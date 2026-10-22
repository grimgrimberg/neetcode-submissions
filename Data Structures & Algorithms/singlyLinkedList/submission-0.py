from typing import List

class ListNode:
    """A helper class representing a single node in the linked list."""
    def __init__(self, val: int):
        self.val = val      # Holds the data integer
        self.next = None    # Points to the next node (starts as None)

class LinkedList:
    
    def __init__(self):
        # Initialize an empty list
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        # If index is out of bounds, return -1
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        # Loop "index" times to walk to the right node
        for _ in range(index):
            current = current.next
            
        return current.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        
        # Point the new node to the old head
        new_node.next = self.head
        # Make this new node the new head
        self.head = new_node
        
        # If the list was completely empty, this new node is ALSO the tail
        if self.size == 0:
            self.tail = new_node
            
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        
        # If the list is empty, inserting at tail is the exact same as inserting at head
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # Connect the old tail's next pointer to the new node
            self.tail.next = new_node
            # Move the tail pointer to our new node
            self.tail = new_node
            
        self.size += 1

    def remove(self, index: int) -> bool:
        # If index is out of bounds, we cannot remove anything
        if index < 0 or index >= self.size:
            return False
            
        # Case 1: Removing the head node (index 0)
        if index == 0:
            self.head = self.head.next
            # If the list only had 1 item, updating the head means tail must also become None
            if self.size == 1:
                self.tail = None
                
        # Case 2: Removing a node anywhere else
        else:
            current = self.head
            # Stop right BEFORE the node we want to delete (at index - 1)
            for _ in range(index - 1):
                current = current.next
            
            # Skip over the deleted node by pointing to its next element
            current.next = current.next.next
            
            # If we just deleted the very last node, update our tail pointer
            if index == self.size - 1:
                self.tail = current
                
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        
        # Walk through every single node until we hit None
        while current is not None:
            values.append(current.val)
            current = current.next
            
        return values
