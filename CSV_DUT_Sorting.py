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
    strr=[0 for x in xrange(10000)]
    strr_num=3

    strr[0]="********************************************************"
    strr[1]="This API is to check the POR and stamp-reading status on SATA CNE "
    strr[2]="By Jinqiang   May 14, 2015"
    strr[3]="********************************************************"

    print '''
    "********************************************************
    This API is to check the POR and stamp-reading status on SATA CNE
    By Jinqiang   May 14, 2015
    ********************************************************
    '''
    result_name=''
    Dies=raw_input("Please input the number of dies per DUT: ")
    Dies_perDUT=int(Dies)
    print "Please select the target CSV file:"
    DUTS=set()
    Dut_num = [0 for x in xrange(300)]
    file_name=get_path('*.csv')
    print "Processing file ",file_name
    strr_num=strr_num+1
    strr[strr_num]="Processing file "+file_name

    index=file_name.find('.')
    result_name=file_name[:index]+"-POR Status"+'.txt'

    with open(file_name,'rb') as input_file:

        line_num=0
        for row in input_file:
            line_num=line_num+1

            splits=row.split(',')
            if (((splits[12]=='')==False) and (line_num<>1)):

                DUTS.add(int(splits[0]))
                dut=int(splits[0])
                Dut_num[dut]=Dut_num[dut]+1

    for i in range(0,300):
        if ((Dut_num[i]>0)and (Dut_num[i]<Dies_perDUT)):
            print "DUT number",i,"Has POR Issue"
            strr_num=strr_num+1
            strr[strr_num]="DUT number :" + str(i)+": Has POR Issue"

        elif(Dut_num[i]==Dies_perDUT):
                print "DUT number",i,"POR OK"
                strr_num=strr_num+1
                strr[strr_num]="DUT number :"+str(i)+" : POR OK"

    with open(result_name,'w') as result:
        for i in range(1,strr_num):
            a=str(strr[i])
            result.write(a+'\n')
    print "the result is saved into as below file:"
    print result_name

if __name__ == '__main__':
    main()

