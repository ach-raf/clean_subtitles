import configparser


def read_info_file(info_file_path):
    """function to read informations from an info.ini file and return a list of info.

    Args:
        file_path ([str]): [path to read regex from]

    Returns:
        [dict]: [dict of credentials]
    """
    config = configparser.ConfigParser()
    config.read(info_file_path)
    credentials = {}
    for section in config.sections():
        for key in config[section]:
            # print(f'{key} = {config[section][key]}')
            credentials[key] = config[section][key]
    return credentials


def read_file(_file_path):
    """
    a simple function that open a file in read mode
    :param _file_path: path to a certain file
    :return: opened file
    """
    with open(_file_path, 'r', encoding='utf8') as _file_to_read:
        _file = _file_to_read.read()
    return _file


def save_file(_file_path, _content):
    """
    a function that replaces the content of the file with the new _content
    :param _file_path: path to a certain file
    :param _content: the content you want to write to the file
    :return: create or replace a file at the specified _file_path
    """
    with open(_file_path, 'w', encoding='utf8') as _file_to_save:
        _file_to_save.write(str(_content))


if __name__ == '__main__':
    # Path: util.py
    print("util.py is a module, not a script.")
