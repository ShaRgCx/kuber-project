import requests
import json
import time

# URL-адрес endpoint'а
service_name = 'web-app'
statistics_url = f"http://{service_name}/statistics"

# Имя файла для записи статистики
filename = "statistics.json"

if __name__ == '__main__':
	while True:
		try:
			response = requests.get(statistics_url)
			if response.status_code == 200:
    				data = json.loads(response.content)

    				requests_count = data["requests_count"]

    				with open(filename, "w") as f:
        				json.dump({"requests_count": requests_count}, f)
		except requests.exceptions.RequestException:
			continue
		time.sleep(5)                  
