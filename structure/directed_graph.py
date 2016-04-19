class DirectedGraph:
    def __init__(self):
        self.adjacancy_dict = {}

    def add_edge(self, vrtx1, vrtx2):
        if vrtx1 not in self.adjacancy_dict:
            self.adjacancy_dict[vrtx1] = []
        self.adjacancy_dict[vrtx1].append(vrtx2)

    def siblings(self, vrtx):
        if vrtx not in self.adjacancy_dict:
            return []
        return self.adjacancy_dict[vrtx]
