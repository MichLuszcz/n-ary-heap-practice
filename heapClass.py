import math



class Heap:

    def __init__(self, n) -> None:
        self.arity = n
        self._internal_tab = []


    def get_parent(self, self_index):

        parent_index = math.ceil(self_index/self.arity) - 1
        # return self._internal_tab[parent_index]
        return parent_index

    def get_children_indices(self, parent_index):
        children_indices = []
        for child_number in range(1, self.arity+1):
            child_index = self.arity * parent_index + child_number
            if child_index < len(self._internal_tab):
                children_indices.append(child_index)
        return children_indices

    def pop(self):
        if self._internal_tab:
            last_index = len(self._internal_tab) - 1
            # swap max element (root) with the last element
            self.swap_at_indices(0, last_index)
            # remember the value and delete the last (now max) node
            return_value = self._internal_tab.pop()
            # heapify by pushing the root down until the heap property is satisfied
            self.heapify()
            return return_value



    def swap_at_indices(self, index_1, index_2):
        internal = self._internal_tab
        internal[index_1], internal[index_2] = internal[index_2], internal[index_1]

    def add(self, key, value):
        # # nie dodawanie duplikatu
        # if key in self._internal_tab:
        #     return
        internal = self._internal_tab
        self._internal_tab.append((key, value))
        current_index = len(self._internal_tab) - 1
        parent_index = self.get_parent(current_index)
        while (internal[current_index][0] > internal[parent_index][0]) and current_index != 0:
            self.swap_at_indices(parent_index, current_index)
            current_index = parent_index
            parent_index = self.get_parent(current_index)

    def heapify(self) -> None:
        # swap with larger child, until the child index exceeds the size of the array
        if self._internal_tab:
            current_index = 0
            children_indices = self.get_children_indices(current_index)
            while children_indices:
                largest = self._internal_tab[children_indices[0]][0] # the key of the first child
                largest_index = children_indices[0]
                # find the largest child to swap with
                for child_index in children_indices:
                    if self._internal_tab[child_index][0] > largest:
                        largest_index = child_index
                        largest = self._internal_tab[child_index][0]
                # swap with the largest child and update the position of the node
                # and get the new children
                self.swap_at_indices(current_index, largest_index)
                current_index = largest_index
                children_indices = self.get_children_indices(current_index)


    def node_to_string(self, node_index, indent=0, which_child = None) -> str:
        children_indices = self.get_children_indices(node_index)
        internal = self._internal_tab
        result = " " * indent + (f"{which_child}: " if which_child is not None else '')
        result += f"[{internal[node_index][0]}, {internal[node_index][1]}]\n"
        for child_number, child_index in enumerate(children_indices):
            result += self.node_to_string(child_index, indent+4, child_number + 1)
        return result


    def __str__(self) -> str:
        if self._internal_tab:
            return self.node_to_string(0)
        return ""