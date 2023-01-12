import requests

#print(requests.__version__)

result = requests.get('https://raw.githubusercontent.com/CryingOutCloud/lab1/master/version.py')
print(result.content)