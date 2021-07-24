import requests


SECRET_URL = "https://raw.githubusercontent.com/MrGallo/pbd-python/master/web-files/secret-data.txt"
request = requests.get(SECRET_URL)
secrets = request.text

print(secrets)
