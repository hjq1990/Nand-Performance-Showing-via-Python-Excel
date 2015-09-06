__author__ = '20093'


from functools import partial
import glob
import os
from openpyxl import Workbook
import wx

# Get_path is refered from this site:
# http://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python


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

    All_FF = 'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF'
    ALl_00 = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'

    filename = get_path('*.pat')
    filename_save = filename[:-4] + '-new.pat'
    print "Processing File", filename
    bytes_per_line = 16
    line_of_FF = 0x7
    line_of_00 = 0x9

    str = [0 for i in xrange(0x50000)]

    with open(filename, 'rb') as binary_file:
        line_num = 0
        for block in iter(partial(binary_file.read, bytes_per_line), ''):
            s1 = ' '.join('{0:02x}'.format(ord(b)) for b in block)
            str_lin = line_num / 0x450 * 0x465 + line_num % 0x450
            str[str_lin] = s1
            if line_num % 0x450 == 0x448:
                print '0x448: ', s1
            if line_num % 0x450 == 0x449:
                print '0x449: ', s1
            line_num = line_num + 1
    for i in range(0, (line_num + 1) / 0x450):
        for j in (0, line_of_FF):
            str[i * 0x465 + 0x450 + j] = All_FF
        for k in (0, line_of_00):
            str[i * 0x465 + 0x456 + k] = ALl_00
    # bins=bytearray(str[:(line_num / 0x450+1) *0x465])
    print str
    # new_FILE=open(filename_save,'wb')
    # new_FILE.write(bins)


if __name__ == '__main__':
    main()
