class Node:
#'Like a pocket to hold data'
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
    #"""Return a string representation of this node."""
        return '{!r}'.format(self.data)

class Linked_list:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
    #"""Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None
        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            self.head = previous_node

    # Find out if Linked_list is empty
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    # add data if linked list is empty
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def find(self, data):
        current_node = self.head
        while current_node.data != data:
            if current_node == None:
                return None

            current_node = current_node.next

        return current_node.data

    def items(self):
    #Return a list (dynamic array) of all items in this linked list.
    #Best and worst case running time: O(n) for n items in the list (length)
    #because there is always a need to loop through all n nodes to get each item.
        items = []

        node = self.head

        while node is not None:

            items.append(node.data)

            node = node.next

        return items


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
ll = Linked_list()
print(ll)
ll.append(node1)
print(ll)
ll.append(node2)
print(ll)
ll.append(node3)
print(ll)
ll.reverse()
print(ll)
print(ll.head)