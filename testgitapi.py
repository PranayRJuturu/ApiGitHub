import unittest
from gitapi import getgitdata

class TestGitApi(unittest.TestCase):

    def testNoRepositories(self):
        self.assertEqual(getgitdata('ReddyJ'),'No repositories created.', 'No repositories created.')

    def testUserId(self):
        self.assertEqual(getgitdata('PranayRJuturu...........................'),'User ID cannot be longer than 39 characters!')    

    def testNoUser(self):
        self.assertEqual(getgitdata('PranayReeddyJuturuu'),'Failed to retrieve data!')
        
if __name__ == '__main__':
    print("Running unit tests")
    unittest.main()        