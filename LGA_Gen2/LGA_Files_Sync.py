__author__ = '20093'

import wx
import os
import shutil
import itertools
from multiprocessing.dummy import Pool as ThreadPool

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

def get_dir():
    app = wx.PySimpleApp()
    dialog = wx.DirDialog(
        None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == wx.ID_OK:
        mydir = dialog.GetPath()
    else:
        mydir = None
    dialog.Destroy()
    return mydir

def main():

    global dest_folder
    folder_list = get_path('*.txt')
    dest_folder = get_dir()
    with open(folder_list, 'r') as fl:
        lines = fl.read().splitlines()
    pool = ThreadPool(4)
    pool.map(Sync_folder, lines)
    pool.close()


def Sync_folder(line):
    global dest_folder
    MAPS_sub = line + '/maps'
    CNE = line[line.rfind('CNE'):line.rfind('CNE') + 4]
    PC = line[line.find('PC'):line.find('PC') + 3]
    Folder = line[line.rfind('_') + 1:]
    sync_path = dest_folder + '/' + Folder + '-' + CNE + '-' + PC
    if os.path.exists(sync_path)==1:
        print 'Already exists sync folder',sync_path
        return 1
    os.mkdir(sync_path)
    print sync_path
    files_to_sync = filter(lambda files: (files[-4:] == '.csv' and files[
                           : 8] == 'MAPS_DUT') or 'Split_EFR.maps.log' in files, os.listdir(MAPS_sub))
    files_paths_to_sync = map(
        lambda file: [MAPS_sub + '\\' + file, sync_path], files_to_sync)
    list(itertools.starmap(shutil.copy, files_paths_to_sync))

if __name__ == '__main__':
    dest_folder = ''
    main()
