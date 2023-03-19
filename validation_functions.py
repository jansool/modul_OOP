import exceptions


def name_validation(name):
    if name.isalpha() and len(name)<=20:
        return name
    else:
        print('Use only letters, do not exceed 20 characters')
        raise KeyboardInterrupt


