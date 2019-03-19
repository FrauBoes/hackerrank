# Program to find highest sectional load in tree
# Sectional load = avg of values of root and all its children
# Helper code by PranchalK from GeeksForGeeks


# Function to create new tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


# Helper function to find node with highest sectional load recursively
def findHighestSectionalLoadUtil(r, ans):

    # If current node is None return 0 to parent node
    if r is None:
        return [0, 0]

    # Sectional load rooted at current node
    sum = r.value
    count = 1

    for n in r.children:
        current = findHighestSectionalLoadUtil(n, ans)
        sum += current[0]
        count += current[1]

    if count > 1 and sum/count > ans[0]:
        # Update answer if current section load is greater than answer so far
        ans[0], ans[1] = sum/count, r

    # Return current section load to its parent node
    return [sum, count]


# Function to find largest subtree sum.
def findHighestSectionalLoad(r):

    # If tree does not exist return 0
    if r is None:
        return [0, None]

    # Variable to store maximum subtree sum
    ans = [-999999999999, None]

    # Call to recursive function to find highest sectional load
    findHighestSectionalLoadUtil(r, ans)

    return ans


# Driver Code
if __name__ == '__main__':

    # Build test tree
    root = Node(20)
    root.children.append(Node(12))
    root.children.append(Node(18))
    root.children[0].children.append(Node(11))
    root.children[0].children.append(Node(2))
    root.children[0].children.append(Node(3))
    root.children[1].children.append(Node(15))
    root.children[1].children.append(Node(8))

    print(findHighestSectionalLoad(root))
