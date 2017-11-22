import firebase_admin
from firebase_admin import credentials,db



cred = credentials.Certificate('./botbienesraices-firebase-adminsdk-qk0jv-f88daca119.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://botbienesraices.firebaseio.com/'
})
root = db.reference()

new_user = root.child('BienesInmuebles').push({
    'descripcionInmueble' : 'Se vende casa de lujo con 3 dormitorios',
    'localizacion' : 'equipetrol',
    'medida' : 'm2',
    'moneda' : 'bolivianos',
    'nombrecontacto' : 'Ejemplo',
    'precio' : 5000,
    'superficie' : 'm2',
    'tamano' : 520,
    'telefonocontacto' : 78956230,
    'tipolugar' : 'casa',
    'tipotransaccion' : 'venta',
    'url' : 'http://www.tumomo.com/files/73/01/577730_1.jpg',
    'zona' : 'sur'
})

mary = db.reference('BienesInmuebles/1'.format(new_user.key)).get()
print mary
