# Discord-Image-CDN-Replace IN DEVELOPMENT
- CDN Image Replaced with 3rd party image hosting automatically when user sets image in discord because discord image links only last 7 days

## TODO
    - MAYBE ADD FEATURE FOR ADMINS TO ENABLE A LOG CHANNEL TO VIEW IMAGES
    - OPTIONALIZING THE WHOLE THING MAYBE ADMIN SET/USER SET
    - 3RD PARTY IDEA TO USE MACHINE LEARNING OR SOMETHING TO DELETE NFSW IMAGES FROM SERVERS

## SOURCES
https://apidocs.imgur.com/#intro

## USER GUIDE
You can obtain your Client ID by registering an application on the Imgur website:
-Go to the Imgur API registration page.
-Log in with your Imgur account.
-Fill out the form to register your application. You can choose "OAuth 2 authorization without a callback URL" for simplicity.
-After registering, you will be provided with a Client ID and a Client Secret. Use the Client ID in your code.
-Replace 'IMGUR_CLIENT_ID' in the .env file with the actual Client ID provided by Imgur.

## REQUIRMENTS
- IMGUR API Client Key
- Postman (Optional, nice to use to view all requests)
