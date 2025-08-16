import json
import firebase_admin
from firebase_admin import credentials, firestore

# 1️⃣ Firebase service account key
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# 2️⃣ Firestore client তৈরি
db = firestore.client()

# 3️⃣ JSON ফাইল load করা
with open("divisions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 4️⃣ Upload to Firestore
# ধরো আমরা 'upazilas' নামে collection তৈরি করব
for upazila in data['divisions']:
    doc_ref = db.collection('divisions').document(str(upazila['id']))
    doc_ref.set(upazila)

print("All data uploaded successfully!")
