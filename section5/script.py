import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Add
data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}
db.collection(u'cities').document(u'LA').set(data)

#  Update
db.collection(u'cities').document(u'LA').update({
    
})

db.collection(u'cities').document(u'DC').delete()
print(db)