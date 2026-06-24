import requests

try:
    r = requests.get("https://api.github.com/users/this-user-does-not-exist-zzz", timeout=5)
    r.raise_for_status()
    data = r.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
except requests.exceptions.Timeout:
    print("Запрос таймаутнул")
except requests.exceptions.ConnectionError:
    print("Не удалось подключиться")
except requests.exceptions.RequestException as e:
    print(f"Неизвестная ошибка requests: {e}")
