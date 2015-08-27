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
    line = 0
    file_path = get_path('*.csv')
    Wafer_lots = {
        "DX0789350",
        "DX0788091",
        "DP0785678",
        "DP8787688",
        "DP8788114",
        "DP0788091",
        "DP0779095",
        "DP0779554",
        "DP0779556",
        "DP0789358",
        "DP0788114",
        "DP0789370",
        "DP0788128",
        "DX0785678",
        "DP0679554",
        "DP0787688",
        "DP0788194",
        "DP1788128",
        "DP0795678",
        "DP0788117",
        "DP0788191",
        "DP0788509",
        "DP0787667",
        "DP0587667",
    }
    wafer_list = ''
    with open(file_path, 'r') as f:
        line_num = 0
        for lines in f:
            lin = lines.split(',')

            if line_num > 0:
                if lin[2] in Wafer_lots:

                    strr[line] = lines
                    line = line + 1
                if lin[2] in wafer_list:
                    a = 1
                else:
                    wafer_list = wafer_list + ',' + lin[2]
            else:
                strr[line] = lines
                line = line + 1
            line_num = line_num + 1

    result_file = ('.').join(
        file_path.split('.')[:-1]) + 'wafers_July22' + '.txt'

    with open(result_file, 'w') as result:
        for i in range(1, line + 1):
            a = str(strr[i])
            result.write(a + '\n')
    print "the result is saved into as below file:", result_file
    print wafer_list

if __name__ == '__main__':
    main()
