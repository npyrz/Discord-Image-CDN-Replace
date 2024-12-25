import requests

def upload_image_to_imgur(image_path, client_id, username, fileType):
    if fileType in ['jpg', 'png', 'jpeg']:
        fileTypePayload = "image"
    elif fileType in ['gif', 'mp4', 'mov', 'avi', 'webm']:
        fileTypePayload = "video"
    
    # Extract the file name without the path and extension
    file_name = image_path.split('/')[-1].split('\\')[-1]

    url = "https://api.imgur.com/3/image"
    payload = {
        'type': fileTypePayload,
        'title': file_name + ' uploaded by ' + username, # Original filename and username to be shown on the site and discord
    }
    files = [
        ('image', (image_path, open(image_path, 'rb'), 'image/' + fileType))
    ]
    headers = {
        'Authorization': f'Client-ID {client_id}'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response.json()['data']['link']
