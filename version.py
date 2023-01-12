import requests

#print(requests.__version__)

result = requests.get('https://www.google.com/teapot')
print(result)