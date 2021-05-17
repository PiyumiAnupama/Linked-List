'''
RegNo           : AR/96447
ExamNo          : AF/18/14481
NameInitials    : Anupama P.G.P.
Purpose         : Doubly Linked List
Date            : 17.05.2021
'''


class Node:                             # Create a class for the Node
    def __init__(self):                 # Constructor
        self.data = None                # Create a variable named "data"
        self.next = None                # Create a variable named "Next"
        self.prev = None                # Create a variable named "prev"



    def setData(self, data):            # Set data of the Node
        self.data = data


    def getData(self):                  # Get data of this Node
        return self.data



    def setNext(self, next):            # Set next of the Node
        self.next = next



    def getNext(self):                  # Get next of this Node
        return self.next



    def hasNext(self):                  # Get if it has a Next
        return self.next is not None

    def setPrev(self, prev):            # Set previous of the Node
        self.prev = prev

    def getPrev(self):                  # Get Previous of this Node
        return self.prev

    def hasPrev(self):                  # Get if it has a previous
        return self.prev is not None
