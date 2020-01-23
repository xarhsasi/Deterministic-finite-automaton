import os
from helpers.FileReader import FileReader
from helpers.DFA import DFA
from helpers.DFAGraph import DFAGraph
from helpers.CLIColor import CLIColor as color


class Runnable:
    """
       DFA Runnable class which handles the whole program execution
    """

    def __init__(self):
        """
            Initialize the runnable class with its variables
        """
        self.prefix = "q"
        self.input_word = "010101010"
        self.rel_path = "dfa.txt"

        self.print_welcome()

    def calc_path_file(self):
        """
        calculate the relative path of the given file
        :return: Fle's path
        """
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, self.rel_path)
        return abs_file_path

    def run(self):
        """
        Execute the program logic
        :return: [nodes, table, symbols]
        """
        [nodes, table, symbols] = FileReader().read_file(self.calc_path_file())

        self.dfa_init(nodes, table, symbols)
        self.graph_init(nodes)

    def dfa_init(self, nodes, table, symbols):
        """
        initialize the DFA instance with the needed parameters
        :param nodes:
        :param table:
        :param symbols:
        :return: void
        """
        dfa = DFA(nodes, table, symbols)
        dfa.initialize_state()
        dfa.execute_dfa(word=self.input_word)

    def graph_init(self, nodes):
        """
        Initialize the graph logic
        :param nodes:
        :return: void
        """
        graph = DFAGraph(nodes=nodes, prefix=self.prefix)
        graph.initialize_graph()
        graph.show_graph()

    def print_welcome(self):
        """
        Sinmple welcome message for the represtation
        :return: void
        """
        print(color.YELLOW("******************************************************"))
        print(color.MAGENTA("HELLO DEAR USER, WELCOME TO DFA PYTHON CLI PROGRAM"))
        print(color.YELLOW("******************************************************"))
        print(color.UNDERLINE("Author: Charalampos Asimakopoulos"))
        print(color.UNDERLINE("AM: 141098"))
        print(color.UNDERLINE("Email: cs141098@uniwa.gr - xarhsasi@gmail.com"))
        print(color.UNDERLINE("Github: https://graphviz.readthedocs.io/en/stable/examples.html"))
