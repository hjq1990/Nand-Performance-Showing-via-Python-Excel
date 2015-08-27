__author__ = '20093'
import wx
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
    folder_path =get_path('*.txt')
    stamp_data=[0 for  i in xrange(1000000)]
    stamp_num=0


    with open(folder_path, 'r') as fl:
        lines = fl.read().splitlines()

        for line in lines:
            for files in os.listdir(line):
                if files[-4:]=='.csv' and 'ReadStamp' in files:
                    with open (line+'/'+files,'r') as stamp_file:
                        for stamp_line in stamp_file:
                            stamp_num=stamp_num+1
                            stamp_data[stamp_num]=stamp_line

    result_file =folder_path[:-4]+'combined_wafer_info'+'.txt'
    with open(result_file, 'w') as result:
        for i in range(1, stamp_num + 1):
            a = str(stamp_data[i])
            result.write(a + '\n')
    print "the result is saved into as below file:", result_file

if __name__ == '__main__':
    main()