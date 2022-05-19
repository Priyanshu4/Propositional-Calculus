from pandas import DataFrame

class TruthTable:
    """ A class representing truth tables for propositions.
    """

    def __init__(self, variable_names):
        """ Creates a truth table with a column for each unique variable name.
        """
        self.var_names = set(variable_names)
        self.n_vars = len(variable_names) 
        # each variable has 2 possible values
        # therefore, we need 2^n_vars rows
        self.n_rows = 2 ** self.n_vars
        self.dataframe = DataFrame(columns = variable_names, index = [i for i in range(self.n_rows)])
        
        # build each row in dataframe
        for i in range(self.n_rows):
            # convert index i to a binary number with length = to n_vars
            # each bit in i gives us the truth value of a variable
            flags = format(i, '0' + str(self.n_vars) + 'b')
            row = []
            for bit in flags:
                if bit == '0':
                    row.append(False)
                else:
                    row.append(True)
            self.dataframe.loc[i] = row

    def add_proposition(self, prop):
        """ Adds a column for a proposition to the truth table.
        The proposition should only use variables already included in the truth table.
        """
        prop_vars = prop.get_var_names()
        if not prop_vars.issubset(self.var_names):
            raise ValueError("The variable names used in the proposition must be the same as the names used in the table.")
        prop_column = []
        column_names_list = self.dataframe.columns.values.tolist()
        if str(prop) in column_names_list:
            return
        var_names_list = column_names_list[:self.n_vars]
        for i in range(self.n_rows):
            # create a dictionary assigning variable names to truth values
            var_truth_vals_list = self.dataframe.loc[i, :].values.tolist()[:self.n_vars]
            var_truth_vals_dict = dict(zip(var_names_list, var_truth_vals_list))
            # evaluate the proposition using the truth values of this row
            prop_truth = prop.evaluate(var_truth_vals_dict)
            # append the truth value to the column
            prop_column.append(prop_truth)
        # append the new column to the dataframe
        self.dataframe.insert(len(self.dataframe.columns), str(prop), prop_column)

    def get_proposition_col(self, prop):
        """ Gets a list representing the column of values for a given proposition.
        """
        return self.dataframe[str(prop)].tolist()

    def __str__(self):
        return self.dataframe.to_string(index=False)



