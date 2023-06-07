h = """ 
 main da interface principal, para utilizar os parâmetros 
 posicionais, você deve utilizar:

    python -m Suporte.[ saf | bitrix | wpp | atendimentos ] comando <valores>

"""
from .GUI import Application

if __name__ == "__main__":
    print(h)

    app = Application()
    app.root.mainloop()