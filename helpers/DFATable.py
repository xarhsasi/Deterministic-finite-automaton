class DFATable:
    """
    DFA Table class represents the whole table with its rows
    """

    def __init__(self, rows=[]):
        self.rows = rows

    """
        rows setter and getter
    """

    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, rows):
        self.__rows = rows

    @rows.getter
    def rows(self):
        return self.__rows

    def add_row(self, row):
        """
        Adds a row in the table
        :param row:
        :return:
        """
        self.rows.append(row)

    def __str__(self):
        for row in self.rows:
            attrs = vars(row)
            print(', '.join("%s: %s" % item for item in attrs.items()))
        return "<DFATable %s>\n" % (self.rows,)
