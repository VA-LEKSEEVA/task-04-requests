import requests
from pathlib import Path

# Читаем токен
token_file = Path("~/.config/github_token").expanduser()
if not token_file.exists():
    print("❌ Файл ~/.config/github_token не найден. Создайте его с Personal Access Token.")
    exit(1)

token = token_file.read_text().strip()

# Данные для нового репозитория
repo_data = {
    "name": "test-api-repo",
    "description": "Создан через GitHub API (POST-запрос)",
    "private": False,
}

response = requests.post(
    "https://api.github.com/user/repos",
    headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    },
    json=repo_data,
    timeout=10,
)

if response.status_code == 201:
    print("✅ Репозиторий создан!")
    print(f"URL: {response.json()['html_url']}")
else:
    print(f"❌ Ошибка: {response.status_code}")
    print(response.text)
