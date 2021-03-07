import unittest
import stringcompression


class TestStringCompression(unittest.TestCase):

    def test_stringcompression(self):
        result = stringcompression.compress("bbcceeee")
        self.assertEqual(result, "b2c2e4")
        self.assertEqual(
            stringcompression.compress("aaabbbcccaaa"), "a3b3c3a3")
        self.assertEqual(stringcompression.compress("a"), "a")


if __name__ == '__main__':
    unittest.main()

