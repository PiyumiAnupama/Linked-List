import LinkedList

LinkedList=LinkedList.LinkedList()

LinkedList.printList()

print(" ")

LinkedList.searchValue(2)

print(" ")

LinkedList.addNodeBeginning(10)             # Add node head to the list
LinkedList.addNodeBeginning(20)

LinkedList.addNodeEnd(110)                  # Add node tail to the list

LinkedList.addNodeInPos(2,30)               # Add nodes given positions
LinkedList.addNodeInPos(3,40)
LinkedList.addNodeInPos(4,50)
LinkedList.addNodeInPos(5,60)
LinkedList.addNodeInPos(6,70)
LinkedList.addNodeInPos(2,80)
LinkedList.addNodeInPos(0,90)
LinkedList.addNodeInPos(1,100)

LinkedList.deleteFirstNode()                # Delete first Node
LinkedList.deleteLastNode()                 # Delete last Node
LinkedList.deleteNodeInPos(1)               # Delete nodes given positios

LinkedList.printList()

print(" ")

LinkedList.searchValue(30)

print(" ")
print("forward")
LinkedList.forward()                       # print forward

print(" ")
print("backward")
LinkedList.backward()                      # print backward



LinkedList.printList()


