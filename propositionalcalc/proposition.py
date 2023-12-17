from abc import ABC, abstractmethod
from .truthtable import TruthTable

class Proposition(ABC):
    """
    Abstract base class for propositions.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, variable_values = None):
        """ Evaluates the proposition to a single boolean value.
        Params
        ------
        variable_values: a dictionary with the variable symbols as the key and
                         a boolean as the value of the variable.
        Returns
        -------
        truth: a boolean indicating whether the proposition is true or false.
        """
        pass

    @abstractmethod
    def get_var_names(self):
        """ Returns a set containing all the variable names used in this proposition.
        """
        pass

    @abstractmethod
    def __str__(self):
        pass

    def get_truth_table(self):
        """ Returns a truth table for the proposition.
        """
        var_names = self.get_var_names()
        truth_table = TruthTable(var_names)
        truth_table.add_proposition(self)
        return truth_table

class Variable(Proposition):
    """ Propositional Logic Variable that can be true or false
    """

    def __init__(self, name):
        """ Creates a variable with the given name. 
        Variable names are not case sensistive and should only contain letters.
        """
        self.name = name.lower()

    def evaluate(self, variable_values):
        for name, value in variable_values.items():
            if name.lower() == self.name:
                return value
        raise ValueError("Parameter variable_values does not contain value for variable ", self.name)

    def get_var_names(self):
        return set([self.name])

    def __str__(self):
        return self.name

class Constant(Proposition):
    """ Propositonal Logic constant that is always either true or false
    """

    def __init__(self, value):
        """ Creates a constant expression given its boolean value.
        """
        self.value = value

    def evaluate(self, variable_values = None):
        return self.value

    def get_var_names(self):
        return set()

    def __str__(self):
        if self.value:
            return "True"
        else:
            return "False"