'''Stack using linked list'''
class Node:
    '''Defining class Node'''
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Stack:
    '''Defining class Stack'''
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    def push(self, item):
        '''Inserting data into the stack'''
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.size += 1
    def pop(self):
        '''Removing data from the stack'''
        data_pop = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data_pop
    def peek(self):
        '''Finding the top element of the stack'''
        temp = self.head
        return temp.data
    def is_Empty(self):
        '''To check whether the stack is empty or not'''
        if self.size == 0:
            return True
        else: 
            return False
    def size_of_stack(self):
        '''To check the size of the stack'''
        return self.size
    def print_Stack(self):
        '''To print the stack'''
        current = self.head
        while current != None:
            print("-->", current.data, end="")
            current = current.next
        print('\n')
STACK = Stack()
STACK.push(10)
STACK.push(20)
STACK.push(30)
STACK.push(40)
print(STACK.peek())
STACK.pop()
STACK.print_Stack()
STACK.size_of_stack()
print(STACK.peek())
