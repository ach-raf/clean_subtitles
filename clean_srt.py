import os
import sys
import re

SUPPORTED_MEDIA = ['srt']
SEPARATOR = ','

# path for the txt file that you can edit with new ads separated by SEPARATOR
ads_file_path = r'C:\path\to\ads.txt'


def read_file(_file_path):
    """
    a simple function that open a file in read mode
    :param _file_path: path to a certain file
    :return: opened file
    """
    with open(_file_path, 'r', encoding='utf8') as _file_to_read:
        _file = _file_to_read.read()
    return _file


def get_ads_list(_ads_file_path):
    """
    read and clean the ads file
    :param _ads_file_path: path to the ads file
    :return: a list of each ad
    """
    _ads_to_remove = read_file(_ads_file_path).split(SEPARATOR)
    _ads_to_remove = [ad.strip() for ad in _ads_to_remove]
    return _ads_to_remove


def save_file(_file_path, _content):
    """
    a function that replaces the content of the file with the new _content
    :param _file_path: path to a certain file
    :param _content: the content you want to write to the file
    :return: create or replace a file at the specified _file_path
    """
    with open(_file_path, 'w', encoding='utf8') as _file_to_save:
        _file_to_save.write(str(_content))


def remove_ads_from_srt(_srt_file_path, _ads_to_remove):
    """
    this function cleans an srt file by replacing all the entries in the _ads_to_remove list by an empty string ''
    you can achieve the same results as the regex by simply looping through _ads_to_remove,
    and replacing each item by an empty string.
    I choose to do it this way to try something new.
    """
    join_ads_regex = re.compile('|'.join(map(re.escape, _ads_to_remove)))
    _file_content = join_ads_regex.sub('', read_file(_srt_file_path))
    save_file(_srt_file_path, _file_content)
    print(f'{_srt_file_path} cleaned!')


def clean_folder_of_srt(_file_path, _ads_to_remove):
    """
    takes the path of a selected file and get it's current directory, and clean all ads on that directory.
    :param _file_path: path of selected file
    :param _ads_to_remove: list of ads to remove
    :void: calls the remove_ads_from_srt() for each supported file
    """
    _directory_path = os.path.dirname(_file_path)
    for filename in os.listdir(_directory_path):
        if filename[-3:].lower() in SUPPORTED_MEDIA:
            remove_ads_from_srt(_file_path, _ads_to_remove)


def clean_selected_files():
    """
    we can loop through the selected file(s) respective path,
    we can get the path from a list returned by the sys.argv variable sent by the script
    :void: calls remove_ads_from_srt function on each selected file
    """
    subtitles = sys.argv[1:]
    for subtitle in subtitles:
        remove_ads_from_srt(subtitle, ads_to_remove)


def print_menu():  # much graphic, very handsome
    print(30 * '-', 'MENU', 30 * '-')
    print('1. Clean selected file(s) only')
    print('2. Clean entire folder of selected file')
    print('3. Exit')
    print(66 * '-')


def options_menu():
    user_choice = True
    while user_choice:
        print_menu()
        user_choice = input('What would you like to do? ')
        if user_choice == '1':
            clean_selected_files()
            user_choice = False
        elif user_choice == '2':
            clean_folder_of_srt(sys.argv[1], ads_to_remove)
            user_choice = False
        elif user_choice == '3':
            print('Exit Menu...')
            user_choice = False
        elif user_choice != '':
            print("\nNot a valid choice try again")


ads_to_remove = read_file(ads_file_path).split(',')
ads_to_remove = [ad.strip() for ad in ads_to_remove]
options_menu()
