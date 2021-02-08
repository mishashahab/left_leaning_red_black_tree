# Creating a public class of RBTNode
class RBTNode:
    # This constructor takes one argument data key i.e. data to set the elements
    def __init__(self, key):

        self.key = key
        # Initialize Node pointers left and right
        self.left = None
        self.right = None
        # New node is always Red
        self.color = True
        # Red = True, Black = False
        self.Red = True
        self.Black = False

    # Traverse the Nodes in PostOrder
    # Perform action on left then right then currentNode
    def postOrder(self, output=None):
        if output is None:
            output = []

        if self.left:
            self.left.postOrder(output)

        if self.right:
            self.right.postOrder(output)
        output.append(self.key)

        return output

    # Traverse the Nodes in InOrder
    # Perform action on left then currentNode then Right
    def inOrder(self, output=None):
        if output is None:
            output = []

        if self.left:
            self.left.inOrder(output)

        output.append(self.key)

        if self.right:
            self.right.inOrder(output)

        return output

    # Traverse the Nodes in PreOrder
    # Perform action on currentNode then Left then Right
    def preOrder(self, output=None):
        if output is None:
            output = []

        output.append(self.key)
        if self.left:
            self.left.preOrder(output)

        if self.right:
            self.right.preOrder(output)

        return output


