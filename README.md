# left_leaning_red_black_tree
Left Leaning Red Black Tree:
Left Leaning Red Black Tree is a self balancing binary search tree.
It provide time complexity O(logN) for insertion, deletion and search.
We can represent 2-3-4 trees as a binary search tree using internal red edges for 3 and 4 nodes but 3 nodes must be left leaning.
It is easy to implement as compare to Red Black Tree.

Properties:
Every node can be red or black.
Use recursive implementation.
All nulls are black.
When we insert a new node its color is always red and change its color according to situation.
If a node is red then both of its children must be black.

Overview:
Insertion in Left Leaning Red Black Tree
If the value of new node is greater than root node then it will add on right side. Similarly if the value of new node is less than root node then it will add on left side.
If both children of parent node are red then color of the parent node will flip its color to black.
If right child of root is Red and left child of root is not Red so when we insert the new node the root node will rotate at left side.
If left child of root node is Red and the further left child of that child is Red then the Root node will rotate right while inserting the new node.

Deletion in Left Leaning Red Black Tree
When value is less than the root node:
If the desired value is less than the root node then it will traverse the left child as well as its left child.
If these children are not Red then it will rotate left and flip their color to Red and delete the desired node.
If the desired node has a red left node then it will rotate right to delete the desired node.

When value is greater than the root node:
If the desired value is greater than the root node then it will traverse the right side of the root.
If the right child and it left child are not Red then it will rotate right and flip their color to Red and delete the desired node.
If the right child of the desired node is None then it will delete the node and return None.
If both right and left child of the desired node are not Red then it will move to the right and flip their color to Red and delete the desired node.

Fixing up
If the right child of current node is Red then it will rotate left.
If the left child of current node is Red and also the left child of that child is Red then current node will rotate Right.
If the left and right child of current node are Red the current node will flip its color to Black.

Searching
If there is no root node then it will return None while searching.
If root is equal to the desired value then it will return root node.
If node is less than the root node then it will traverse at the left side and if node is greater than the root node then it will traverse at the right side of the root node and if that value is present then it will return True otherwise False.


