import requests
import json
import sys

try:
    userId = input("Enter the GitHub UserId: ")
    if len(userId)>39:
        print("User ID cannot be longer than 39 characters!")

    repositoryResponse = requests.get('https://api.github.com/users/'+userId+'/repos')
  
    if(repositoryResponse.status_code != 200):
        raise FileNotFoundError
        sys.exit()  

    jsonReposiotryResponse = json.loads(repositoryResponse.text)

except FileNotFoundError:
    print("No user found!")

try:
    for repository in jsonReposiotryResponse:

        commitsResponse = requests.get('https://api.github.com/repos/'+userId+'/'+repository['name']+'/commits')
        if(commitsResponse.status_code != 200):
            raise FileNotFoundError
            sys.exit()
        jsonCommitsResponse = json.loads(commitsResponse.text)
        print("Repo:"+repository['name']+" Number of commits:",len(jsonCommitsResponse))
except FileNotFoundError:
    print("No commits found!")    