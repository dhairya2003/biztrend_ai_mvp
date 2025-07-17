import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)

def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return user.uid
    except Exception as e:
        return str(e)

def verify_user(email, password):
    return True  # Demo-only placeholder