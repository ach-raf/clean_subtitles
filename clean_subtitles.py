import os
import sys
import re
import util
from pathlib import Path


# ================================ Paths =============================
CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
INFO_FILE_PATH = os.path.join(CURRENT_DIR_PATH, "info.ini")
# ====================================================================

# =============== Reading from info.ini ==============================
CONFIG_INFO = util.read_info_file(INFO_FILE_PATH)
SUPPORTED_MEDIA = [
    media for media in CONFIG_INFO['supported_media'].split(',')]
ADS_SEPARATOR = CONFIG_INFO['ads_separator']

# path for the txt file that you can edit with new ads separated by SEPARATOR
ADS_FILE_PATH = CONFIG_INFO['ads_file_path']


def get_ads_list(_ads_file_path):
    """
    read and clean the ads file
    :param _ads_file_path: path to the ads file
    :return: a list of each ad
    """
    _ads_to_remove = util.read_file(_ads_file_path).split(ADS_SEPARATOR)
    _ads_to_remove = [ad.strip() for ad in _ads_to_remove]
    return _ads_to_remove


def clean_ads_regex(_subtitle_file_path, _ads_to_remove):
    full_path = Path(_subtitle_file_path)
    directory_name = full_path.parent
    file_name = full_path.stem
    file_extension = full_path.suffix

    _content = util.read_file(full_path.absolute())
    between_brackets_regex = r'\[([^]]+)\]'
    # clean _ads_to_remove from empty strings
    _ads_to_remove = [ad for ad in _ads_to_remove if ad]

    # create a dynamic regex based on the start of each ad.
    regex_list = []
    for _ad in _ads_to_remove:
        regex_list.append(f'(^{_ad}.*$)')

    join_ads_regex = ('|'.join(map(re.escape, regex_list)).replace('\\', ''))
    _file_content = re.sub(pattern=join_ads_regex, repl='',
                           string=_content, flags=re.MULTILINE)

    # result = re.findall(join_ads_regex, _text, re.MULTILINE)

    util.save_file(full_path.absolute(), _file_content)
    print(f'{full_path.absolute()} cleaned!')


def clean_folder_of_srt(_subtitle_file_path, _ads_to_remove):
    """
    takes the path of a selected file and get it's current directory, and clean all ads from srt files, in that directory.
    :param _file_path: path of selected file
    :param _ads_to_remove: list of ads to remove
    :void: calls the remove_ads_from_srt() for each supported file
    """
    full_path = Path(_subtitle_file_path)
    directory_name = full_path.parent
    for filename in os.listdir(directory_name):
        if filename[-3:].lower() in SUPPORTED_MEDIA:
            clean_ads_regex(full_path.absolute(), _ads_to_remove)


def clean_selected_files(_ads_to_remove):
    """
    we can loop through the selected file(s) respective path,
    we can get the path from a list returned by the sys.argv variable sent by the script
    :void: calls remove_ads_from_srt function on each selected file
    """
    subtitles = sys.argv[1:]
    for subtitle in subtitles:
        clean_ads_regex(subtitle, _ads_to_remove)


def print_menu():  # much graphic, very handsome
    print(30 * '-', 'MENU', 30 * '-')
    print('1. Clean selected file(s) only')
    print('2. Clean entire folder of selected file')
    print('3. Exit')
    print(66 * '-')


def main():
    user_choice = True
    ads_to_remove = get_ads_list(ADS_FILE_PATH)
    while user_choice:
        print_menu()
        user_choice = input('What would you like to do? ')
        if user_choice == '1':
            clean_selected_files(ads_to_remove)
            user_choice = False
        elif user_choice == '2':
            clean_folder_of_srt(sys.argv[1], ads_to_remove)
            user_choice = False
        elif user_choice == '3':
            print('Exit Menu...')
            user_choice = False
        elif user_choice != '':
            print("\nNot a valid choice try again")


if __name__ == '__main__':
    main()
