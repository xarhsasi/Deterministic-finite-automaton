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

    """
        current_status setter and getter
    """

    @property
    def input_state(self):
        return self.__input_state

    @input_state.setter
    def input_state(self, input_state):
        self.__input_state = input_state

    @input_state.getter
    def input_state(self):
        return self.__input_state

    """
        is_first setter and getter
    """

    @property
    def is_first(self):
        return self.__is_first

    @is_first.setter
    def is_first(self, is_first):
        self.__is_first = is_first

    @is_first.getter
    def is_first(self):
        return self.__is_first

    """
        is_final setter and getter
    """

    @property
    def is_final(self):
        return self.__is_final

    @is_final.setter
    def is_final(self, is_final):
        self.__is_final = is_final

    @is_final.getter
    def is_final(self):
        return self.__is_final

    """
        associated_rows setter and getter
    """

    @property
    def associated_nodes(self):
        return self.__associated_nodes

    @associated_nodes.setter
    def associated_nodes(self, associated_nodes):
        self.__associated_nodes = associated_nodes

    @associated_nodes.getter
    def associated_nodes(self):
        return self.__associated_nodes

    def add_node(self, node):
        self.associated_nodes.append(node)

    def is_first_or_final_node(self):
        return self.is_final or self.is_final

    def __str__(self):
        return "<DFANode %s %s %s %s>" % (self.input_state, self.is_first, self.is_final, self.associated_nodes)
