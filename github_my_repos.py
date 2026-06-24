import requests
from pathlib import Path

token = Path("~/.config/github_token").expanduser().read_text().strip()

response = requests.get(
    "https://api.github.com/user/repos",
    headers={"Authorization": f"token {token}"},
    params={"per_page": 5, "sort": "updated"},
    timeout=10,
)
response.raise_for_status()

repos = response.json()
print("Мои последние 5 репозиториев:")
for r in repos:
    print(f"  {r['name']} ({r['private'] and 'приватный' or 'публичный'})")