# Creating a private class of LeftLeaning
class LeftLeaning:

    def __init__(self):
        # Initialize root pointer
        self.root = None

    def insert(self, key):
        # Public function of insert
        if self.root is None:
            self.root = RBTNode(key)
        else:
            self.root = self.__insert(self.root, key)
            self.root.color = False

    def __insert(self, root, node):
        # Creating a private function of Insert
        if root is None:
            return RBTNode(node)
        if self.__isRed(root.left) and self.__isRed(root.right):
            self.flipColors(root)  # If both children are red, then parent node flip it's color
        if node < root.key:
            root.left = self.__insert(root.left, node)  # If new node is less than root node it will add on left side
        elif node > root.key:
            root.right = self.__insert(root.right,
                                       node)  # If new node is greater than root node it will add on right side
        if self.__isRed(root.right) and not self.__isRed(root.left):
            root = self.rotateLeft(root)  # If only right child is red, then parent node will rotate left
        if self.__isRed(root.left) and self.__isRed(root.left.left):
            root = self.rotateRight(
                root)  # If left child of node is red and also it's left child is red, then parent node will rotate right
        return root

    def rotateLeft(self, node):
        # This function rotates the nodes to it's left
        x = node.right
        node.right = x.left
        x.left = node
        x.color = x.left.color
        x.left.color = True  # Changing color of left node to red
        return x

    def rotateRight(self, node):
        # This function rotates the nodes to it's right
        x = node.left
        node.left = x.right
        x.right = node
        x.color = x.right.color
        x.right.color = True  # Changing color of right node to red
        return x

    def flipColors(self, node):
        # This function flips the color of node
        node.color = not node.color
        if node.left:
            node.left.color = not node.left.color
        if node.right:
            node.right.color = not node.right.color

    def isRed(self, node):
        # Check the color of Node is Red or not
        x = self.root
        while x.key is not None:
            if x.key == node:
                return x.color == True
            elif node < x.key:  # If the node is less than the root node then it will check towards left side
                x = x.left
            elif node > x.key:  # If the node is greater than the root node then it will check towards right side
                x = x.right
        return -1  # Else return -1

    def __isRed(self, node):
        # Private function to check, If node is none then return False means Black Color
        if node is None:
            return False
        return node.color == True

    def Search(self, node):
        # Public function to search node, Returns True if node is in tree.
        node = self._Search(self.root, node)
        if node:
            return True
        else:
            return False

    def _Search(self, root, node):
        # Private function of search
        if root is None:
            return None  # If root is none then tree is empty
        if root.key == node:
            return node  # If the desired node is equal to root node
        if node < root.key:
            return self._Search(root.left,
                                node)  # If the desired node is less than the root node then it will find towards left side
        else:
            return self._Search(root.right,
                                node)  # If the desired node is greater than the root node then it will find towards right side

    def fixUp(self):
        # Public function of fixup
        self.__fixUp(self.root)

    def __fixUp(self, current_node):
        # Private function of fixup, for fixing problems in tree
        if self.__isRed(current_node.right):
            current_node = self.rotateLeft(
                current_node)  # If the right child of given node is red then it will rotate left
        if self.__isRed(current_node.left) and self.__isRed(current_node.left.left):
            current_node = self.rotateRight(
                current_node)  # If left child of given node is red and also it's left child is red, then given node will rotate right
        if self.__isRed(current_node.left) and self.__isRed(current_node.right):
            self.flipColors(current_node)  # If both children of given node are red, then given node flip it's color
        return current_node

    def delete(self, val):
        # Public function to delete node by value
        if self.root is None:
            return None
        else:
            self.root = self._delete_node(self.root, val)

    def _delete_node(self, node, val):
        # Private function for desired node by rotations and color fliping to maintain balance of LLRBT
        if node is None:
            return node  # Return none if desired node is none
        if val < node.key:  # If the desired node is less than the root node then it will traverse towards left side
            if not self.__isRed(node.left) and not self.__isRed(
                    node.left.left):  # If left children of desired node are not red
                node = self._moveRedLeft(node)  # parent node of desired node will rotate left and also flip it's color
            node.left = self._delete_node(node.left, val)  # delete node
        else:  # else (val > node.key) If the desired node is greater than the root node then it will traverse towards right side
            if self.__isRed(node.left):
                node = self.rotateRight(node)  # If the left child of desired node is red then it will rotate right
            if val == node.key and node.right is None:  # If the value equals to node and right child of node is None
                return None  # None
            if node.right is None or (not self.__isRed(node.right) and not self.__isRed(node.right.left)):
                # If right child of desired node is none or If right child and it's left child of desired node is not red
                node = self._moveRedRight(
                    node)  # parent node of desired node will rotate right and also flip it's color
            if val == node.key:
                # If value is equal to the node in tree, it will search right and minimum right node and take place of desired node
                node.key = self._Search(node.right, self.__min(node.right))
                node.right = self._deleteMin(node.right)  # delete minimum right child
            else:  # else If desired node is not equal to the node in tree
                node.right = self._delete_node(node.right, val)  # delete minimum right child
        return self.__fixUp(node)  # Applying fixups

    def FindMax(self):
        # Public function to find maximum node
        x = self.__FindMax(self.root)
        if x.color:
            x.color = "Red"
        else:
            x.color = "Black"
        return x.key, x.color  # return node of maximum value and it's color

    def __FindMax(self, node):
        # Private function of find maximum
        if node.right is None:
            return node  # find the node on right side of root
        return self.__FindMax(node.right)  # tail recursion, return value of maximum node

    def FindMin(self):
        # Public function to find minimum node
        x = self.__FindMin(self.root)
        if x.color:
            x.color = "Red"
        else:
            x.color = "Black"
        return x.key, x.color  # return node of minimum value and it's color

    def __FindMin(self, root):
        # Private function of find mimimum
        if root.left is None:
            return root  # find the node on left side of root
        return self.__FindMin(root.left)  # tail recursion, return value of minimum node

    def _deleteMin(self, node):
        # private function to delete the minimum decendant.
        if node.left is None:
            return None  # If left node of minimum decendant is None, return None
        if not self.__isRed(node.left) and not self.__isRed(node.left.left):
            node = self._moveRedLeft(node)  # If children of left node is not red, red node will rotate left
        node.left = self._deleteMin(node.left)  # minimum left node will delete
        return self.__fixUp(node)  # Applying fixing up

    def _deleteMax(self, node):
        # private function to delete the maximum decendant.
        if self.__isRed(node.left):
            node = self.rotateRight(node)  # If left node of maximum decendant is red , node will rotate right
        if node.right is None:
            return None  # If left node of maximum decendant is None, return None
        if not self.__isRed(node.right) and not self.__isRed(node.right.left):
            node = self._moveRedRight(node)  # If left children of right node is not red, red node will rotate right
        node.left = self._deleteMax(node.left)  # minimum left node will delete
        return self.__fixUp(node)  # Applying fixing up

    def Successor(self):
        # Public function of successor
        x = self.__Successor(self.root)
        if x.color:
            x.color = "Red"
        else:
            x.color = "Black"
        return x.key, x.color  # Returns node and also it's color

    def __Successor(self, node):
        # Private function which returns the minimum node on left side of root
        if node.right is not None:
            return self.__FindMin(
                node.right)  # if right node of root is not none,finds the minimum node on right side of root
        suc = node.parent
        while node is suc.right and suc is not None:
            node = suc
            suc = suc.parent
        return suc  # returns the minimum node on right side of root

    def Predecessor(self):
        # public funtion of predecessor
        x = self.__Predecessor(self.root)
        if x.color:
            x.color = "Red"
        else:
            x.color = "Black"
        return x.key, x.color  # Returns node and also it's color

    def __Predecessor(self, node):
        # Private function which returns the maximum node on left side of root
        if node.left is not None:
            return self.__FindMax(node.left)  # if left node of root is not none,finds maximum node on left side of root
        pre = node.parent
        while node is pre.left and pre is not None:
            node = pre
            pre = node.parent
            return pre  # returns the maximum node on left side of root

    def __min(self, node):
        # private function to return the minimum node.
        while node.left is not None:
            node = node.left  # make bottom left node the desired node
        if node is None:
            return None  # If desired node is none, return none
        else:
            return node.key  # returns minimum node

    def __max(self, node):
        # private function to return the maximum node.
        while node.right is not None:
            node = node.right  # make bottom left node the desired node
        if node is None:
            return None  # If desired node is none, return none
        else:
            return node.key  # returns maximum node

    def _moveRedLeft(self, node):
        # private function to rotate red node to left
        self.flipColors(node)  # flips the color of node
        if node.right and self.__isRed(
                node.right.left):  # if the right node of desired node is not red and and it's left node is red
            node.right = self.rotateRight(node.right)  # right node of desired node will rotate right
            node = self.rotateLeft(node)  # desired node will rotate left
            self.flipColors(node)  # flips the color of node
        return node

    def _moveRedRight(self, node):
        # private function to rotate red node to right
        self.flipColors(node)  # flips the color of node
        if node.left and self.__isRed(
                node.left.left):  # if the left node of desired node is not red and and it's left node is red
            node = self.rotateRight(node)  # desired node will rotate right
            self.flipColors(node)  # flips the color of node
        return node

    def Print(self, root):
        # Public function to print node color
        if not self.isRed(root):
            print("Black", root)  # if is_Red function return false the color will be Black of desired node
        else:
            print("Red", root)  # if is_Red function return True the color will be Red of desired node


