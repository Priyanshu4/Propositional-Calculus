from truthtable import TruthTable

class Argument():
    """ A class representing an argument with multiple propositions as premises and one conclusion.
    """

    def __init__(self, premises, conclusion):
        """ Initializes an argument given premises and a conclusion
        Params
        --------
        premises: A list of propositions representing the premises of the argument.
                  Premises are the propostions which are given to be true.
        conclusion: The proposition which is to be concluded from the premises.
        """
        self.premises = premises
        self.conclusion = conclusion
        variables = set()
        for prop in premises:
            variables = variables.union(prop.get_var_names())
        variables = variables.union(conclusion.get_var_names())
        self.truth_table = TruthTable(variables)
        for prop in premises:
            self.truth_table.add_proposition(prop)
        self.truth_table.add_proposition(conclusion)

    def is_valid(self):
        """ Determines if the argument is valid.
        An argument is valid if the conclusion is true in every case where all premises are true.
        """
        premise_cols = []
        for premise in self.premises:
            premise_cols.append(self.truth_table.get_proposition_col(premise))
        conclusion_col = self.truth_table.get_proposition_col(self.conclusion)
        argument_valid = True
        for i in range(len(conclusion_col)):
            premises_true = True
            for premise_col in premise_cols:
                if not premise_col[i]:
                    premises_true = False
            # if there is a case where all premises are true and the conclusion is false
            # then the argument is invalid
            if premises_true and not conclusion_col[i]:
                argument_valid = False
        return argument_valid

    def get_truth_table(self):
        """ Returns a truth table object which includes the premises and conclusion of the argument.
        """
        return self.truth_table