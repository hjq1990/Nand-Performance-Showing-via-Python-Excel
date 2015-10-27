__author__ = '20093'

import wx
import os
import shutil
import time


def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path


def main():

    dest_folder = 'Z:\Active\Jinqiang\Y5'
    folder_list = get_path('*.txt')

    with open(folder_list, 'r') as fl:
        lines = fl.read().splitlines()
        for line in lines:
            CNE = line[line.find('CNE'):line.find('CNE') + 3]
            PC = line[line.find('PC'):line.find('PC') + 3]
            Folder = line[line.rfind('_') + 1:]
            MAPS_sub = line.split(' ')[1]

            dest_folder_sub = os.path.join(dest_folder, line.split(' ')[0][0:line.split(
                ' ')[0].find('health') - 1] + '-' + Folder + '-' + CNE + '-' + PC)

            print MAPS_sub, dest_folder_sub
            if os.path.exists(dest_folder_sub) == 0:
                os.mkdir(dest_folder_sub)
            file_num = 0
            for file in os.listdir(MAPS_sub):
                if file[-4:] == '.csv' and 'MAPS' in file:
                    file_path = os.path.join(MAPS_sub, file)
                    file_num += 1
                    shutil.copy(file_path, dest_folder_sub)
                    print file_path, dest_folder_sub
            if file_num < 12:
                print MAPS_sub, 'Missing data'


if __name__ == '__main__':
    main()
