class DFATableRow:
    """
    DFA Table row class which represents each row of a DFA table
    """

    def __init__(self, current_state, state, next_state, is_first, is_final):
        """
        initialize the RowTable object with its arguments
        :param current_state:
        :param state:
        :param next_state:
        """

        self.current_state = current_state
        self.state = state
        self.next_state = next_state
        self.is_first = is_first
        self.is_final = is_final

    def is_first_or_final(self):
        return self.is_final or self.is_first

    def __str__(self):
        return "<DFATableRow %s %s %s %s %s>" % (
            self.current_state, self.state, self.next_state, self.is_first, self.is_final)
