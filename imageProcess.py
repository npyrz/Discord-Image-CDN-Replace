import requests

def upload_image_to_imgur(image_path, client_id, username, fileType):
    # Check the file type of the image and set the payload accordingly
    if fileType in ['png', 'jpg', 'jpeg']:
        fileTypePayload = "image"
    elif fileType in ['gif', 'mp4', 'mkv', 'mov', 'avi']:
        fileTypePayload = "video"
    
    # Extract the file name without the path and extension
    file_name = image_path.split('/')[-1].split('\\')[-1]

    url = "https://api.imgur.com/3/image" # Imgur API endpoint
    payload = {
        'type': fileTypePayload, # Set the type of the file
        'title': file_name + ' uploaded by ' + username, # Original filename and username to be shown on the site and discord
    }
    files = [
        ('image', (image_path, open(image_path, 'rb'), 'image/' + fileType)) # Open the image file in binary mode
    ]
    headers = {
        'Authorization': f'Client-ID {client_id}' # Authorization header with the client
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files) # Send the request to imgur
    return response.json()['data']['link'] # Return the link of the uploaded image