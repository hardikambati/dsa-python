import sys
from queue import Queue


# define constants here
MAX_QUEUE_SIZE=10


class Node:
    """
    creates a node with key, left, right values
    """
    def __init__(self, key: int):
        self.key=key
        self.left=None
        self.right=None


def insert(root: Node, key: int) -> Node:
    """
    inserts a new node in the tree
    will always traverse left, if empty node not found
    """
    new_node=Node(key)
    
    if root==None:
        root=new_node
        return root
    
    if root.left==None:
        root.left=new_node
    elif root.right==None:
        root.right=new_node
    else:
        return insert(root.left, key)
    
    return root


def print_preorder(root: Node) -> None:
    """
    prints tree in order - root, left, right
    """
    if root:
        print(root.key)
        print_preorder(root.left)
        print_preorder(root.right)


def print_inorder(root: Node) -> None:
    """
    prints tree in order - left, root, right
    """
    if root:
        print_inorder(root.left)
        print(root.key)
        print_inorder(root.right)


def print_postorder(root: Node) -> None:
    """
    prints tree in order - left, right, root
    """
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.key)


def BFS_traversal(root: Node) -> None:
    """
    does a level order traversal
    (prints all nodes level by level)
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    while(not q.empty()):
        item: Node=q.get()
        print(item.key)
        if item.left!=None:
            q.put(item.left)
        if item.right!=None:
            q.put(item.right)


def height(root: Node) -> int:
    """
    returns height of the tree
    """
    if root==None: return 0

    l_height=height(root.left)
    r_height=height(root.right)

    if l_height>r_height:
        return l_height+1
    else:
        return r_height+1
    

def insert_first_position_available(root: Node, key: int) -> None:
    """
    inserts a new node in the tree
    finds the first position available using BFS traversal
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    while(not q.empty()):
        item: Node=q.get()
        if item.left==None:
            item.left=Node(key)
            break
        elif item.right==None:
            item.right=Node(key)
            break
        else:
            q.put(item.left)
            q.put(item.right)


def inorder_successor(root: Node) -> Node:
    """
    returns the inorder successor node
    """
    temp=root
    while(root!=None and root.left!=None):
        temp=root.left
    return temp


def search_parent_node(root: Node, target: int) -> Node:
    """
    search the parent node of target child node
    """
    # if there is only one node, or target node is main root node
    if (root.left==None and root.right==None) or (root.key==target):
        return None
    
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    while(not q.empty()):
        item: Node=q.get()
        if item.left!=None:
            if item.left.key==target:
                return item
            q.put(item.left)
        if item.right!=None:
            if item.right.key==target:
                return item
            q.put(item.right)
    return None


def delete(root: Node, target: int) -> None:
    """
    deletes a node and replaces it with right most node
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)
    
    q.put(root)
    while(not q.empty()):
        item: Node=q.get()

        if item.key==target:
            successor_node=inorder_successor(root=root.right)
            right_most_parent_node: Node=search_parent_node(
                root=root,
                target=successor_node.key
            )
            item.key=successor_node.key
            # delete inorder successor
            right_most_parent_node.right=None
            break
        if item.left!=None:
            q.put(item.left)
        if item.right!=None:
            q.put(item.right)


def min_key(root: Node) -> int:
    """
    finds the minimum value node
    """
    if root==None: return sys.maxsize

    min_left=min_key(root.left)
    min_right=min_key(root.right)

    min_val=min(min_left, min_right)
    if min_val<root.key:
        return min_val
    return root.key


def search_node(root: Node, target: int) -> None:
    """
    checks whether a node exists or not
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    found=False

    while(not q.empty()):
        item: Node=q.get()
        if item.key==target:
            print(f'node with key {target} : found')
            found=True
        if item.left!=None:
            q.put(item.left)
        if item.right!=None:
            q.put(item.right)
    if found==False:
        print(f'node with key {target} : not found')


def left_view(root: Node) -> None:
    """
    prints the left view of tree
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    while(not q.empty()):
        q_size=q.qsize()
        counter=1

        while(counter<=q_size):
            item: Node=q.get()

            if counter==1:
                print(item.key)

            if item.left!=None:
                q.put(item.left)
            if item.right!=None:
                q.put(item.right)
            counter+=1


def leaf_nodes(root: Node) -> None:
    q=Queue(maxsize=MAX_QUEUE_SIZE)
    q.put(root)
    while(not q.empty()):
        item=q.get()
        if item.left==None and item.right==None:
            print(item.key)
        else:
            if item.left!=None:
                q.put(item.left)
            if item.right!=None:
                q.put(item.right)


def invert_tree(root: Node) -> None:
    """
    inverts the tree (mirror image)
    """
    if root==None: return

    invert_tree(root.left)
    invert_tree(root.right)

    if root!=None:
        temp=Node(None)
        temp=root.left
        root.left=root.right
        root.right=temp
        del temp


if __name__ == '__main__':

    # build your tree here
    root=insert(root=None, key=1)
    insert(root=root, key=2)
    insert(root=root, key=3)
    insert(root=root, key=4)
    insert(root=root, key=5)

    leaf_nodes(root=root)

    # left_view(root=root)

    # search_node(root=root, target=9)

    # delete(root=root, target=4)

    # BFS_traversal(root=root)

    # invert_tree(root=root)

    # print('-----')
    # BFS_traversal(root=root)
    # print(min_key(root=root))

    # q1=Queue(maxsize=10)
    # print(search_parent_node(root, q1, 1))

    # print_preorder(root=root)

    # tree_height=height(root=root)
    # print(tree_height)


    # insert_first_position_available(root=root, key=6)

    # print('----')
    # BFS_traversal(root=root, q=q2)
    # print_preorder(root=root)



