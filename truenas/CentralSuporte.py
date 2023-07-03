from src.GUI import Application
from src.tools import check_update

if __name__ == "__main__":
    check_update()
    
    app = Application()
    app.loop()