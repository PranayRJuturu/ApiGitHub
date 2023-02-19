import unittest
from gitapi import getGitData

class TestGitApi(unittest.TestCase):

    def testInput(self):
        self.assertEqual(getGitData('ReddyJ'),'No user/commits found!')

if __name__ == '__main__':
    print("Running unit tests")
    unittest.main()        