import unittest
import p2_wordcount

class testPalindrome(unittest.TestCase):
    def test_wordcount1(self):
        result = p2_wordcount.wordcount("Hello world!")
        self.assertEqual(result, 2)

    def test_wordcount2(self):
        result = p2_wordcount.wordcount("Hello, there are 3 cows!")
        self.assertEqual(result, 5)

    def test_wordcount3(self):
        result = p2_wordcount.wordcount("!@#$%^&*() ")
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)