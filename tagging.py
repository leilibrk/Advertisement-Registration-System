import requests

api_key = 'acc_38499111344b01a'
api_secret = 'cc01fe2f6d032299d16db1743d26ef6b'


def tag(image_url):
    response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url, auth=(api_key, api_secret))
    response = response.json()
    state = ''
    category = ''
    for t in response['result']['tags']:
        if t['tag']['en'] == 'vehicle' and t['confidence'] > 50:
            state = 'confirmed'
    if state == '':
        state = 'rejected'
    max_confidence = 0
    max_tag = ''
    if state == 'confirmed':
        for t in response['result']['tags']:
            if t['confidence'] > max_confidence:
                max_confidence = t['confidence']
                max_tag = t['tag']['en']
    category = max_tag
    return state, category
