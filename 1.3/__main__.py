from diretorio import diretorio
from _main.verificacao_inicial import verificacao_inicial
from GUI.GUI import Application
from GUI.login import Login
from GUI.Menu import Menu


class CentralSuporte:
    """ objeto com verificações iniciais, processos e métodos necessários """

    def __init__(self):

        self.diretorio = diretorio
        self.arquivos_necessarios = ['base_gestao.csv','credentials.json','nomes.csv.gz']
        self.diretorio_padrao = '/_all/_files'

        self.result_verification = verificacao_inicial(self)


if __name__ == "__main__":
    obj = CentralSuporte()
    app = Application(obj.diretorio)

    app.root.mainloop()

    # login = Login(app)
    
    # if login.next_window:
    #     app.root.mainloop()
    
    # Menu(app)
