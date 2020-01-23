from helpers.DFATableRow import DFATableRow
from helpers.DFATable import DFATable
from helpers.DFANode import DFANode
from helpers.CLIColor import CLIColor as color


class FileReader:
    """
    DFA File Reader which handles the object structure based on file
    """

    def __init__(self):
        """
        initialize the file reader variables
        """
        self.total_states = 0
        self.symbols = None
        self.first_state = None
        self.final_states = None

        self.nodes = []
        self.table = DFATable()
        self.used_symbols = []


    def read_file(self, filename):
        """
        Opens and reads the given file path and creates the instances which are described in file
        :param filename:
        :return: [self.nodes, self.table]
        """

        try:
            i = 0
            with open(filename) as f:
                for line in f:
                    if i == 0:
                        self.total_states = line
                    elif i == 1:
                        self.symbols = line
                    elif i == 2:
                        self.first_state = line
                    elif i == 3:
                        self.final_states = line
                    else:
                        row = line.replace("\n", "").split(" ")
                        is_first_state = True if int(self.first_state) == int(row[0]) else False
                        is_final_state = True if row[0] in self.final_states else False
                        if i == 4:
                            node_tmp = DFANode(row[0], is_first_state, is_final_state)
                            self.nodes.append(node_tmp)
                        else:
                            exists = False
                            for n in self.nodes:
                                if row[0] == n.input_state:
                                    exists = True
                            if not exists:
                                node_tmp = DFANode(row[0], is_first_state, is_final_state)
                                self.nodes.append(node_tmp)
                        self.used_symbols.append(row[1])
                        row_tmp = DFATableRow(row[0], row[1], row[2], is_first_state, is_final_state)
                        self.table.add_row(row_tmp)
                    i = i + 1
                # Add rows in nodes for a better representation and data handling
                for row in self.table.rows:
                    for node in self.nodes:
                        if row.current_state == node.input_state:
                            node.add_node(row)

                self.print_info()
                f.close()
                return self.nodes, self.table, self.symbols
        except FileNotFoundError:
            f.close()
            print(color.RED("ERROR: File not found"))

    def symbols_validity(self):
        """
        Checks if the dfa symbols described in the file are contained in the dfa dictionary
        which is also described in the file
        :return: Exits if error with the appropriate message, otherwise returns true (is valid)
        """
        for used_symbol in self.used_symbols:
            if used_symbol not in self.symbols:
                print(color.RED("The described symbols are not in the described dictionary, please try again!"))
                return False
        return True

    def print_info(self):
        print(color.YELLOW("******************************************************"))
        print(color.MAGENTA(f"Total States: {self.total_states}"
                            f"Symbols: {self.symbols}"
                            f"First state: {self.first_state}"
                            f"Final states: {self.final_states}"))
        print(color.YELLOW("******************************************************"))
