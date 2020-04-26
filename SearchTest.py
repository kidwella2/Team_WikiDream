import unittest
from Search import Search

class MyTestCase(unittest.TestCase):
    '''test to make sure searched words are highlighted'''
    def test_searchExampleHighlight(self):
        self.assertEqual('one two \x1b[42m\x1b[30mcat\x1b[0m ball house run pet shoe alpaca pizza \x1b[42m\x1b[30mcat\x1b[0m',
                         Search().search('cat'))

    def test_searchExampleHighlight2(self):
        self.assertEqual('one two cat ball house run pet shoe alpaca pizza cat',
                         Search().search('donkey'))

if __name__ == '__main__':
    unittest.main()
