import requests
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

GOOGLE_CLIENT_ID = "1057703273834-ln6o2p8n8evoho9sqjg52un487s4lrit.apps.googleusercontent.com"

def verify_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            google_requests.Request(),
            GOOGLE_CLIENT_ID
        )

        return {
            "email": idinfo["email"],
            "name": idinfo.get("name"),
            "picture": idinfo.get("picture")
        }

    except Exception as e:
        print("Token verification failed:", e)
        return None
