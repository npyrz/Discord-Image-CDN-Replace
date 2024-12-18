# GIVEN CODE FROM THE IMGUR API SITE - NOT STARTED THIS FEATURE YET

import requests

url = "https://api.imgur.com/3/image"

payload={'type': 'image',
'title': 'Simple upload',
'description': 'This is a simple image upload in Imgur'}
files=[
  ('image',('GHJQTpX.jpeg',open('C:\Users\noahp\Desktop\Code\Discord-Image-CDN-Replace\imgs','rb'),'image/jpeg'))
]
headers = {
  'Authorization': 'Client-ID {{clientId}}'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
