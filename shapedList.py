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

    def insert(self, item):
        """ Inserts an item at the range of indices which account for a given first letter
         of the item. Returns False if the insertion is not successful. """
        inserted = False
        insertion_index = index(item[0], self.shape_list[1:27])

        if insertion_index != -1:
            letter_load = self.shape_list[insertion_index + self.shape_nodes]
            # If the load of the sublist is getting close to the size of the 3-D shape,
            # i.e. soon to be filled in, it needs to be enlarged. The difference is
            # arbitrary, currently it is 5.
            if self.shape_nodes - letter_load < self.shape_nodes - (self.shape_nodes - 5):
                increased_by = self.shape_nodes // 2
                increase_list = list(None for _ in range(increased_by))
                # It has to be performed from the end of the list to correctly point to
                # empty parts of containers.
                for i in range(self.containers, -1, -1):
                    self.shape_list[(self.shape_nodes * i) + self.shape_nodes:
                                    (self.shape_nodes * i) + self.shape_nodes] = increase_list
                self.shape_nodes += increased_by
                self.shape_list[0] = self.shape_nodes

            # After checking the load for the letter, the word can be inserted.
            letter_start_index = (insertion_index + 1) * self.shape_nodes
            if letter_load < self.shape_nodes and \
                    self.shape_list[letter_start_index + letter_load] is None:
                self.shape_list[letter_start_index + letter_load] = item
                self.shape_list[insertion_index + self.shape_nodes] += 1
                inserted = True

        return inserted

    def search(self, item):
        """ Returns the index of the item if found, otherwise returns -1. The search
         is linear, if found, the index marks the first item found. """
        item_index: int = -1
        search_index = index(item[0], self.shape_list[1:27])

        letter_load = 0
        if search_index != -1:
            letter_load = self.shape_list[search_index + self.shape_nodes]

        if letter_load != 0:
            i = (search_index + 1) * self.shape_nodes
            found = False
            while i < ((search_index + 1) * self.shape_nodes) + self.shape_nodes and not found:
                if self.shape_list[i] == item:
                    found = True
                    item_index = i
                i += 1

        return item_index
