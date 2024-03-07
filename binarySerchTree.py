import sys
from queue import Queue


# define constants here
MAX_QUEUE_SIZE=10


class Node:
    """
    creates a node with key, left, right values
    """
    def __init__(self, key: int=None):
        self.key=key
        self.left=None
        self.right=None


def insert(root: Node, key: int) -> Node:
    """
    inserts a new node in the tree
    """
    if root==None:
        return Node(key)
    
    if key<root.key:
        root.left=insert(root.left, key)
    elif key>root.key:
        root.right=insert(root.right, key)
    return root


def print_preorder(root: Node) -> None:
    """
    root, left, right
    """
    if root!=None:
        print(root.key)
        print_preorder(root.left)
        print_preorder(root.right)


def print_inorder(root: Node) -> None:
    """
    left, root, right
    """
    if root!=None:
        print_inorder(root.left)
        print(root.key)
        print_inorder(root.right)


def print_postorder(root: Node) -> None:
    """
    left, right, root
    """
    if root!=None:
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

def inorder_successor(root: Node, target: int) -> None:
    """
    returns the inorder successor node of a particular node
    """
    target_node=search_node(root=root, target=target)
    if target_node!=None:
        if target_node.right!=None:
            temp: Node=target_node.right
            while(temp.left!=None):
                temp=temp.left
            return temp
    return None


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
    deletes a node and replaces it with inorder successor
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    while(not q.empty()):
        item: Node=q.get()
        
        if item.key==target:
            successor_node: Node=inorder_successor(root=root, target=target)

            if successor_node!=None:
                # if successor node exists
                parent_node=search_parent_node(
                    root=root,
                    target=successor_node.key
                )
                
                item.key=successor_node.key

                if parent_node.left.key==successor_node.key:
                    parent_node.left=None
                elif parent_node.right.key==successor_node.key:
                    parent_node.right=None
            else:
                # if no successor node, it means the right child is empty
                # thus, replace the left sub tree with target node
                
                # first, find the parent node of target node
                parent_node=search_parent_node(
                    root=root,
                    target=target
                )

                # now, replace the parent node's left or right node 
                # with left sub tree of target node
                if parent_node.left.key==target:
                    parent_node.left=item.left
                    del item
                    break
                elif parent_node.right.key==target:
                    parent_node.right=item.left
                    del item
                    break
        
        if item.left!=None:
            q.put(item.left)
        if item.right!=None:
            q.put(item.right)


def search_node(root: Node, target: int) -> Node:
    """
    checks whether a node exists or not
    """
    if root==None:
        return None
    if root.key==target:
        return root
    if target<root.key:
        if root.left!=None:
            return search_node(root.left, target)
        return None
    elif target>root.key:
        if root.right!=None:
            return search_node(root.right, target)
        return None


def min_key(root: Node) -> None:
    """
    finds the minimum value node
    """
    temp=root
    while(temp.left!=None):
        temp=temp.left
    print(temp.key)


def left_view(root: Node) -> None:
    """
    prints the left view of tree
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    while(not q.empty()):
        counter=1
        q_size=q.qsize()

        while(counter<=q_size):
            item=q.get()

            if counter==1:
                print(item.key)
                
            if item.left!=None:
                q.put(item.left)
            if item.right!=None:
                q.put(item.right)
            counter+=1


def leaf_nodes(root: Node) -> None:
    """
    prints the leaf nodes of a tree
    """
    q=Queue(maxsize=MAX_QUEUE_SIZE)

    q.put(root)
    while(not q.empty()):
        item: Node=q.get()

        if item.left==None and item.right==None:
            print(item.key)
        
        if item.left!=None:
            q.put(item.left)

        if item.right!=None:
            q.put(item.right)


def invert_tree(root: Node) -> None:
    """
    inverts the tree (mirror image)
    NOTE: when a binary search tree is inverted,
          it's no more a binary search tree.
          It becomes a normal binary tree.
    """
    
    if root==None: return

    invert_tree(root.left)
    invert_tree(root.right)

    if root!=None:
        temp=root.left
        root.left=root.right
        root.right=temp
        del temp


if __name__ == '__main__':

    # build your tree here
    root=insert(root=None, key=30)
    insert(root=root, key=20)
    insert(root=root, key=10)
    insert(root=root, key=25)
    insert(root=root, key=40)
    insert(root=root, key=35)
    insert(root=root, key=50)
    insert(root=root, key=31)    
    insert(root=root, key=37)


    BFS_traversal(root=root)  


    # left_view(root=root)

    # invert_tree(root=root)

    # BFS_traversal(root=root)
    # delete(root=root, target=40)
    # print('-------')
    # BFS_traversal(root=root)  

    # leaf_nodes(root=root)

    # min_key(root=root)

    # target=10
    # if (search_node(root=root, target=target)):
    #     print(f'{target} found')
    # else:
    #     print(f'{target} not found')

