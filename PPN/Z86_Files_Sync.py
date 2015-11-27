__author__ = '20093'


import wx
import os
import shutil
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
    pool.map(Sync_z86, lines)
    pool.close()

def Sync_z86(line):
    global dest_folder
    sync_status=0
    sub = os.listdir(line)
    DUT_list=filter(lambda s:os.path.isdir(os.path.join(line,s)),sub)

    CNE = line[line.find('PC')-5:line.find('PC')-1]
    PC = line[line.find('PC'):line.find('PC') + 3]
    Folder = line[line.rfind('_') + 1:]
    sync_path = os.path.join(dest_folder, Folder+'-'+CNE+'-'+PC)
    os.mkdir(sync_path)
    for dut in DUT_list:
        files=os.listdir(os.path.join(line,dut))
        maps=filter(lambda s: s[:4]=='MAPS' or 'Split.maps.log',files)

        if len(maps)<=1:
            print 'Not finished processing',os.path.join(line,dut)
        else:
            os.mkdir(os.path.join(sync_path,dut))
            for file in maps:
                shutil.copy(os.path.join(line,dut,file),os.path.join(sync_path,dut,file))
            sync_status=1
    if sync_status==1:
        print 'Sync finish',line
    else:
        print 'Unprocessed folder',line
if __name__ == '__main__':
    main()