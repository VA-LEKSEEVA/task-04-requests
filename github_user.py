import requests

response = requests.get("https://api.github.com/users/torvalds")
print(f"Status: {response.status_code}")
data = response.json()
print(f"Name: {data['name']}")
print(f"Public repos: {data['public_repos']}")
print(f"Followers: {data['followers']}")