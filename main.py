import PySimpleGUI as sg
import convertcurrency


def main():
    sg.theme('SandyBeach')
    # All the stuff inside your window.
    layout = [[sg.Text('Enter the base currency:'), sg.InputText(key='BASE')],
                [sg.Button('Convert')],
                [sg.Multiline(size=(30, 10), key='RESULT')]]

    window = sg.Window('Convert Currency', layout).Finalize()

    while True:
        event, values = window.read()
        if event in (None, 'Close Window'):
            break
        base_currency = values['BASE'].upper()
        result = convertcurrency.convert_currency(base_currency)
        data = []
        for ticker, value in result.items():
            data.append(f"{ticker}: {value}")
            window['RESULT'].update(value='\n'.join([item for item in data]))


if __name__ == "__main__":
    main()
