import unittest
from proposition import Variable, Constant
from logicalconnective import Negation, Conjunction, Disjunction, Conditional, Biconditional

class TestProposition(unittest.TestCase):

    def test_constant(self):
        t = Constant(True)
        self.assertTrue(t.evaluate())
        f = Constant(False)
        self.assertFalse(f.evaluate())

    def test_variable(self):
        x = Variable("x")
        self.assertTrue(x.evaluate({'x': True}))
        self.assertFalse(x.evaluate({'x': False}))
        self.assertTrue(x.evaluate({'a': False, 'x': True, 'y': True}))
        self.assertFalse(x.evaluate({'a': False, 'x': False, 'y': True}))
        # test to ensure variable names are not case-sensitive
        self.assertTrue(x.evaluate({'X': True}))
        self.assertFalse(x.evaluate({'X': False}))
        # test multiple letter variable names
        x = Variable("var")
        self.assertTrue(x.evaluate({'var': True}))
        self.assertTrue(x.evaluate({'VAR': True}))
        self.assertFalse(x.evaluate({'var': False}))

    def test_negation(self):
        x = Variable("x")
        negation = Negation(x)
        self.assertTrue(negation.evaluate({'x': False}))
        self.assertFalse(negation.evaluate({'x': True}))

    def test_conjunction(self):
        x = Variable("x")
        y = Variable("y")
        conj = Conjunction(x, y)
        self.assertTrue(conj.evaluate({'x': True, 'y': True}))
        self.assertFalse(conj.evaluate({'x': False, 'y': True}))
        self.assertFalse(conj.evaluate({'x': True, 'y': False}))
        self.assertFalse(conj.evaluate({'x': False, 'y': False}))

    def test_disjunction(self):
        x = Variable("x")
        y = Variable("y")
        disj = Disjunction(x, y)
        self.assertTrue(disj.evaluate({'x': True, 'y': True}))
        self.assertTrue(disj.evaluate({'x': False, 'y': True}))
        self.assertTrue(disj.evaluate({'x': True, 'y': False}))
        self.assertFalse(disj.evaluate({'x': False, 'y': False}))

    def test_conditional(self):
        x = Variable("x")
        y = Variable("y")
        cond = Conditional(x, y)
        self.assertTrue(cond.evaluate({'x': True, 'y': True}))
        self.assertTrue(cond.evaluate({'x': False, 'y': True}))
        self.assertFalse(cond.evaluate({'x': True, 'y': False}))
        self.assertTrue(cond.evaluate({'x': False, 'y': False}))

    def test_biconditional(self):
        x = Variable("x")
        y = Variable("y")
        cond = Biconditional(x, y)
        self.assertTrue(cond.evaluate({'x': True, 'y': True}))
        self.assertFalse(cond.evaluate({'x': False, 'y': True}))
        self.assertFalse(cond.evaluate({'x': True, 'y': False}))
        self.assertTrue(cond.evaluate({'x': False, 'y': False}))

    def test_compound_propostion(self):
        x = Variable("x")
        y = Variable("y")
        z = Variable("z")
        # (x <-> y) & (!y || (x -> z))
        prop = Conjunction(Biconditional(x, y), Disjunction(Negation(y), (Conditional(x , z))))
        # x  y  z  Result
        # T  T  T  T
        # T  T  F  F
        # T  F  T  F
        # F  T  T  F
        # T  F  F  F
        # F  T  F  F
        # F  F  T  T
        # F  F  F  T
        self.assertTrue(prop.evaluate({'x': True, 'y': True, 'z': True}))
        self.assertFalse(prop.evaluate({'x': True, 'y': True, 'z': False}))
        self.assertFalse(prop.evaluate({'x': True, 'y': False, 'z': True}))
        self.assertFalse(prop.evaluate({'x': False, 'y': True, 'z': True}))
        self.assertFalse(prop.evaluate({'x': True, 'y': False, 'z': False}))
        self.assertFalse(prop.evaluate({'x': False, 'y': True, 'z': False}))
        self.assertTrue(prop.evaluate({'x': False, 'y': False, 'z': True}))
        self.assertTrue(prop.evaluate({'x': False, 'y': False, 'z': False}))

        t = Constant(True)
        f = Constant(False)
         # (x -> (f || y & t))
        prop = Conditional(x, Disjunction(f, Conjunction(y , t)))
        # x  y  Result
        # T  T  T  
        # T  F  F  
        # F  T  T  
        # F  F  T  
        self.assertTrue(prop.evaluate({'x': True, 'y': True}))
        self.assertFalse(prop.evaluate({'x': True, 'y': False}))
        self.assertTrue(prop.evaluate({'x': False, 'y': True}))
        self.assertTrue(prop.evaluate({'x': False, 'y': False}))
      
if __name__ == '__main__':
    unittest.main()