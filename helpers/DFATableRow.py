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

    """
        current_status setter and getter
    """

    @property
    def current_state(self):
        return self.__current_state

    @current_state.setter
    def current_state(self, current_state):
        self.__current_state = current_state

    @current_state.getter
    def current_state(self):
        return self.__current_state

    """
        state setter and getter
    """

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @state.getter
    def state(self):
        return self.__state

    """
        next_status setter and getter
    """

    @property
    def next_state(self):
        return self.__next_state

    @next_state.setter
    def next_state(self, next_state):
        self.__next_state = next_state

    @next_state.getter
    def next_state(self):
        return self.__next_state

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

    def is_first_or_final(self):
        return self.is_final or self.is_first

    def __str__(self):
        return "<DFATableRow %s %s %s %s %s>" % (
            self.current_state, self.state, self.next_state, self.is_first, self.is_final)
