import webbrowser

adress = input("Insert the web adress: ")

try:
    if adress.count('/') > 0:
        if adress.count('/') == 2:
            array_adress = adress.split('//')
            if array_adress[0] != 'http:' and array_adress != 'http:' and array_adress != 'www':
                raise ValueError
            else:
                if array_adress[len(array_adress) - 1] != 'pl' and array_adress[len(array_adress) - 1] != 'com':
                    raise ValueError
                else:
                    print('Given URL is fine.')
                    webbrowser.open(adress)
        else:
            raise ValueError
    else:
        if adress.count('.') > 0:
            array_adress = adress.split('.')
            if array_adress[len(array_adress) - 1] != 'pl' and array_adress[len(array_adress) - 1] != 'com':
                raise ValueError
            else:
                print('Given URL is fine.')
                webbrowser.open(adress)
        else:
            raise ValueError
except ValueError:
    print("URLError, check the adress")


