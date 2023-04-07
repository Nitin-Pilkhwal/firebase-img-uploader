import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage


# Initialize Firebase
cred = credentials.Certificate('Generated private key(json file) local path')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'storage path for firebase storage'
})

# Upload image
bucket = storage.bucket()
blob = bucket.blob('image name')
blob.upload_from_filename('local image-file path/image.png')
