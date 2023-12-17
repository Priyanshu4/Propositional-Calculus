from .proposition import Proposition

class Negation(Proposition):
        
    def __init__(self, proposition):
        self.proposition = proposition

    def evaluate(self, variable_values = None):
        return not self.proposition.evaluate(variable_values)

    def get_var_names(self):
        return self.proposition.get_var_names()

    def __str__(self):
        return "¬" + str(self.proposition)

class DualLogicalConnective(Proposition):
    
    def __init__(self, left_proposition, right_proposition):
        self.left_proposition = left_proposition
        self.right_proposition = right_proposition

    def get_var_names(self):
        left_names = self.left_proposition.get_var_names()
        right_names = self.right_proposition.get_var_names()
        return left_names.union(right_names)

class Conjunction(DualLogicalConnective):

    def __init__(self, left_proposition, right_proposition):
        super().__init__(left_proposition, right_proposition)

    def evaluate(self, variable_values = None):
        left_val = self.left_proposition.evaluate(variable_values)
        right_val = self.right_proposition.evaluate(variable_values)
        return left_val and right_val

    def __str__(self):
        return "(" + str(self.left_proposition) + "∧" + str(self.right_proposition) + ")"

class Disjunction(DualLogicalConnective):

    def __init__(self, left_proposition, right_proposition):
        super().__init__(left_proposition, right_proposition)

    def evaluate(self, variable_values = None):
        left_val = self.left_proposition.evaluate(variable_values)
        right_val = self.right_proposition.evaluate(variable_values)
        return left_val or right_val

    def __str__(self):
        return "(" + str(self.left_proposition) + "∨" + str(self.right_proposition) + ")"

class Conditional(DualLogicalConnective):

    def __init__(self, left_proposition, right_proposition):
        super().__init__(left_proposition, right_proposition)

    def evaluate(self, variable_values = None):
        left_val = self.left_proposition.evaluate(variable_values)
        right_val = self.right_proposition.evaluate(variable_values)
        return not left_val or (left_val and right_val)

    def __str__(self):
        return "(" + str(self.left_proposition) + "→" + str(self.right_proposition) + ")"
    
class Biconditional(DualLogicalConnective):

    def __init__(self, left_proposition, right_proposition):
        super().__init__(left_proposition, right_proposition)

    def evaluate(self, variable_values = None):
        left_val = self.left_proposition.evaluate(variable_values)
        right_val = self.right_proposition.evaluate(variable_values)
        return left_val == right_val

    def __str__(self):
        return "(" + str(self.left_proposition) + "↔" + str(self.right_proposition) + ")"





