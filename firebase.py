#-------------------------------------------------------------------------------
# Imports
import pyrebase
import os

#-------------------------------------------------------------------------------
# Variables & Setup

filelist = [ f for f in os.listdir(".") if f.endswith(".JPG") ]
for f in filelist:
    os.remove(os.path.join(".", f))

config = {
"apiKey": "Your API Key",
"authDomain": "Your auth domain",
"databaseURL": "https://connectiontopython.firebaseio.com",
"projectId": "connectiontopython",
"storageBucket": "connectiontopython.appspot.com",
"serviceAccount": "serviceAccountKey.json"
}

firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()

#-------------------------------------------------------------------------------
# Uploading And Downloading Images

# storage.child("Guitar.JPG").put("Guitar.JPG")
# storage.child("PlayingGuitar.JPG").download("PlayingGuitar.JPG")

all_files = storage.list_files()

for file in all_files:
    print(file.name)
    file.download_to_filename(file.name)
