import unittest

from .testargument import TestArgument
from .testparser import TestParser
from .testproposition import TestProposition
from .testtruthtable import TestTruthTable

test_cases = [TestArgument, TestParser, TestProposition, TestTruthTable]
test_suite = unittest.TestSuite()

for test_case in test_cases:
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_case))

runner = unittest.TextTestRunner()
runner.run(test_suite)
