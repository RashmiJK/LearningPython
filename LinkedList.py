# Linked List example


# the node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        set.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1


    def find(self,val):
        # find the first item with a given value
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

def main():
    # create a linked list and insert some items
    myitemlist = LinkedList()
    myitemlist.insert(38)
    myitemlist.insert(49)
    myitemlist.insert(13)
    myitemlist.insert(15)
    myitemlist.dump_list()

    # exercise the list
    # print("Item count: ", myitemlist.get_count())
    # print("Finding item: ", myitemlist.find(13))
    # print("Finding item: ", myitemlist.find(78))

    # delete an item
    myitemlist.deleteAt(3)
    print("Item count: ", myitemlist.get_count())
    print("Finding item: ", myitemlist.find(38))
    myitemlist.dump_list()


if __name__ == "__main__":
    main()