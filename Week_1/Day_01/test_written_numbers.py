import unittest
from written_numbers import spellout

class WrittenNumbersTest(unittest.TestCase):

    def test_can_write_numbers(self):
        self.assertEqual("one thousand", spellout(1000))
        self.assertEqual(("two hundred and fifty nine thousand, one hundred "
                          "and twenty three"),
                         spellout(259123))
        # TODO: more assertions?!


# zmd@ExpectedReturn:~/Code/Examination/mockacademy/Week_1/Day_01$
# python -m unittest discover
# [... redacted]
# F
# ======================================================================
# FAIL: test_can_write_numbers (test_written_numbers.WrittenNumbersTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File
#   "/home/zmd/Code/Examination/mockacademy/Week_1/Day_01/test_written_numbers.py",
#   line 10, in test_can_write_numbers
#     spellout(259123))
# AssertionError: 'two hundred and fifty nine thousand, one hundred and
# twenty three' != 'two hundred and fifty nine thousand, one hundred and
# twenty three '

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=1)
