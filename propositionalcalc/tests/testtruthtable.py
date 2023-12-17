import unittest
from ..truthtable import TruthTable
from ..proposition import Variable
from ..logicalconnective import Negation, Conjunction, Disjunction, Conditional, Biconditional

class TestTruthTable(unittest.TestCase):
    
    def test_init(self):
        x, y, z = Variable('x'), Variable('y'), Variable('z')
        tt = TruthTable([x.name, y.name, z.name])
        self.assertEqual(tt.n_vars, 3)
        x_col = tt.get_proposition_col(x)
        y_col = tt.get_proposition_col(y)
        z_col = tt.get_proposition_col(z)
        # check if all unique possbilities are covered
        self.assertEqual(tt.n_rows, 8)
        row_set = set()
        for i in range(len(x_col)):
            row_tuple = (x_col[i], y_col[i], z_col[i])
            row_set.add(row_tuple)
        self.assertEqual(len(row_set), 8)

    def test_add_proposition(self):
        x, y, z = Variable('x'), Variable('y'), Variable('z')
        tt = TruthTable([x.name, y.name, z.name])
        prop = Conjunction(x, y)
        tt.add_proposition(prop)
        x_col = tt.get_proposition_col(x)
        y_col = tt.get_proposition_col(y)
        prop_col = tt.get_proposition_col(prop)
        for i in range(len(x_col)):
            self.assertTrue(prop_col[i] == (x_col[i] and y_col[i]))

    def test_get_truth_table(self):
        x, y = Variable('x'), Variable('y')
        always_true = Disjunction(Disjunction(x, Negation(x)), y)
        tt = always_true.get_truth_table()
        prop_col = tt.get_proposition_col(always_true)
        for truth_val in prop_col:
            self.assertTrue(truth_val)
        

if __name__ == '__main__':
    unittest.main()


    


