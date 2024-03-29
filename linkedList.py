# Single LinkedList

class Node:
    """
    creates a node with data and next
    """
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:
    """
    LinkedList class
    """
    
    def __init__(self):
        self.head=None

    
    def insert_end(self, data) -> None:
        """
        insert node at end
        """
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            return

        last_node=self.head
        while(last_node.next!=None):
            last_node=last_node.next
        
        last_node.next=new_node


    def insert_start(self, data) -> None:
        """
        insert node at end
        """
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            return
        
        new_node.next=self.head
        self.head=new_node


    def insert_at_index(self, data, index) -> None:
        """
        inserts a node at a particular index
        """
        new_node=Node(data)
        curr=self.head
        pos=0
        if pos == index:
            self.insert_start(data)
        else:
            while(curr!=None and pos+1 != index):
                pos+=1
                curr=curr.next
            
            if curr!=None:
                new_node.next=curr.next
                curr.next=new_node
            else:
                print(f'Invalid index passed : {index}')


    def find_node(self, value) -> None:
        """
        finds and prints whether node was found or not
        """
        curr=self.head
        while(curr.next!=None):
            if curr.data==value:
                print(f'found : {value}')
                return
            curr=curr.next
        print(f'not found : {value}')

    
    def remove_first_node(self) -> None:
        if self.head == None:
            return
        self.head=self.head.next


    def remove_last_node(self) -> None:
        if self.head == None:
            return
        
        sec_last=self.head
        while(sec_last.next.next!=None):
            sec_last=sec_last.next
        
        del sec_last.next.next
        sec_last.next=None


    def remove_at_index(self, index) -> None:
        """
        remove node at a particular index
        """
        pos=0
        curr=self.head
        if pos == index:
            self.remove_first_node()
        else:
            while(curr!=None and pos+1 != index):
                pos+=1
                curr=curr.next
            
            if curr!=None:
                curr.next=curr.next.next
            else:
                print(f'Invalid index passed : {index}')


    def print_list(self) -> None:
        """
        prints the data of each node
        """
        curr=self.head
        while(curr!=None):
            print(curr.data)
            curr=curr.next


    def size_of(self) -> None:
        if self.head == None:
            print(f'total nodes : 0')
            return

        count=1
        curr=self.head
        while(curr.next!=None):
            curr=curr.next
            count+=1
        print(f'total nodes : {count}')
        

    def bubble_sort(self) -> None:
        swapped=True
        while(swapped):
            swapped=False
            curr=self.head

            while(curr!=None and curr.next!=None):
                if curr.data > curr.next.data:
                    temp=curr.next.data
                    curr.next.data=curr.data
                    curr.data=temp
                    swapped=True
                curr=curr.next


    def mid_node(self, start: Node, last: Node=None) -> Node:
        """
        returns the middle node in range [start, last] nodes
        """
        if start == None:
            return None
        
        slow=start
        fast=start.next

        while(fast != last):
            fast=fast.next
            
            if (fast != last):
                slow=slow.next
                fast=fast.next
        return slow


    def binarySearch(self, target) -> None:
        """
        does a binary search for finding a target
        """
        if (self.head.data == target):
            print(f'found {target}')
            return

        start=self.head
        last=None

        while(True):
            # find mid
            mid=self.mid_node(start=start, last=last)

            if (target == mid.data):
                print(f'found : {target}')
                break

            if (target > mid.data):
                start=mid.next
            elif (target < mid.data):
                last=mid

            if (start == last):
                print(f'not found : {target}')
                break


if __name__ == '__main__':

    l = LinkedList()

    l.insert_end(1)
    l.insert_end(2)
    l.insert_end(3)
    l.insert_end(4)
    l.insert_end(5)

    l.print_list()
    l.binarySearch(12)

    # print(l.mid_node(l.head).data)

    # l.remove_last_node()
    # l.insert_at_index(9, 5)
    # l.remove_at_index(4)
    # l.bubble_sort()
    # l.size_of()
