import requests

session = requests.Session()
session.headers.update({"User-Agent": "my-cli/1.0"})

users = ["torvalds", "kelseyhightower", "stefanprodan"]
for user in users:
    try:
        r = session.get(f"https://api.github.com/users/{user}", timeout=10)
        r.raise_for_status()
        print(r.json()["name"])
    except Exception as e:
        print(f"Ошибка при запросе {user}: {e}")
