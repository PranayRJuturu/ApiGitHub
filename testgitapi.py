import unittest
from gitapi import getgitdata
from unittest.mock import MagicMock, patch
import json


class TestGitApi(unittest.TestCase):

    def testValidUserId(self):
        mock_repository_response = MagicMock(status_code=200)
        mock_repository_response.text = json.dump

    def testNoRepositories(self):
        self.assertEqual(getgitdata('ReddyJ'),'No repositories created.', 'No repositories created.')

    def testUserId(self):
        self.assertEqual(getgitdata('PranayRJuturu...........................'),'User ID cannot be longer than 39 characters!')    

    def testNoUser(self):
        self.assertEqual(getgitdata('PranayReeddyJuturuu'),'Failed to retrieve data!')

    def testUser(self):
        self.assertEqual(getgitdata('Pranay'),('Repo:Spoon-Knife Number of commits:', 5))    


    def test_getgitdata_with_valid_userid(self):
        mock_repository_response = MagicMock(status_code=200)
        mock_repository_response.text = json.dumps([{'name': 'repo1'}, {'name': 'repo2'}])
        mock_commits_response = MagicMock(status_code=200)
        mock_commits_response.text = json.dumps([{'sha': 'abc123'}, {'sha': 'def456'}])
        with patch('requests.get') as mock_get:
            mock_get.side_effect = [mock_repository_response, mock_commits_response]
            result = getgitdata('validuserid')
            self.assertEqual(result, ('Repo:repo1 Number of commits:', 2))

    def test_getgitdata_with_userid_longer_than_39_characters(self):
        result = getgitdata('12345678901234567890123456789012345678901')
        self.assertEqual(result, 'User ID cannot be longer than 39 characters!')

    def test_getgitdata_with_repository_response_not_200(self):
        mock_repository_response = MagicMock(status_code=404)
        with patch('requests.get', return_value=mock_repository_response):
            result = getgitdata('validuserid')
            self.assertEqual(result, 'Failed to retrieve data!')

    def test_getgitdata_with_empty_repository_response(self):
        mock_repository_response = MagicMock(status_code=200)
        mock_repository_response.text = '[]'
        with patch('requests.get', return_value=mock_repository_response):
            result = getgitdata('validuserid')
            self.assertEqual(result, 'No repositories created.')

    def test_getgitdata_with_commits_response_not_200(self):
        mock_repository_response = MagicMock(status_code=200)
        mock_repository_response.text = json.dumps([{'name': 'repo1'}])
        mock_commits_response = MagicMock(status_code=404)
        with patch('requests.get') as mock_get:
            mock_get.side_effect = [mock_repository_response, mock_commits_response]
            result = getgitdata('validuserid')
            self.assertEqual(result, 'Failed to retrieve data!')
        
if __name__ == '__main__':
    print("Running unit tests")
    unittest.main()        