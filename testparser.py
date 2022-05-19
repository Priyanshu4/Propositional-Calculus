import unittest
from propositionparser import parse_proposition
from proposition import Variable, Constant
from logicalconnective import Negation, Conjunction, Disjunction, Conditional, Biconditional

class TestParser(unittest.TestCase):
    
    def test_parse_proposition(self):
        expected_prop = Variable("cat")
        parsed_prop = parse_proposition("cat")
        self.assertEqual(str(parsed_prop), str(expected_prop))

        expected_prop = Biconditional(Variable('p'), Variable('q'))
        parsed_prop = parse_proposition("p<->q")
        self.assertEqual(str(parsed_prop), str(expected_prop))
        parsed_prop = parse_proposition("P <-> q")
        self.assertEqual(str(parsed_prop), str(expected_prop))

        x, y, z = Variable("x"), Variable("y"), Variable("z")
        expected_prop = Conjunction(Biconditional(x, y), Disjunction(Negation(y), (Conditional(x , z))))
        parsed_prop = parse_proposition("(x <-> y) & (!y || (x -> z))")
        self.assertEqual(str(parsed_prop), str(expected_prop))
        parsed_prop = parse_proposition("(x ↔ y) ^ (~y ∨ (x → z))")
        self.assertEqual(str(parsed_prop), str(expected_prop))

        pet, cat, dog = Variable("PET"), Variable("cat"), Variable("dog")
        expected_prop = Conditional(Disjunction(cat, dog), pet)
        parsed_prop = parse_proposition("cat || dog -> pet")
        self.assertEqual(str(parsed_prop), str(expected_prop))

        a, b, c = Variable("a"), Variable("b"), Variable("c")
        expected_prop = Biconditional(Conditional(Disjunction(Conjunction(Negation(a), b), a), b), c)
        parsed_prop = parse_proposition('¬A & B || A -> B <-> C')
        self.assertEqual(str(parsed_prop), str(expected_prop))

        t = Constant(True)
        f = Constant(False)
        expected_prop = Conjunction(t, f)
        parsed_prop = parse_proposition('true & false')
        self.assertEqual(str(parsed_prop), str(expected_prop))

        expected_prop = Biconditional(Conjunction(x, Negation(f)), t)
        parsed_prop = parse_proposition('x & ~False <-> true')
        self.assertEqual(str(parsed_prop), str(expected_prop))

if __name__ == '__main__':
    unittest.main()

