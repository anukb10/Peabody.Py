# Python program to find the second largest element
# in BST using reverse inorder traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper function to find the second largest element
def reverseInorder(root, count, result):
    
    # Base case: if root is null or we have already
    # found the second largest
    if root is None or count[0] >= 2:
        return

    # Traverse the right subtree first (reverse inorder)
    reverseInorder(root.right, count, result)

    # Increment the count of visited nodes
    count[0] += 1

    # If count becomes 2, then this is
    # the second largest element
    if count[0] == 2:
        result[0] = root.data
        return

    # Traverse the left subtree
    reverseInorder(root.left, count, result)

# Function to find the second largest element in BST
def findSecondLargest(root):
    count = [0]  
    result = [-1] 

    # Start reverse inorder traversal
    reverseInorder(root, count, result)

    return result[0]  

if __name__ == "__main__":
    
    # Representation of the input BST:
    #              7
    #             / \
    #            4   8
    #           / \   
    #          3   5 
    root = Node(7)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)

    secondLargest = findSecondLargest(root)

    print(secondLargest)