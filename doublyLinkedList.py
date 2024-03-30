# Doubly Linked List

class Node:
    """
    creates a node with data and next
    """
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None


class LinkedList:
    """
    Linked List class
    """

    def __init__(self):
        self.head=None
        self.tail=None

    
    def insert_end(self, data):
        """
        inserts a node at at end
        """
        new_node=Node(data)

        if (self.head == None and self.tail == None):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node

    
    def insert_start(self, data):
        """
        inserts a node at start
        """
        new_node=Node(data)

        if (self.head == None and self.tail == None):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node


    def insert_at_index(self, data, index: int):
        """
        inserts a node at a particular index
        """
        if (index == 0):
            self.insert_start(data)
            return

        new_node=Node(data)
        
        pos=0
        curr=self.head
        while(curr!=None and pos != index):
            curr=curr.next
            pos+=1

        if (curr == None):
            print(f'Invalid index passed : {index}')
            return
        
        prev_node=curr.prev
        # set prev node's next node to new_node
        prev_node.next=new_node

        # set new_node's prev to prev node 
        new_node.prev=prev_node
        
        # set current node's prev to new_node
        curr.prev=new_node

        # set new_node's next to current node
        new_node.next=curr


    def remove_first_node(self):
        """
        delete a node at first position
        """
        # no node
        if (self.head == None):
            return
        # single node
        if (self.head.next == None):
            self.head=None
            self.tail=None
            return
        
        self.head=self.head.next
        self.head.prev=None

    
    def remove_last_node(self):
        """
        delete a node at last position
        """
        # no node
        if (self.tail == None):
            return
        # single node
        if (self.tail.prev == None):
            self.head=None
            self.tail=None
        self.tail=self.tail.prev
        self.tail.next=None


    def remove_at_index(self, index: int):
        """
        remove a node at a particular index
        """
        # no node
        if (self.head == None):
            return
        # one node
        if (self.head.next == None):
            self.remove_first_node()
            return

        pos=0
        curr=self.head
        while(curr!=None and pos!=index):
            curr=curr.next
            pos+=1

        if (curr == None):
            print(f'Invalid index passed : {index}')
            return
        # first node to be deleted : de-link last node
        elif (curr.prev == None):
            self.head=curr.next
            self.head.prev=None
            curr.next=None
            return
        # last node to be deleted : de-link last node
        elif (curr.next == None):
            self.tail=curr.prev
            self.tail.next=None
            curr.prev=None
            return
        
        prev_node=curr.prev
        next_node=curr.next

        # connect prev and next node of curr node
        prev_node.next=next_node
        next_node.prev=prev_node

    
    def print_list(self, flow: str='forward'):
        """
        prints the data of each node
        :flow - ['forward', 'backward']
        """
        if (flow == 'backward'):
            curr=self.tail
            while(curr!=None):
                print(curr.data, end=' <-> ')
                curr=curr.prev
        else:
            curr=self.head
            while(curr!=None):
                print(curr.data, end=' <-> ')
                curr=curr.next


if __name__ == '__main__':

    l = LinkedList()

    l.insert_end(1)
    l.insert_end(2)
    l.insert_end(3)
    l.insert_end(4)
    l.insert_end(5)

    l.remove_at_index(10)
    # l.insert_at_index(9, 3)
    # l.remove_first_node()
    # l.remove_last_node()

    l.print_list()
