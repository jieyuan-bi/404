import requests

URL = "https://raw.githubusercontent.com/jieyuan-bi/404/main/q8.py"
r = requests.get(url = URL, allow_redirects=True)
print(r.content)
open('q8.py', 'wb').write(r.content)