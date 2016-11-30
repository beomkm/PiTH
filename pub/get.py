import requests

URL = "http://128.199.254.45:8000/register"
params = {'time': '20161201023924', 'temp': 33, 'humi' :37}
requests.get(URL, params=params)
