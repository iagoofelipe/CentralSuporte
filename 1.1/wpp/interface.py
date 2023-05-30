import PySimpleGUI as sg

def interface():
    sg.theme('LightGray1')

    layout = [
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('IAGO', key='-NOME-')],
            [sg.Text(key='-NOME_OLD-', font=("Helvetica", 9)), sg.Text(key='-VALOR-', font=("Helvetica", 9))],
            [sg.Text('')],
            [sg.Button('Em branco'), sg.Push(), sg.Button('Avançar')]
            ]

    return sg.Window(
        title='Programas', 
        layout=layout, 
        finalize=True, 
        font=("Helvetica", 13), 
        size=(300,250)
        )