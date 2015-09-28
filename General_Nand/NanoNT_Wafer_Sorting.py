__author__ = '20093'
import os
import codecs
import time
import wx

def get_dir():
    app = wx.PySimpleApp()
    dialog = wx.DirDialog(
        None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == wx.ID_OK:
        mydir = dialog.GetPath()
    else:
        mydir = None
    dialog.Destroy()
    return mydir
def main():
    folder=get_dir()

    strr=[' ' for i in xrange(100000)]
    line=0
    for file in os.listdir(folder):
        with codecs.open(os.path.join(folder,file), "r",encoding='utf-8', errors='ignore') as UnitInfo:

            die=-1
            lines = UnitInfo.read().splitlines()

            for lin in lines:

                if 'Select Chip' in lin:
                    die=die+1

                    line=line+1
                    strr[line]=strr[line]+file+lin

                if 'Lot ID       : ' in lin:

                    strr[line]=strr[line]+' '+lin
                if 'Wafer Num' in lin:

                    strr[line]=strr[line]+' '+lin
                if 'X            : ' in lin:

                    strr[line]=strr[line]+' '+lin
                if 'Y            : ' in lin:

                    strr[line]=strr[line]+' '+lin

    result_file='c:/'+str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)+'_wafer_id.txt'
    with open(result_file,'w') as result:
        for i in range(1,line+1):
            a=str(strr[i])
            result.write(a+'\n')
    print "the result is saved into as below file:",result_file

if __name__ == '__main__':
    main()


