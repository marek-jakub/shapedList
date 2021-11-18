# Marek Jakub
# Text storing based on 3-D shape list evaluation.
# 2021

def index(letter, alphabet):
    insertion_index = -1
    for i in range(26):
        if alphabet[i] == letter.lower():
            insertion_index = i + 1

    return insertion_index


class ShapeList:
    def __init__(self):
        """ Initial size of the list is (shape_nodes + 1) * shape_nodes, first value in the
         list is the current size of the 3-D shape, then follows the alphabet. """
        # Number of containers is 26 + 2 (alphabet length + 2 containers holding alphabet
        # characters and letter load).
        self.containers = 27
        # Storing the 3-D shape size in this variable, redundant, as the information is stored
        # in the list at index 0 as well.
        self.shape_nodes = 27
        self.shape_list = list(None for _ in range((self.shape_nodes + 1) * self.shape_nodes))
        self.shape_list[0] = self.shape_nodes
        for i in range(1, self.shape_nodes, 1):
            self.shape_list[i] = chr(i + 96)
            self.shape_list[i + self.shape_nodes] = 0

    def is_empty(self):
        """ The load of inserted words for each letter reside at indices i + shape_size.
         If they are all 0, containers are empty (returns true). """
        is_empty = True
        for i in range(1, self.shape_nodes, 1):
            if self.shape_list[i + self.shape_nodes] != 0:
                is_empty = False
                break
        return is_empty
