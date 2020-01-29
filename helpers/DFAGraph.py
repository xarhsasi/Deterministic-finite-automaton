from graphviz import Digraph
from helpers.CLIColor import CLIColor as color


class DFAGraph:
    """
    class which initializes and creates a pdf file with the dfa representation
    """

    def __init__(self, nodes=None, prefix="q"):
        """
        Initializes the variables
        :param: table
        """
        # self.table = table
        self.nodes = nodes
        self.prefix = prefix
        self.f = None

    def initialize_graph(self):
        """
        Function which initializes and calculates all the nodes based on the created table
        :return: Shows the pdf with the dfa
        """
        try:
            self.f = Digraph('finite_state_machine', filename='fsm.gv')
            self.f.attr(rankdir='q', size='8,5')

            for n in self.nodes:
                self.f.attr('node', shape='doublecircle')
                if n.is_first_or_final_node():
                    self.f.node(self.prefix + n.input_state)

            for n in self.nodes:
                self.f.attr('node', shape='circle')
                if not n.is_first_or_final_node():
                    self.f.node(self.prefix + n.input_state)
                for r in n.associated_nodes:
                    self.f.edge(self.prefix + r.current_state, self.prefix + r.next_state, label=r.state)
        except:
            print(color.RED("Please close the pdf file and execute the program!"))

    def show_graph(self):
        """
        Shows the initialized graph
        :return: void
        """
        self.f.view()
