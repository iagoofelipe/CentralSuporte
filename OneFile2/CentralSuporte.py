# módulos pyhon

# módulos locais
from src.GUI import Application
from src.update import update

if __name__ == "__main__":
    update()
    
    app = Application()
    app.root.mainloop()