from gitapi import getgitdata

try:
    userId = input("Enter the GitHub UserId: ")
    if len(userId)>39:
        print("User ID cannot be longer than 39 characters!")
    getgitdata(userId)
except FileNotFoundError:
    print("No user found!")