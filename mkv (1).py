import os
from pymkv import *
import re
import time

verify_mkvmerge()
# Folder directories
folder_dir = os.path.dirname(__file__)
parent_folder = os.path.join(folder_dir, 'mkvfiles')
output_folder = os.path.join(parent_folder, 'output')


def mkv_path_list():
    mkv_files = []
    for root, dirnames, filenames in os.walk(parent_folder):
        for filename in filenames:
            if filename.endswith('.mkv'):
                mkv_files.append(os.path.join(root, filename))
    return mkv_files


def mkv_file_name():
    mkv_file = []
    for root, dirnames, filenames in os.walk(parent_folder):
        mkv_file.extend(filenames)
        break
    clean_mkv = []
    for file in mkv_file:
        replaced = file.replace('.mkv', '')
        clean_mkv.append(replaced)
    return clean_mkv


def fonts_list():
    font_list = []
    for root, dirnames, filenames in os.walk(parent_folder):
        for filename in filenames:
            if filename.endswith('ttf') or filename.endswith('otf'):
                font_list.append(os.path.join(root, filename))
    return font_list


# Will match and remux it.

def get_matches(mkv_file, mkv_path, font_list):
    for i in range(len(mkv_file)):
        pattern = re.compile(mkv_file[i])
        mkv = MKVFile(mkv_path[i])
        for j in range(len(font_list)):
            matches = pattern.findall(font_list[j])
            if matches:
                mkv.add_attachment(font_list[j])
                mkv.mux(output_folder + "\{}.mkv".format(mkv_file_name()[i]))


get_matches(mkv_file_name(), mkv_path_list(), fonts_list())


print("DONE")
