import os

import time
import wx

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
    filepath = get_path('*.csv')
    Type = raw_input('Please input the type of data to be filtered:')
    CH = raw_input('Please input the CH number:')
    Die = raw_input('Please input the Die number:')
    with open(filepath, 'r') as f:
        line_num = 0
        for lines in f:
            splits = lines.replace(' ', '').split(',')
            if splits[1] == Type and splits[2] == CH and splits[3] == Die:
                if Type==5 or (Type=='7' and splits[8]<>'255'):

                    line_num += 1
                    strr[line_num] = lines


    result_file = filepath[:-4] + '_CH' + CH + '_Die' + Die + '_Type' + Type + '.csv'
    with open(result_file, 'w') as result:
        for i in range(1, line_num + 1):
            result.write(strr[i])
    print "the result is saved into as below file:", result_file

if __name__ == '__main__':
    main()
