import unittest
from logic_operations import AND, OR, NOT, IMPLICATION, BICONDITIONAL

class TestLogicOperations(unittest.TestCase):

    # Normal cases
    def test_AND_true_true(self):
        self.assertTrue(AND(True, True), "AND(True, True) should be True")

    def test_OR_false_false(self):
        self.assertFalse(OR(False, False), "OR(False, False) should be False")

    def test_NOT_true(self):
        self.assertFalse(NOT(True), "NOT(True) should be False")

    # Edge cases
    def test_IMPLICATION_true_false(self):
        self.assertFalse(IMPLICATION(True, False), "IMPLICATION(True, False) should be False")

    def test_BICONDITIONAL_true_false(self):
        self.assertFalse(BICONDITIONAL(True, False), "BICONDITIONAL(True, False) should be False")

    def test_AND_false_false(self):
        self.assertFalse(AND(False, False), "AND(False, False) should be False")

if __name__ == '__main__':
    unittest.main()
