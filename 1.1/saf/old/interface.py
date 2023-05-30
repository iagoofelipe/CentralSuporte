import PySimpleGUI as sg

def interface():
    sg.theme('LightGray1')

    layout = [
            [sg.Text()],
            [sg.Text('Digite o cpf a ser adicionado (somente números):')],
            [sg.Input(key='-INPUT-')],
            [sg.Text(key='-ALERT-', text_color='red', font=('Helvetica', 9))],
            [sg.Text('para extrair dados do bitrix, acresente /b aos parâmetros do comando', font=('normal', 9), text_color='#808080')],
            [sg.Button('Adicionar'), sg.Push(), sg.Button('Finalizar')]
            ]

    return sg.Window(
        title="CPF's para SAF", 
        layout=layout, 
        finalize=True, 
        font=("Helvetica", 13)
        )

def newDados():
    window = interface()
    dados = []

    while True:
        event, values = window.read()
            
        if event == 'Adicionar':
            cpf = values['-INPUT-']

            if len(cpf) == 11 and cpf.isdigit():
                cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}'

                dados.append(cpf)
                window['-INPUT-'].update('')
                window['-ALERT-'].update('')
            
            else:
                window['-ALERT-'].update('CPF inválido!')


        if event in (sg.WIN_CLOSED, 'Finalizar'):
            break

    window.close()
    return dados