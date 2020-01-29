class DFANode:
    """
    DFA Node class which represents each DFA Node
    """

    def __init__(self, input_state, is_first, is_final):
        """
        :param input_state:
        :param is_first:
        :param is_final:
        """
        self.input_state = input_state
        self.is_first = is_first
        self.is_final = is_final
        self.associated_nodes = []

    def add_node(self, node):
        self.associated_nodes.append(node)

    def is_first_or_final_node(self):
        return self.is_final or self.is_final

    def __str__(self):
        return "<DFANode %s %s %s %s>" % (self.input_state, self.is_first, self.is_final, self.associated_nodes)
