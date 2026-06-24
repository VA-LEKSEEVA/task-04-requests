import requests
from pathlib import Path

# Попробуем прочитать токен из файла, если его нет — сообщим
token_file = Path("~/.config/gitlab_token").expanduser()
if not token_file.exists():
    print("❌ Файл ~/.config/gitlab_token не найден. Создайте его с Personal Access Token.")
    print("   Инструкция: GitLab → Settings → Access Tokens → create 'read_api'")
    exit(1)

token = token_file.read_text().strip()

response = requests.get(
    "https://gitlab.com/api/v4/projects",
    headers={"PRIVATE-TOKEN": token},
    params={"membership": "true", "per_page": 5},
    timeout=10,
)
response.raise_for_status()

projects = response.json()
print(f"Найдено проектов: {len(projects)}")
for p in projects:
    print(f"#{p['id']:>8} {p['name_with_namespace']}")
