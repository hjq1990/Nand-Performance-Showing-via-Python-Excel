__author__ = '20093'
import wx
import os
import shutil
import time
import itertools
from multiprocessing import Pool
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
    folder_file=get_path('*.txt')
    print folder_file,'is selected to check'
    with open(folder_file,'r') as f:
        lines = f.read().splitlines()
        TLV_lists=map(lambda s:s+'\\Process_TLV\\rake.parse.log',lines)
        Rake=filter(lambda s:os.path.exists(s),TLV_lists)
        Rake_No=filter(lambda s:os.path.exists(s)==0,TLV_lists)
        print 'Below folder is not completely decoded:'
        for i in Rake_No:
            print i,'Not completed decoding'
        print '***************************************************'
        for rake_file in Rake:
            Decode_check(rake_file)

def Decode_check(file):
    with open(file,'r') as f:
        lines = f.read().splitlines()
    print file, 'Contains ', len(lines),'Decoded duts',
    Pass=filter(lambda s:s[-4:]=='PASS',lines)
    print len(Pass),'duts passed',len(lines)-len(Pass),'Failed duts'

if __name__ == '__main__':
    main()