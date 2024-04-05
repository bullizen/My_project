# test palindromish
import unittest

from palindromish import palindromish

# lista med testfall:
# kajak 2 -> True
# nastraran 3 -> False
# naturrutan 4 -> True
# hejsan 2 -> False
# <tomt> -> True
# nationalencyklopedin 3 -> False
# nationalencyklopedin 1 -> True
# heltal, en int 5
# radar -> True

class TestPalindromish(unittest.TestCase):

    def test_nastaran_two(self):
        self.assertEqual(palindromish("nastaran", 2), True)

    def test_kajak_two(self):
        self.assertEqual(palindromish("kajak", 2), True)

    def test_naturrutan_four(self):
        self.assertEqual(palindromish("naturrutan", 4), True)

    def test_hejsan_two(self):
        self.assertEqual(palindromish("hejsan", 2), False)

    def test_tom_strang(self):
        self.assertEqual(palindromish(""), True)

    def test_nationalencyklopedin_three(self):
        self.assertEqual(palindromish("nationalencyklopedin", 3), False)

    def test_nationalencyklopedin_one(self):
        self.assertEqual(palindromish("nationalencyklopedin", 1), True)

    def test_typ_heltal_raises_typeerror_with_string(self):
        with self.assertRaisesRegex(TypeError, "Ange en strang"):
            palindromish(12345)

    def test_radar(self):
        self.assertEqual(palindromish("radar"), True)

if __name__ == '__main__':
    unittest.main()