from typing import List, Optional, Any

from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.trees.avl_node import AVLNode

class AVLTreeIndex(BinarySearchTreeIndex):
    """
    An AVL Tree implementation of an index that maps a key to a list of values.
    AVLTreeIndex inherits from BinarySearchTreeIndex meaning it automatically
    contains all the data and functionality of BinarySearchTree.  Any
    functions below that have the same name and param list as one in 
    BinarySearchTreeIndex overrides (replaces) the BSTIndex functionality. 

    Methods:
        insert(key: Any, value: Any) -> None:
            Inserts a new node with key and value into the AVL Tree
    """
    
    def __init(self):
       super().__init__()
       self.root: Optional[AVLNode] = None 
    
    def _height(self, node: Optional[AVLNode]) -> int:
        """
        Calculate the height of the given AVLNode.

        Parameters:
        - node: The AVLNode for which to calculate the height.

        Returns:
        - int: The height of the AVLNode. If the node is None, returns 0.
        """
        
        # TODO: make sure to update height appropriately in the
        # recursive insert function.

        if not node:
            return 0
    
        return node.height
    

    def _update_node_height(self, node: Optional[AVLNode]) -> None:

        if not node:
            return 0
        
        #Indicating the height
        height = node.height

        #Updating height
        height = max(height(self._height(node.left), self._height(node.right))) + 1

        return height

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Performs a right rotation on the AVL tree.

        Args:
            y (AVLNode): The node to be rotated.

        Returns:
            AVLNode: The new root of the rotated subtree.
        """
        
        # TODO: implement the right rotation for AVL Tree

        #Node to modify (will access its inner values)
        x = y.left 

        #Subtree present in the shift 
        other_section_right = x.right 

        #Rotating to make y a right child of x and the rest of the attached portion of the other branch a left child
        x.right = y
        x.left = other_section_right


        

        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Rotate the given node `x` to the left.
        Args:
            x (AVLNode): The node to be rotated.
        Returns:
            AVLNode: The new root of the subtree after rotation.
        """
        
        # TODO: implement the left rotation for AVL Tree

        y = x.right

        #Subtree present in the shift
        other_section_left = y.left
        
        return y

    def _insert_recursive(self, current: Optional[AVLNode], key: Any, value: Any) -> AVLNode:
        """
        Recursively inserts a new node with the given key and value into the AVL tree.
        Args:
            current (Optional[AVLNode]): The current node being considered during the recursive insertion.
            key (Any): The key of the new node.
            value (Any): The value of the new node.
        Returns:
            AVLNode: The updated AVL tree with the new node inserted.
        """
        # TODO: Implement a proper recursive insert function for an
        # AVL tree including updating height and balancing if a
        # new node is inserted. 
        
        # TODO: Remove or comment out this line once you've implemented
        # the AVL insert functionality 
        current = super()._insert_recursive(current, key, value)
 
        return current

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the AVL tree. If the key exists, the
         value will be appended to the list of values in the node. 

        Parameters:
            key (Any): The key to be inserted.
            value (Any): The value associated with the key.

        Returns:
            None
        """
        if self.root is None:
            self.root = AVLNode(key)
            self.root.add_value(value)
        else:
            self.root = self._insert_recursive(self.root, key, value)

    # def _inorder_traversal(self, current: Optional[AVLNode], result: List[Any]) -> None:
    #     if current is None:
    #         return
        
    #     self._inorder_traversal(current.left, result)
    #     result.append(current.key)
    #     self._inorder_traversal(current.right, result)
   
    # def get_keys(self) -> List[Any]:
    #     keys: List[Any] = [] 
    #     self._inorder_traversal(self.root, keys)
    #     return keys