import unittest
from extract_markdown import extract_title

class TestExtract(unittest.TestCase):
    def test_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

if __name__ == "__main__":
    unittest.main()
