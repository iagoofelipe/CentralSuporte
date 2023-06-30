# módulos pyhon

# módulos locais
from src.GUI import Application
from src.update import check_update

if __name__ == "__main__":
    check_update()
    
    app = Application()
    app.loop()