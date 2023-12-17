import unittest
from ..argument import Argument
from ..propositionparser import parse_proposition as parse

class TestArgument(unittest.TestCase):

    def test_is_valid(self):
        # p -> q
        # ∴ q -> p
        # False
        converse = Argument([parse('p -> q')], parse('q -> p'))
        self.assertFalse(converse.is_valid())

        # p -> q
        # ∴ ~p -> ~q
        # False
        inverse = Argument([parse('p -> q')], parse('~p -> ~q'))
        self.assertFalse(inverse.is_valid())

        # p -> q
        # ∴ ~q -> ~p
        # True
        contrapositive = Argument([parse('p -> q')], parse('~q -> ~p'))
        self.assertTrue(contrapositive.is_valid())

        # p
        # ∴ q
        # False
        diff_vars = Argument([parse('p')], parse('q'))
        self.assertFalse(diff_vars.is_valid())

        # ~p || q
        # ∴ p -> q
        # True
        conditional = Argument([parse('~p || q')], parse('p -> q'))
        self.assertTrue(conditional.is_valid())

        # p -> q
        # p
        # ∴ q
        # True
        conditional2 = Argument([parse('p->q'), parse('p')], parse('q'))
        self.assertTrue(conditional2.is_valid())

        # p -> q
        # q -> p
        # ∴ p <-> q
        # True
        biconditional = Argument([parse('p->q'), parse('q->p')], parse('p <-> q'))
        self.assertTrue(biconditional.is_valid())

        # p -> q
        # q -> r
        # ∴ p -> r
        # True
        transitive = Argument([parse('p->q'), parse('q->r')], parse('p->r'))
        self.assertTrue(transitive.is_valid())

        # p -> (q || ~r)
        # q -> (p & r)
        # ∴ p -> r
        # False
        argument = Argument([parse("p -> (q || ~r)"), parse("q -> (p & r)")], parse('p->r'))
        self.assertFalse(argument.is_valid())

        # p -> (q || ~r)
        # q -> (p & r)
        # r <-> t
        # ∴ (p & t) <-> q
        # True
        argument = Argument([parse("p -> (q || ~r)"), parse("q -> (p & r)"), parse('r <-> t')], parse('(p & t) <-> q'))
        self.assertTrue(argument.is_valid())

        # ~p & q
        # r -> p
        # ~r -> s
        # s -> t
        # ∴ t
        # True
        argument = Argument([parse('~p & q'), parse('r -> p'), parse('~r -> s'), parse('s -> t')], parse('t'))
        self.assertTrue(argument.is_valid())

        # ~p & q
        # r -> q
        # ~r -> s
        # s -> t
        # ∴ t
        # False
        argument = Argument([parse('~p & q'), parse('r -> q'), parse('~r -> s'), parse('s -> t')], parse('t'))
        self.assertFalse(argument.is_valid())
        
        # p <-> q
        # r || q
        # ~r
        # ∴ p
        # True
        argument = Argument([parse('p <-> q'), parse('r || q'), parse('~r')], parse('p'))
        self.assertTrue(argument.is_valid())


        



if __name__ == "__main__":
    unittest.main()