import requests

def upload_image_to_imgur(image_path, client_id, title, username):
    url = "https://api.imgur.com/3/image"
    payload = {
        'type': 'image',
        'title': title + ' uploaded by ' + username, # Original filename and username to be shown on the site and discord
    }
    files = [
        ('image', (image_path, open(image_path, 'rb'), 'image/jpeg'))
    ]
    headers = {
        'Authorization': f'Client-ID {client_id}'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response.json()['data']['link']
