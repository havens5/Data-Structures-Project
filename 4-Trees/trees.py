class BST:

    class Node:
        
        # Each node of the BST will have data and links to the left and right sub-tree.

        def __init__(self, data):

            #Initialize the node to the data provided
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        #Initialize an empty BST.
    
        self.root = None

    def insert(self, data):

        if self.root is None: # if there isnt anything in the tree set the root to the new node
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
    
        if data == node.data:
            #print("already in list")
            pass
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __contains__(self, data):
        
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        
        if data == node.data:
            return True
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                return False
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                return False
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                 return self._contains(data, node.right)

    def __iter__(self):
    
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)  