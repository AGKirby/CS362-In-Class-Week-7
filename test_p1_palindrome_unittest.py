import unittest
import p1_palindrome

class testPalindrome(unittest.TestCase):
    def test_palindrome1(self):
        result = p1_palindrome.palindrome("Hello world!")
        self.assertEqual(result, False)

    def test_palindrome2(self):
        result = p1_palindrome.palindrome("Race CAR")
        self.assertEqual(result, True)

    def test_palindrome3(self):
        result = p1_palindrome.palindrome("Mad!~!Dam")
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main(verbosity=2)