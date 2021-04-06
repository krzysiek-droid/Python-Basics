
def read_file(filename):
    try:
        with open(filename, 'r') as fopen:
            handler = fopen.read()

    except FileNotFoundError:
        return "file not found error"

    if handler == '':
        return 'file is empty!'
    else:
        return handler

def write_file(filename, text):
    try:
        with open(filename, 'x', encoding='UTF-8') as f:
            f.write(text)
    except FileExistsError:
        return 'there is no such file'

    return 'file saved'