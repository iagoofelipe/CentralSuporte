# módulos pyhon
from my_tools import File, Registros as reg

# módulos locais
from src.GUI import Application

if __name__ == "__main__":
    fileName = r'\\TRUNAS\certfy\config\Files\default.json'
    if File.isFile(fileName):
        users = File.getFile(fileName)['users']
    else:
        users = reg.get('users').split(', ')

    app = Application(users)
    app.loop()