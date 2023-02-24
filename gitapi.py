import requests
import json
import sys


def getgitdata(userId):

    if len(userId)>39:
        return "User ID cannot be longer than 39 characters!"
        sys.exit()
    repositoryResponse = requests.get('https://api.github.com/users/'+userId+'/repos')
    if repositoryResponse.status_code != 200:
        return "Failed to retrive data!"
        sys.exit()  
    jsonReposiotryResponse = json.loads(repositoryResponse.text)

    if len(jsonReposiotryResponse) <= 0:
        return "No repositories created."

    for repository in jsonReposiotryResponse:

        commitsResponse = requests.get('https://api.github.com/repos/'+userId+'/'+repository['name']+'/commits')
        if commitsResponse.status_code != 200:
            return "Failed to retrieve data!"
            sys.exit()
        jsonCommitsResponse = json.loads(commitsResponse.text)

        if len(jsonCommitsResponse) <=0:
            return "No commits to the repository "+ repository['name']    
        return "Repo:"+repository['name']+" Number of commits:",len(jsonCommitsResponse)

userId = input("Enter the GitHub UserId: ")
if len(userId)>39:
    print("User ID cannot be longer than 39 characters!")
    print(getgitdata(userId))

