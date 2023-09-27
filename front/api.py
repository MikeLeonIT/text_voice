import requests

response = requests.post('http://localhost:63342', data={'foo': 'bar'})
print('URL:', response.request.url)
print('Body:', response.request.body)
print('-' * 10)

response = requests.post('http://localhost:63342', data='foo=bar')
print('URL:', response.request.url)
print('Body:', response.request.body)