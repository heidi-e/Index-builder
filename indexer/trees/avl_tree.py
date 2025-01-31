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

        if not node:
            return 0
    
        return node.height
    

    #This function is extremely important for the recursive portion of this indexer
    def _update_node_height(self, node: Optional[AVLNode]) -> None:
        
        #Indicating the height and then updating it after finding out the note exists. If it does not, nothing gets
        #updated
        if node:
            node.height = max(self._height(node.left), self._height(node.right)) + 1

        #No value gets updated
        else: 
            pass

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Performs a right rotation on the AVL tree.

        Args:
            y (AVLNode): The node to be rotated.

        Returns:
            AVLNode: The new root of the rotated subtree.
        """
        #Node to modify (will access its inner values)
        x = y.left 

        #Subtree present in the shift 
        other_section_right = x.right 

        #Rotating to make y a right child of x and the rest of the attached portion of the other branch a left child
        x.right = y
        y.left = other_section_right
        
        #Updating heights
        #Passed-in node
        self._update_node_height(y)
        #New root node of subtree
        self._update_node_height(x)
        
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Rotate the given node `x` to the left.
        Args:
            x (AVLNode): The node to be rotated.
        Returns:
            AVLNode: The new root of the subtree after rotation.
        """
        #Node to modify (will access its inner values)
        y = x.right

        #Subtree present in the shift
        other_section_left = y.left

        #Rotating to make y a right child of x and the rest of the attached portion of the other branch a left child
        y.left = x
        x.right = other_section_left
        
        #Updating heights
        #Passed-in node
        self._update_node_height(x)
        #New root node of subtree
        self._update_node_height(y)
        
        #As you may tell, this function is a mirror image of _rotate_right
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

        #Same recursive application as the one used for the binary search tree
        if not current:
            node = AVLNode(key)
            node.add_value(value)
            return node
        elif key < current.key:
            current.left = self._insert_recursive(current.left, key, value)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key, value)
        elif key == current.key:
            current.add_value(value)
            return current
    
        #Begin by modifying the height and then obtain the balance factor (which is -1, 0, or 1)
        self._update_node_height(current)
        #Balance factor equation: bal_fac = height of left branch - height of right branch
        bal_fac = self._height(current.left) - self._height(current.right)

        #Balancing of the tree
        #Case 1: Left-Left (LL) Case
        if bal_fac > 1 and key < current.left.key:
            return self._rotate_right(current)

        #Case 2: Right-Right (RR) Case
        if bal_fac < -1 and key > current.right.key:
            return self._rotate_left(current)

        #Case 3: Left-Right (LR) Case
        if bal_fac > 1 and key > current.left.key:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)

        #Case 4: Right-Left (RL) Case
        if bal_fac < -1 and key < current.right.key:
            current.right = self._rotate_right(current.right)
            return self._rotate_left(current)
        
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

    def _inorder_traversal(self, current: Optional[AVLNode], result: List[Any]) -> None:
        if current is None:
            return
        self._inorder_traversal(current.left, result)
        result.append(current.key)
        self._inorder_traversal(current.right, result)

    def get_keys_in_order(self) -> List[Any]:
        result = []
        self._inorder_traversal(self.root, result)
        return 