class LinkedList:
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list
    def __str__(self):
        
        # Return a string representation of the linked list.
        
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    def insert_head(self, value):
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def insert_tail(self, value):
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
       
       # If the list is not empty, then only self.tail will be affected.
        else:
            new_node.prev = self.tail # Connect new node to the previous tail
            self.tail.next = new_node # Connect the previous tail to the new node
            self.tail = new_node      # Update the tail to point to the new node


    def insert_after_value(self, value, newNodeVal):
        # Create the new node
        new_node = LinkedList.Node(newNodeVal) 

        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    new_node.prev = self.tail # Connect new node to the previous tail
                    self.tail.next = new_node # Connect the previous tail to the new node
                    self.tail = new_node      # Update the tail to point to the new node
                else:
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node
                    return       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    def remove_head(self):
         
        #Remove the first node known as the head of the linked list.
        #If the list hos nothing inside of it
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def remove_tail(self):

        #Remove the last node (i.e. the tail) of the linked list.

        self.tail.prev.next = None
        self.tail = self.tail.prev


    def remove(self, value):
        #remove first node with the desired value
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.head: #check to see if it is the Head
                    curr.next.prev = None
                    self.head = curr.next
                    return #leave the loop when operation is complete on the desired value
                elif curr == self.tail: #check to see if it is the Tail
                    curr.prev.next = None
                    self.tail = curr.prev
                    return #leave the loop when operation is complete on the desired value
                else: # remove from the middle 
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    return #leave the loop when operation is complete on the desired value
            curr = curr.next

        
list = LinkedList()
list.insert_tail(5)
list.insert_head(4)
list.insert_head(3)
list.insert_head(2)
list.insert_head(1)
list.insert_after_value(3, 3.5)
list.insert_after_value(5, 6)
print(list)