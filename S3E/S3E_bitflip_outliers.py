__author__ = '20093'
import wx
import csv
import os


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
    strr = ['' for i in xrange(10000000)]

    file_path = get_path('*.csv')
    print file_path
    with open(file_path, 'r') as fbc_file:
        for line in fbc_file:
            splits = line.split(',')

            # if splits[9] == '':
                # if int(splits[11], 10) > 10:
                #     print line
            if splits[9]=='3' or splits[9]=='2':

                if int(splits[11],10)>100:
                    print line

if __name__ == '__main__':
    main()
