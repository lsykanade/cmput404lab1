import requests
print("version of requests: ",requests.__version__)

google = requests.get('https://www.google.com')
print(google.status_code)


script= requests.get('https://raw.githubusercontent.com/lsykanade/cmput404lab1/main/script.py')
print(script.text)