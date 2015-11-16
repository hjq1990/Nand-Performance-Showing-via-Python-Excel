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

    folder_file = get_path("*.txt")
    print folder_file, 'is selected to check'
    with open(folder_file, 'r') as f:
        lines = f.read().splitlines()
        TLV_lists = map(lambda s: s.split()[
                        2] + '\\Process_TLV\\rake.parse.log', lines)
        Rake = filter(lambda s: os.path.exists(s), TLV_lists)
        Rake_No = filter(lambda s: os.path.exists(s) == 0, TLV_lists)
        print 'Below folder is not completely decoded:'
        for i in Rake_No:
            print i, 'Not completed decoding'
        print '***************************************************'

        for line in lines:

            TLV = os.path.join(line.split()[2], 'Process_TLV')
            csv_dut = map(lambda s: os.path.join(TLV, s), os.listdir(TLV))
            csv_file = filter(lambda s: s[-4:] == '.csv', csv_dut)

            for csv in csv_file:
                file_size = 0
                if line.split()[1] == 'bonfire_ext_3.0.bin':
                    file_size = 4000000000
                elif line.split()[1] == "EFR_ext_3.0.bin":
                    file_size = 5000000000
                if os.path.getsize(csv) < file_size:
                    print csv[:csv.find('Proce') - 1], csv[csv.find('Proce') + 12:], os.path.getsize(csv), file_size

if __name__ == '__main__':
    main()
