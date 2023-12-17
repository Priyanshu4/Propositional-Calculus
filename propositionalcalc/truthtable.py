class TruthTable:
    """ A class representing truth tables for propositions. """

    def __init__(self, variable_names):
        """ Creates a truth table with a column for each unique variable name. """
        self.var_names = set(variable_names)
        self.var_names_list = sorted(list(self.var_names))
        self.n_vars = len(self.var_names)
        self.n_rows = 2 ** self.n_vars

        # Initialize the truth table as a list of dictionaries
        self.truth_table = []

        for i in range(self.n_rows):
            row = {}
            flags = format(i, '0' + str(self.n_vars) + 'b')
            for var, bit in zip(variable_names, flags):
                row[var] = bit == '1'
            self.truth_table.append(row)

    def add_proposition(self, prop):
        """ Adds a column for a proposition to the truth table. """
        prop_vars = prop.get_var_names()
        if not prop_vars.issubset(self.var_names):
            raise ValueError("Variables in the proposition must be in the table.")
        
        if str(prop) in self.truth_table[0]:
            return

        for row in self.truth_table:
            row[str(prop)] = prop.evaluate(row)

    def get_proposition_col(self, prop):
        """ Gets a list representing the column of values for a given proposition. """
        return [row[str(prop)] for row in self.truth_table]

    def __str__(self):
        # Create a string representation of the truth table
        header = ' '.join(self.var_names_list) + '\n'
        rows = [' '.join(['T' if col else 'F' for col in row.values()]) for row in self.truth_table]
        return header + '\n'.join(rows)
