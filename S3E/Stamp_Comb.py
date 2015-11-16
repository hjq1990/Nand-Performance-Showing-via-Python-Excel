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
    file_path = get_path('*.txt')
    stamp_data = [0 for i in xrange(1000000)]
    stamp_num = 0
    with open(file_path, 'r') as fl:
        lines = fl.read().splitlines()

        csv_path=map(lambda s:s+'\\ReadStamp.csv',lines)
        csv_list=filter(lambda s:os.path.exists(s),csv_path)
        for csv in csv_list:
            with open(csv,'r') as csv_file:
                for line in csv_file:
                    stamp_num+=1
                    stamp_data[stamp_num]=csv+','+line
        csv_pending=filter(lambda  s:os.path.exists(s)==0,csv_path)
        print 'Below folder is not completely:'
        for i in csv_pending:
            print i
        print '***************************************************'

    # result_file = file_path[:-4] + 'combined_wafer_info' + '.txt'
    # with open(result_file, 'w') as result:
    #     for i in range(1, stamp_num + 1):
    #         a = str(stamp_data[i])
    #         result.write(a + '\n')
    print "the result is saved into as below file:", result_file

if __name__ == '__main__':
    main()
