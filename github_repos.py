import requests

USERNAME = "torvalds"  # или подставьте свой

response = requests.get(
    f"https://api.github.com/users/{USERNAME}/repos",
    params={"per_page": 10, "sort": "updated"},
    timeout=10,
)
response.raise_for_status()

repos = response.json()
print(f"Топ-10 репозиториев {USERNAME}:")
for r in repos:
    print(f" ⭐ {r['stargazers_count']:>6} {r['name']}: {r['description'] or '-'}")
