# ArrayList of Linked-List because creating Linked List is much efficient than the Pure Linked List because indexing is fast in ArrayList, but all the other operations are slower
class Node:
    def __init__(self, data, top, down, left, right):
        self.data = data
        self.top = top
        self.down = down
        self.left = left
        self.right = right


class SkipList:
    def __init__(self):
        self.levels = []

    # insert operations core-most operation
    def insert(self, data):
        # checking if the data is already in the list, if so, throw the error
        for node in self.levels:
            if node.data == data:
                raise ValueError("Value already in the list, cannot insert again")

        # reading the levels
        for I in range(len(self.levels)):
            if self.levels[I] == None:
                new_node = Node(data, -1, 1, I,
                                self.levels[(I-1) if I!=0 else 0].data)
                self.levels[I] = new_node
                break
            if self.levels[I].data > data:
                new_node = Node(data, self.levels[I].data, 1, I,
                                self.levels[(I-1) if I!=0 else 0].data)
                self.levels[I:0] = [new_node]
                for k in range(I-2, -1, -1):
                    self.levels[k] = Node(self.levels[k+1].data, self.levels[k+2].data, 1, k,
                                          self.levels[(k - 1) if k != 0 else 0].data)
                self.align_list()
                return

        self.align_list()

    # remove function of the list operations
    def remove(self, data):
        None

    # Seaching function that searches for provided number
    def search(self, data):
        for I in range(len(self.levels)):
            if self.levels[I].data == data:
                return True, I
            if self.levels[I].data > data:
                return False, I
        return False, I

    # Aligns the created skip list
    def align_list(self):
        elements_list = []
        for I in range(len(self.levels)):
            str1 = []
            for j in range(len(self.levels)):
                str1.append(self.levels[j].data)
            elements_list.append(str1)

        #travels the each leaf and appar any none values with correct number
        for I in range(len(elements_list)):
            for j in range(len(elements_list[I])):
                if elements_list[I][j] is None:
                    for k in range(len(elements_list) - 1, I - 1, -1):
                        if elements_list[k][j] < elements_list[k + 1][j]:
                            elements_list[k][j] = elements_list[k + 1][j]
                        if elements_list[k][j] == elements_list[k + 1][j]:
                            break

    def print_complete_list(self):
        elements_list = []
        for I in range(len(self.levels)):
            str1 = []
            for j in range(len(self.levels)):
                str1.append(self.levels[j].data)
            elements_list.append(str1)
        return elements_list


n1 = Node(1, -1, 1, 0, 2)
n2 = Node(2, 1, 1, 1, 3)
n3 = Node(3, 2, 1, 2, 4)

sl = SkipList()
sl.levels = [n1, n2, n3]
print(sl.print_complete_list())
sl.insert(4)
print(sl.print_complete_list())
