from helpers.CLIColor import CLIColor as color


class DFA:
    """
    The main class which stores and handles the basic logic for the dfa system
    """

    def __init__(self, nodes, table, symbols):
        self.nodes = nodes
        self.table = table
        self.symbols = symbols
        self.current_state = None
        self.final_states = []

    def initialize_state(self):
        """
        initialize the first node and the final nodes
        :return:
        :return:
        """
        for node in self.nodes:
            if node.is_first:
                self.current_state = node
            if node.is_final:
                self.final_states.append(node)

    def execute_dfa(self, word):
        """
        handle the logic for the dfa system
        :param word:
        :return:
        """
        word = self.split_word_to_array(word)
        print(color.UNDERLINE(f"Given word: {word}"))
        if not self.word_validity(word):
            print(color.RED("The given word contains unacceptable symbols for this DFA"))
            exit(0)

        for char in word:
            node_found = False
            for node in self.nodes:
                if node is self.current_state and not node_found:
                    node_found = True
                    for w in node.associated_nodes:
                        if str(w.state) == str(char):
                            self.current_state = self.get_node_by_input_state(w.next_state)

        if self.current_state in self.final_states:
            print(color.GREEN("Accepted word, good job!"))
        else:
            print(color.RED("Non accepted word, please try again!"))

    def word_validity(self, word):
        """
        checks the given word if is contained in the given symbols
        :param word:
        :return: Boolean
        """
        for w in word:
            if w not in self.symbols:
                return False
        return True

    def get_node_by_input_state(self, input_state):
        """
        Returns the node instance based on the given state
        :param input_state:
        :return: DFANode
        """
        for node in self.nodes:
            if str(node.input_state) == str(input_state):
                return node

        return None

    def split_word_to_array(self, word):
        """
        split the given word to an array of chars
        :param word:
        :return: Array of chars
        """
        splitted_word = []
        splitted_word[:0] = word
        return splitted_word

    def print_nodes(self):
        """
        print all the nodes (debug)
        :return:
        """
        for node in self.nodes:
            print(node)
            for n in node.associated_nodes:
                print(n)

    """
       nodes setter and getter
    """

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, nodes):
        self.__nodes = nodes

    @nodes.getter
    def nodes(self):
        return self.__nodes

    """
       table setter and getter
    """

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, table):
        self.__table = table

    @table.getter
    def table(self):
        return self.__table
