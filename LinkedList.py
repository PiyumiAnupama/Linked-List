from Node import Node                               # import Node


class LinkedList:                                   # Create a class for the linked list
    def __init__(self):                             # Constructor
        self.head = None                            # Initally there are no elements in the list
        self.length = 1

    def listLength(self):                           # Create a length function
        current = self.head                         # Create a variable named current and  it start in the head of the list
        count = 0                                   # Create a variable named count
        while current is not None:                  # while current is not none
            count = count + 1                       # count length
            current = current.getNext()             # current variable is linked next value
        return count


    def printList(self):                            # Create a print function
        if self.head is None:                       # Check whether list is empty or not
            print('Empty Linked List')
        else:                                       # if list is not empty
            current = self.head                     # current variable assigned to self.head
            while current is not None:              # while current is not none
                print(current.getData())            # print current value
                current = current.getNext()         # current is equal to current.next


    def addNodeBeginning(self, data):               # Insert an item - Beginning

        newNode = Node()                            # Create the new Node
        newNode.setData(data)                       # pass the data to  the new node

                                                    # At to the Beginning
        if self.head is None:                       # If list is empty
            self.head = newNode                     # New Node become a new head
        else:                                       # If list isn"t empty
            newNode.setPrev(None)                   # head has not previous
            newNode.setNext(self.head)              # old head is set to new head's next
            self.head.setPrev(newNode)
            self.head = newNode                     # new node assigned as self.head
        self.length += 1                            # count length


    def addNodeEnd(self, data):                     # Insert an item - End

        newNode = Node()                            # Create the new Node
        newNode.setData(data)                       # pass the data to  the new node

                                                    # At to the End
        if self.head is None:                       # If list is empty
            self.head = newNode                     # New Node become a new head
        else:                                       # If list isn"t empty. change the pointers accordingly.
            current = self.head                     # current variable is assigned as self.head
            while current.getNext() is not None:    # while current.next is not none
                                                    # Loop breaks when it reaches last element
                current = current.getNext()         # current is equal to next node
            current.setNext(newNode)                # current.next is become a new node
            newNode.setPrev(current)                # current node set for the new node's previous
            newNode.setNext(None)                   # new node next is none
        self.length += 1                            # count length


    def addNodeInPos(self, pos, data):              # Insert an item - Given Position

        if pos > self.length - 1 or pos < 0:
            return None
        elif pos == 0:                              # if position is zero add node beginning
            self.addNodeBeginning(data)
        elif pos == self.length - 1:                # add node end
            self.addNodeEnd(data)
        else:
            newNode = Node()                        # Create the new Node
            newNode.setData(data)                   # pass the data to  the new node
            count = 0                               # get count
            current = self.head                     # current variable is assigned as self.head

            while count != pos - 1:                 # while count is not equal pos
                count += 1                          # count is equal to count plus one
                current = current.getNext()         # current is equal to next node

            newNode.setNext(current.getNext())      # set current next to new node
            newNode.setPrev(current)                # current node set for the new node's previous

            current.setNext(newNode)                # current.next is become a new node
        self.length += 1                            # count length



    def deleteFirstNode(self):                       # Delete first Node
        if self.head is None:                        # if list is empty
            print("Empty Linked List")
        else:                                        # if list is not empty
            self.head = self.head.getNext()          # self.head equal to next
            self.head.setPrev(None)                  # head has not previous
        self.length -= 1


    def deleteLastNode(self):                       # Delete Last Node
        if self.head is None:                       # if list is empty print that statement
            print("Empty Linked List")
        else:                                       # if list is not empty
            current = self.head                     # current variable is assigned as self.head
            previous = None
            while current.getNext() is not None:    # while current.next node is not none
                previous = current                  # previous equal to current
                current = current.getNext()         # current is equal to next node
            previous.setNext(None)                  # delete current node
        self.length -= 1


    def deleteNodeInPos(self, pos):                 # Delete given Position
        if self.head is None:                       # if list is empty print that statement
            print("Empty Linked List")
            return None
        if self.length > pos > -1:
            if pos == 0:                            # if position is equal to zero
                self.deleteFirstNode()              # delete first node
            elif pos == self.length - 1:            # if position is equal to self.length-1
                self.deleteLastNode()               # delete last node
            else:
                count = 0
                current = self.head                 # current variable is assigned as self.head
                while count != pos - 1:             # while count is not equal to position -1
                    count += 1                      # count is equal to count plus one
                    current = current.getNext()     # current is equal to current.next node
                deletingNode = current.getNext()    # delete current.getNext node
                nextNode = deletingNode.getNext()   # nextNode is equal to deletingNode.getNext
                nextNode.setPrev(current)           # set previous node
                current.setNext(nextNode)           # set next node
            self.length -= 1

    def forward(self):                              # Traversing Forward
        if self.head is None:                       # if list is empty print that statement
            print("Empty list")
            return
        else:
            current = self.head                     # current variable is assigned as self.head
            while current is not None:              # while current is not none
                print(current.data)                 # print current value
                current = current.next              # current is equal to current.next



    def backward(self):                             # Traversing Backward
        if self.head is None:                       # if list is empty print that statement
            print("Empty List")
        else:
            first = self.head                       # first variable is assigned as self.head
            second = first.next                     # second variable is assigned as first.next
            first.next = None                       # first.next is equal to none
            first.prev = second                     # first.previous is assigned as second

            while second is not None:               # print backward
                second.prev = second.next
                second.next = first
                first = second
                second = second.prev
                self.head = first


    def searchValue(self, data):                    # Search possition
      current=self.head                             # current variable is assigned as self.head
      count=1

      while current:
          if current.data==data:                    # if current is equal to "data" print position
              print("Element {} found at {}\'th possition.".format(data,count))
              return
          else:                                     # if current is not equal to "data" print element is not found
              count+=1
              current=current.getNext()
      print("Element {} not found ".format(data))
