import os
from tools import Json

credentials = {
  "type": "service_account",
  "project_id": "ancient-tractor-385119",
  "private_key_id": "60f1ef8f7dd13fcaf68f931d463449bc51e49518",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClemR6rLA0IUqg\nL5+ftJzbKOE3o2LAGwH95zCnZ7OBR+kAD853Wqqu2WBEbECsrvrAyLvpdxHK/xLD\n4yvJyX/vGSLTg2BsE0da0ichZ7ueAUdY5mBhd4lFj2EajKw2J4vp/SFBWXtdl/+4\nCCrwMR88EDqg8Uxe5HmyfOvMJgE86zMWMJ1/YV5EejpZqf4FraucYPrbOhyahO8f\n78GRPIT26qA7oAyUO/y1uqKNYb+2yKyK3gWDH8Jek68njG0Yb7Zku+Q3iZ/IjL04\nuqLVx6q9XW+Cuq1ARh5lZ6t6HnISuZK798sTPfm3vDcO82NFqi3sKPjgUtD34Knq\nqZj1iQklAgMBAAECggEAQA/bcWCEUJIo3U3CiqX16aRwWEVQ+BUclsqXW9+6Lw0D\nR4pXAH7hwBIYgjS0bwXIvrSXhuEZStCn150NOS/gbtR41pCwVfa6s47TJkwN5rQR\nBnodiu4nfv3sdkZKbyatNFdSNgXpzAiJr5m94cHqmSqhP+hajAwAjxhsgtqdtRKr\nPOyPMEQGvW95Neco7rNiXp+Y+kxLIMAOyYfE1P8Hn4dOBMa+vvdFvy7in/WPazDq\nTwsRtzBxKe1grSaFaVWly5D1zN09EkUxkfU3loXa1Zb8aD4kGUlSoJAl0q1yoPcQ\n22Lt8KFrRErTruuHuQGAPPVGCyExVB1DKbK7Q0Z1WwKBgQDb4ocdSJoqmvWL9hKZ\n0M1g0i7vqpXVtThuXS5D1C/e33+lxOSyXsRE5NN14jSKaHOKg03EgGTJgSPMm6Fh\nl47f0beH5sE9GNoADB13LDMg23IbQZdv2PQIGpYipUHVT7gCsEfCTyDeXd0BDwmS\nRX65AaPXA3V3UvPW8uQVIAZ6lwKBgQDAqDrGwqoh3RtLSSL0KvwUWAGvokNeIKwD\n3sFTeTxJrlnN+x7yNBM1cqU3upuDllJfkG+4kft/4u+LGcrh2mWOdqgF00g8wK1W\nXCz0FsfOwgBL2icoCeMxcNMyCd3/JAZu1GQmDUc1aqaXPsRpPoOUsfXIYpNlPqVx\ntxcb0MU9owKBgAGw5EkdXdImDu1cnxf/uxSbiTDepvhVxHFU1h4/a37TSTAFK50T\njX7aI6YsbysBUqImEFsKgbvq+lOAfuU5PSgLfNXWuHW30zVc4n0gIeSGy4HaJ0f8\n6yOE0NLDYpY5Xrjmkia0ZRRQtHplmzU8w5S4poHozOZ2BNoKVCa1cFdRAoGBAJcI\ny9tabOpTXrxsv7xPnoOMYvX/7XRzhKccEM+R8dOJndm/jwkuDgkOsbu4zYYhaL6G\niy9VMqeVj1mrhMP+5TMEjsDSXIVUQA+9/3f0C/xpVrYgdiYLalMuMkO+PI1y/qAQ\nXdr++d5EmAlmKbCgU6NUyGyp6weqTyWQ9crWpmqlAoGAPnS/tiUsTj3EsVOeYdnW\nGEdyKvx3qxtAohPI57IH380bJLOTd9CMMhAqiudRZMfqXl9jwQcAzKqMdb3AXZO/\ntey5BD0JfmOpF+6gza8FCwgJMlT+4ghdPDelcWqGyIzmWYth5fAnHR7DyvN22blE\nv+EWXoUP4FMKOBc3/HfPkGw=\n-----END PRIVATE KEY-----\n",
  "client_email": "python-278@ancient-tractor-385119.iam.gserviceaccount.com",
  "client_id": "106310570490629841510",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-278%40ancient-tractor-385119.iam.gserviceaccount.com"
}

def make_files():
    __path__ = os.path.abspath('')
    fileName = __path__ + r'\files'
    if not os.path.exists(fileName):
        os.mkdir(__path__ + r'\files')
    
    Json.setJson(credentials, __path__ + r'\files\credentials.json')

    os.system(r'getmac /fo csv > files\mac.txt')
    os.system(r'net localgroup Administradores > files\administradores.txt')
    os.system(r'net localgroup Usuários > files\usuarios.txt')