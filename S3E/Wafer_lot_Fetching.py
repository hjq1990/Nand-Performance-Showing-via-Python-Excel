__author__ = '20093'
import csv
import os
import time
from multiprocessing import Pool
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
    line_num = 1
    strr = [0 for i in xrange(1000000)]

    list = get_path('*.txt')
    with open(list, 'r') as list_files:

        lines = list_files.read().splitlines()
        for line in lines:
            Path = line.replace(
                '\\\\cvpmfsip01\\S3E_Data\\', 'x:\\') + '\\Process_TLV'

            if os.path.exists(Path):

                for csv_files in os.listdir(Path):

                    full_path = Path + '\\' + csv_files
                    if csv_files[-4:] == '.csv':
                        with open(full_path, 'r') as f:
                            f.readline()
                            wrong_info = 0
                            wafer_info = f.readline()
                            chars = wafer_info.replace(
                                ',', '').replace(' ', '')[8:]
                            wafer_info = wafer_info.replace(',', ' ')
                            line_num = line_num + 1
                            for i in chars:
                                if ord(i) > 64:
                                    wrong_info = 1

                                    print full_path, "wrong info", chars
                                    strr[line_num] = full_path + \
                                        'wrong info' + chars

                            if (wrong_info == 0):
                                wafer_info = wafer_info.split(' ')[4:]
                                if len(wafer_info) >= 16:
                                    wafer_lot = chr(int(wafer_info[1], 16)) + chr(int(wafer_info[2], 16)) + chr(int(wafer_info[6], 16)) + chr(int(wafer_info[7], 16)) + chr(
                                        int(wafer_info[11], 16)) + chr(int(wafer_info[12], 16)) + chr(int(wafer_info[13], 16)) + chr(int(wafer_info[14], 16)) + chr(int(wafer_info[15], 16))
                                    wafer_num = int(wafer_info[3], 10)
                                    wafer_x = int(wafer_info[4], 10)
                                    wafer_y = int(wafer_info[5], 10)
                                    wafer_date = int(wafer_info[8], 10)
                                    wafer_month = int(wafer_info[9], 10)
                                    wafer_year = int(wafer_info[10], 10)

                                    strr[line_num] = full_path + ' ' + wafer_lot + ' ' + str(wafer_num) + ' ' + str(wafer_x) + ' ' + str(
                                        wafer_y) + ' ' + str(wafer_date) + ' ' + str(wafer_month) + ' ' + str(wafer_year)
                                    print strr[line_num]
                                else:
                                    print full_path, "wrong info", wafer_info
                                    strr[line_num] = full_path + \
                                        'wrong info' + chars
            else:
                print Path, 'Not processed'
    strr[1] = 'Source Wafer_Lot Wafer_Num X Y Date Month Year'
    result_file = 'c:/' + 'Wafer_maps_August_21_SDSS.txt'
    with open(result_file, 'w') as result:
        for i in range(1, line_num + 1):
            a = str(strr[i])
            result.write(a + '\n')
    print "the result is saved into as below file:", result_file


if __name__ == '__main__':
    main()
