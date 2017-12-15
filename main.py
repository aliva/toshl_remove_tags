import requests

# Get your token from
# https://developer.toshl.com/
TOKEN = 'YOUR_TOKEN'

resp = requests.get('https://api.toshl.com/me', auth=(TOKEN, ''))
print(resp.json()['email'])

while True:
    resp = requests.get('https://api.toshl.com/categories', auth=(TOKEN, ''))
    for category in resp.json():
        print('deleting category:', category['name'])
        requests.delete(
            'https://api.toshl.com/categories/%s' % category['id'],
            auth=(TOKEN, ''),
        )
    else:
        break

while True:
    resp = requests.get('https://api.toshl.com/tags', auth=(TOKEN, ''))
    for tag in resp.json():
        print('deleting tag:', tag['name'])
        requests.delete(
            'https://api.toshl.com/tags/%s' % tag['id'],
            auth=(TOKEN, ''),
        )
    else:
        break