# Driver Code
leftredblack = LeftLeaning()
# Inserting nodes 45, 55, 15, 35, 25, 155, 99, 36
leftredblack.insert(45)
leftredblack.insert(55)
leftredblack.insert(15)
leftredblack.insert(35)
leftredblack.insert(25)
leftredblack.insert(155)
leftredblack.insert(99)
leftredblack.insert(36)
print("Print Nodes of Tree")
# Print nodes in inOrder traversal
print("Inorder", leftredblack.root.inOrder())
# Print nodes in postOrder traversal
print("PostOrder", leftredblack.root.postOrder())
# Print nodes in preOrder traversal
print("PreOrder", leftredblack.root.preOrder())
# Print the maximum value with color in LLRBT
print("Maximum Node", leftredblack.FindMax())
# Print the maximum value with color in LLRBT
print("Minimum Node", leftredblack.FindMin())
# Print the colors of respective nodes
print("Colors of the Desired Node")
leftredblack.Print(45)
leftredblack.Print(15)
leftredblack.Print(55)
leftredblack.Print(25)
# Delete the nodes of values 35, 155
leftredblack.delete(35)
leftredblack.delete(155)
print("Print Nodes of Tree after Deletion")
# Print nodes in inOrder traversal after deletion
print("InOrder", leftredblack.root.inOrder())
# Print nodes in postOrder traversal after deletion
print("PostOrder", leftredblack.root.postOrder())
# Print nodes in preOrder traversal after deletion
print("PreOrder", leftredblack.root.preOrder())
print("Successor")
# Print the minimum node on right side of root
print(leftredblack.Successor())
print("Predecessor")
# Print the maximum node on left side of root
print(leftredblack.Predecessor())
