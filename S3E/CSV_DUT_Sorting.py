__author__ = '20093'

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
    strr = [0 for x in xrange(1000)]
    strr_num = 3
    strr[0] = "********************************************************"
    strr[
        1] = "This API is to check the POR and stamp-reading status on SATA CNE "
    strr[2] = "By Jinqiang   May 14, 2015"
    strr[3] = "********************************************************"

    print '''
"********************************************************
This API is to check the POR and stamp-reading status on SATA CNE
By Jinqiang   May 14, 2015
********************************************************
'''
    result_name = ''

    Units_perDUT = int(raw_input("Please input the number of units per DUT: "))
    Dies_perUnit = int(raw_input("Please input the number of Dies per unit: "))
    print "Please select the target CSV file:"

    Dut_num = [[0 for x in xrange(4)] for x in xrange(50)]
    file_name = get_path('*.csv')
    print "Processing file ", file_name
    strr_num = strr_num + 1
    strr[strr_num] = "Processing file " + file_name

    index = file_name.find('.')
    result_name = file_name[:index] + "-POR Status" + '.txt'

    FIM = 0

    with open(file_name, 'rb') as input_file:

        line_num = 0
        for row in input_file:
            line_num = line_num + 1

            splits = row.split(',')
            if (len(splits) > 10):
                if (((splits[12] == '') == False) and (line_num <> 1)):
                    FIM = int(splits[2])
                    if (FIM == 0):
                        dut = int(splits[0])
                        Dut_num[dut][0] = Dut_num[dut][0] + 1
                    elif(FIM == 2):
                        dut = int(splits[0])
                        Dut_num[dut][1] = Dut_num[dut][1] + 1

    for i in range(1, 49):
        for j in range(0, Units_perDUT):

            if ((Dut_num[i][j] > 0)and (Dut_num[i][j] < Dies_perUnit)):
                print "Unit on DUT number", i, "FIM ", j, "Has POR Issue"
                strr_num = strr_num + 1
                strr[strr_num] = "Unit on DUT number " + \
                    str(i) + " FIM " + str(j * 2) + " Has POR Issue"

    with open(result_name, 'w') as result:
        for i in range(1, strr_num + 1):
            a = str(strr[i])
            result.write(a + '\n')
    print "the result is saved into as below file:"
    print result_name

if __name__ == '__main__':
    main()
