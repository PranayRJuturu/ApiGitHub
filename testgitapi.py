import unittest
from gitapi import getgitdata

class TestGitApi(unittest.TestCase):

    def testInput(self):
        self.assertEqual(getgitdata('ReddyJ'),'No repositories created.', 'No repositories created.')

if __name__ == '__main__':
    print("Running unit tests")
    unittest.main()        